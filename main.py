import io
import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
from bs4 import BeautifulSoup
import requests


@st.cache(allow_output_mutation=True)
def load_model():
    return EfficientNetB0(weights='imagenet')


def preprocess_image(img):
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x


def load_image():
    uploaded_file = st.file_uploader(label='Choose image')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def print_predictions(preds):
    classes = decode_predictions(preds, top=3)[0]
    for cl in classes:
        st.write(cl[1], cl[2])


# getting a proper thing name from the list
def createThingName(thingNameLst, delim):
    thingName = ''
    firstWord = True
    for word in thingNameLst:
        if firstWord:
            thingName = thingName + word
            firstWord = False
        else:
            thingName = thingName + delim + word
    return thingName


# making a soup from the page
def createSoup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup


# getting content from https://diyprojects.com/
def getContent_1(thingNameLst):
    thingName = createThingName(thingNameLst, delim = '+')
    
    url = f'https://diyprojects.com/?s={thingName}'
    soup = createSoup(url)
    
    filteredData = []
    allData = []
    
    allData = soup.findAll('article')
    for data in allData:
        filtered = []
        if data.find('a', attrs={'class': 'entry-title-link'}) is not None:
            filtered.append(data.find('a', attrs={'class': 'entry-title-link'}).get('href'))
            filtered.append(data.find('a', attrs={'class': 'entry-title-link'}).text)
            filtered.append(data.find('img', attrs={'class': 'alignleft post-image entry-image'}).get('src'))
            filtered.append(data.find('div', attrs={'class': 'entry-content'}).find('p').text)
            filteredData.append(filtered)
    
    return filteredData


# getting content from https://www.hometalk.com
def getContent_2(thingNameLst):
    thingName = createThingName(thingNameLst, delim = '%20')
    
    url = f'https://www.hometalk.com/search/all?filter={thingName}'
    soup = createSoup(url)
    
    filteredData = []
    allData = []
    
    allData = soup.find_all('div', {'class': 'media-component relative js-pin-item'})
    for data in allData:
        filtered = []
        if (data.find('a', attrs={'class': 'js-card-img'}) is not None) and ((data.find('img') is not None)):
            filtered.append('https://www.hometalk.com' + data.find('a', attrs={'class': 'js-card-img'}).get('href'))
            filtered.append(data.find('img').get('alt'))
            #filtered.append(data.find('div', {'class': 'post-body'}).find('a').text)
            filtered.append(data.find('img').get('data-src'))
            filtered.append(None)
            filteredData.append(filtered)
            
    return filteredData


# getting content from https://diyjoy.com
def getContent_3(thingNameLst):
    thingName = createThingName(thingNameLst, delim = '+')
    
    url = f'https://diyjoy.com/?s={thingName}'
    soup = createSoup(url)
    
    filteredData = []
    allData = []
    
    allData = soup.findAll('article')
    for data in allData:
        filtered = []
        if data.find('a', attrs={'class': 'video-index-block-img-link'}) is not None:
            filtered.append(data.find('a', attrs={'class': 'video-index-block-img-link'}).get('href'))
            filtered.append(data.find('a', attrs={'class': 'video-index-block-img-link'}).get('title'))
            filtered.append(data.find('img').get('src'))
            filtered.append(data.find('div', attrs={'class': 'entry-summary'}).find('p').text)
            filteredData.append(filtered)
    
    return filteredData


# printing data parsed from the web page
def printDiyData(thingNameLst):
    diyData = getContent_1(thingNameLst) + getContent_2(thingNameLst) + getContent_3(thingNameLst) 
    if len(diyData) < 10:
        x = len(diyData)
    else:
        x = 10
    for i in range(x):
        st.header(diyData[i][1])
        st.write(diyData[i][0])
        st.image(diyData[i][2])
        if diyData[i][3] != None:
            st.write(diyData[i][3])
        st.write('------------------')

model = load_model()

st.title('Give it a chance!')
if 'switcher' not in st.session_state:
    st.session_state.switcher = -1 # index for predLst (see the next line)
if 'predLst' not in st.session_state:
    st.session_state.predLst = [] # list of predictions, example: 
                                  # [[0.96, 'thing_one'],[0.70, 'thing_three'],[0.54, 'thing_three']]

img = load_image()

# the first try that gives us the most probable variant of prediction
if st.button('Scan image'):
    st.session_state.switcher = 0
    x = preprocess_image(img)
    preds = model.predict(x)
    st.session_state.predLst = decode_predictions(preds, top=3)[0] # takes 3 preds and puts in predLst
    st.subheader(f'it is a {st.session_state.predLst[st.session_state.switcher][1]}')
    printDiyData(st.session_state.predLst[st.session_state.switcher][1].split('_'))

# if pressed: the second try that gives us the second probable variant of prediction
if st.session_state.switcher == 0:
    if st.button(f'No, it\'s NOT a {st.session_state.predLst[st.session_state.switcher][1]}'): 
        st.session_state.switcher += 1
        st.subheader(f'it is a {st.session_state.predLst[st.session_state.switcher][1]}')
        printDiyData(st.session_state.predLst[st.session_state.switcher][1].split('_'))

# if pressed: the third try that gives us the third probable variant of prediction
if st.session_state.switcher == 1:
    if st.button(f'No, it\'s NOT a {st.session_state.predLst[st.session_state.switcher][1]}'): 
        st.session_state.switcher += 1
        st.subheader(f'it is a {st.session_state.predLst[st.session_state.switcher][1]}')
        printDiyData(st.session_state.predLst[st.session_state.switcher][1].split('_'))

# the instructions button is on the screen
if st.session_state.switcher == 2:
    if st.button('How do I utilize it?'): # if pressed: shows an image with instructions
        instructionImg = Image.open('pamyatkamusor.png')
        st.image(instructionImg)
