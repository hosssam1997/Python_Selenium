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
    driver.get("http://dbankdemo.com/bank/login")

    assert 'Digital Bank' == driver.title

def test_login(driver):
    driver.find_element(by=By.NAME, value = 'username').send_keys('jsmith@demo.io')
    #driver.find_element_by_name('email').send_keys('01002977342')
    #driver.find_element(By.ID, 'email').send_keys('01002977342')

    driver.find_element(by=By.NAME, value = 'password').send_keys('Demo123!')
    #driver.find_element_by_name('pass').send_keys('01002977342ass')
    #driver.find_element(By.ID, 'pass').send_keys('01002977342ass')

    driver.find_element(by=By.ID, value = 'submit').click()
    #driver.find_element_by_name('login').click()
    #driver.find_element(By.ID, 'submit').click()
    assert 'home' in driver.current_url

from time import sleep
def test_verify_version(driver):
    driver.find_element(by=By.ID, value='aboutLink').click()
    sleep(1)
    assert '2.1.0.11' in driver.find_element(by=By.CLASS_NAME, value='modal-body').text