import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_search_page(self):
        """Assert that Google search returns data for 'Red Hat'."""
        self.browser.get('https://sigma.innsandbox.com/')
        self.assertIn('Sigma Analytics: Unlock The Potential of Data', self.browser.title)
        element = self.browser.find_element(by=By.XPATH, value='/html/body/app-root/app-homepage/app-header/div[1]/div[2]/div[2]/input')
        assert element is not None
        element.send_keys('a' + Keys.RETURN)

        #Read more btn
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/app-dashboards/div[4]/div[3]/div[3]/div/div[1]/div/p[2]/span[2]')
        ))
        el.click()
        time.sleep(3)

        #X btn
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/app-dashboards/div[5]/div/div/div[1]/button/img')
        ))
        el.click()
        time.sleep(4)
        window_before = self.browser.window_handles[0]
        #print(window_before)

        #view dashboard page
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/app-root/app-dashboards/div[4]/div[3]/div[3]/div/div[1]/div/a/p')
        ))
        el.click()
        time.sleep(5)

        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        #print(window_after)

        #login

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-span')
        ))
        el.click()
        time.sleep(5)

        #Enter email address
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-email')
        ))
        slow_typing(el, 'e212f98a6478@moakt.cc')
        #el.send_keys('e212f98a6478@moakt.cc')
        #time.sleep(5)

        #Click on login btn
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'icon-btn')
        ))
        el.click()
        #time.sleep(5)

        #Enter password
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'password-input')
        ))
        slow_typing(el, 'Aa111111')
        #el.send_keys('Aa111111')

        #show password
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'mat-icon')
             ))
        el.click()
        time.sleep(5)

        #remember me check box
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'mat-checkbox-inner-container')
             ))

        if el.get_attribute("checked") != "true":
            el.click()
            time.sleep(5)

        #Click on password btn
        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-pass-btn')
        ))
        el.click()
        time.sleep(5)

        video = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'home-pageimg')
        ))
        video.send_keys(Keys.SPACE)  # hits space
        time.sleep(1)
        video.click()

        time.sleep(5)


if __name__ == '__main__':
    unittest.main(verbosity=2)