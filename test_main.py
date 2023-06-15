import streamlit as st
import pytest
import requests 
import main as m
#st.session_state.switcher = -2 #testing state


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
