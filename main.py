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
    driver.get("https://sigma.innsandbox.com/")

    assert 'Sigma Analytics: Unlock The Potential of Data' == driver.title

def test_login(driver):

    driver.find_element(by=By.CLASS_NAME, value = 'login-span').click()
    #driver.find_element_by_name('login').click()
    #driver.find_element(By.ID, 'submit').click()


    el = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'login-email')
    ))

    el.send_keys('e212f98a6478@moakt.cc')
    time.sleep(2)
    # driver.find_element(by=By.CLASS_NAME, value = 'mail-input').send_keys('e212f98a6478@moakt.cc')
    #driver.find_element_by_name('email').send_keys('01002977342')
    #driver.find_element(By.ID, 'email').send_keys('01002977342')

    driver.find_element(by=By.CLASS_NAME, value = 'icon-btn').click()
    #driver.find_element_by_name('login').click()
    #driver.find_element(By.ID, 'submit').click()

    el = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'password-input')
    ))

    el.send_keys('Aa111111')
    time.sleep(2)
    #driver.find_element(by=By.NAME, value = 'password-input ng-pristine ng-valid ng-touched').text.send_keys('Aa111111')
    #driver.find_element_by_name('pass').send_keys('01002977342ass')
    #driver.find_element(By.ID, 'pass').send_keys('01002977342ass')

    driver.find_element(by=By.CLASS_NAME, value = 'login-pass-btn').click()
    #driver.find_element_by_name('login').click()
    #driver.find_element(By.ID, 'submit').click()



    assert '' in driver.current_url
