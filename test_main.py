import main as m
import pytest
import requests 

# check url accessibility
def test_url_accessibility():
    url = 'https://diyprojects.com'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(url, headers=headers, verify=False)
    status = page.status_code
    assert status == 200
