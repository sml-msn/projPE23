import streamlit as st
# import pytest
import requests
from PIL import Image
# import numpy as np
from tensorflow.keras.applications import EfficientNetB0
# from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import decode_predictions  # preprocess_input
from main import preprocess_image


@st.cache(allow_output_mutation=True)
def load_model():
    return EfficientNetB0(weights='imagenet')


model = load_model()


# testing image preprocessing
def test_prep_img():
    assert preprocess_image(Image.open(r"pictures/wine_bottle.jpg")) is not None


# testing prediction
def test_pred():
    x = preprocess_image(Image.open(r"pictures/wine_bottle.jpg"))
    preds = model.predict(x)
    classes = decode_predictions(preds, top=3)[0]
    assert classes[0][1].split('_').count('wine') > 0


# check url accessibility: diyprojects.com
def test_url_accessibility():
    url = 'https://diyprojects.com'
    headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
               AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200


# check url accessibility: hometalk.com
def test_url_accessibility_2():
    url = 'https://www.hometalk.com'
    headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
               AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200


# check url accessibility: diyjoy.com
def test_url_accessibility_3():
    url = 'https://diyjoy.com'
    headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) \
               AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200
