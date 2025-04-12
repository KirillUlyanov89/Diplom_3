from selenium import webdriver
import requests
import pytest
import src.helpers
import src.data

@pytest.fixture(scope='function')
def create_user():
    email, password, name = src.helpers.generate_user_data()
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(src.data.CREATE_USER_API_URL, data=payload)
    token = response.json().get("accessToken")
    
    yield email, password, name
    requests.delete(src.data.DELETE_USER_API_URL, headers={"Authorization": f'{token}'})
    
@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome()
    elif request.param == 'firefox':
        web_driver = webdriver.Firefox()
        
    yield web_driver
    web_driver.quit()
    
@pytest.fixture(scope='function')
def login_user_and_create_order(create_user):
    email, password, _ = create_user
    payload = {
        'email': email,
        'password': password,
    }
    response = requests.post(src.data.LOGIN_USER_API_URL, data=payload)
    token = response.json().get("accessToken")
    payload = {
        "ingredients": [src.data.CRATER_BUN_ID, src.data.FILLET_MAIN_ID, src.data.CHEESE_MAIN_ID, src.data.SPICY_SAUCE_ID]
    }
    response = requests.post(src.data.CREATE_ORDER_API_URL, headers={"Authorization": f'{token}'}, data=payload)
    number = str(response.json()['order']['number'])
    return email, password, number