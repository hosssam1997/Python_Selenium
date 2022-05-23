import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()
    driver.quit()


def test_verify_title(driver):
    driver.get("https://www.facebook.com/")

    assert 'Facebook – log in or sign up' == driver.title

def test_login(driver):
    driver.find_element(by=By.NAME, value = 'email').send_keys('01002977342')
    #driver.find_element_by_name('email').send_keys('01002977342')
    #driver.find_element(By.ID, 'email').send_keys('01002977342')

    driver.find_element(by=By.NAME, value = 'pass').send_keys('01002977342ass')
    #driver.find_element_by_name('pass').send_keys('01002977342ass')
    #driver.find_element(By.ID, 'pass').send_keys('01002977342ass')

    driver.find_element(by=By.NAME, value = 'login').click()
    #driver.find_element_by_name('login').click()
    #driver.find_element(By.ID, 'submit').click()
    assert 'facebook' in driver.current_url
