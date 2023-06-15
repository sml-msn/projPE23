import streamlit as st
import pytest
import requests
from PIL import Image
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions
import subprocess
process = subprocess.Popen(["streamlit", "run", 'main.py'])
from main import preprocess_image, load_image, print_predictions

@st.cache(allow_output_mutation=True)
def load_model():
    return EfficientNetB0(weights='imagenet')
model = load_model()

def test_prep_img():
    #with open() as image_data:
    #assert preprocess_image(Image.open(io.BytesIO(image_data))) is not None
    assert preprocess_image(Image.open(r"pictures/wine_bottle.jpg")) is not None

def test_jpg():
    x = preprocess_image(Image.open(r"pictures/wine_bottle.jpg"))
    preds = model.predict(x)
    classes = decode_predictions(preds, top=3)[0] # takes 3 preds and puts in predLst
    assert classes[0][1].split('_').count('bottle') > 0

# check url accessibility
def test_url_accessibility():
    url = 'https://diyprojects.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200

# check url accessibility
def test_url_accessibility_2():
    url = 'https://www.hometalk.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200    
    
# check url accessibility
def test_url_accessibility_3():
    url = 'https://diyjoy.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200   
