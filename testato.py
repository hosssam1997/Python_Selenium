import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        """Explicitly create a Chrome browser instance."""
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        """Assert that title of page says 'Google'."""
        self.browser.get('https://sigma.innsandbox.com/')
        self.assertIn('Sigma Analytics: Unlock The Potential of Data', self.browser.title)

    def test_search_page_title(self):
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

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-email')
        ))
        el.send_keys('e212f98a6478@moakt.cc')
        time.sleep(5)
        # driver.find_element(by=By.CLASS_NAME, value = 'mail-input').send_keys('e212f98a6478@moakt.cc')
        # driver.find_element_by_name('email').send_keys('01002977342')
        # driver.find_element(By.ID, 'email').send_keys('01002977342')

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'icon-btn')
        ))
        el.click()
        time.sleep(5)
        #self.browser.find_element(by=By.CLASS_NAME, value='icon-btn').click()
        # driver.find_element_by_name('login').click()
        # driver.find_element(By.ID, 'submit').click()

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'password-input')
        ))

        el.send_keys('Aa111111')
        time.sleep(5)
        # driver.find_element(by=By.NAME, value = 'password-input ng-pristine ng-valid ng-touched').text.send_keys('Aa111111')
        # driver.find_element_by_name('pass').send_keys('01002977342ass')
        # driver.find_element(By.ID, 'pass').send_keys('01002977342ass')

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'login-pass-btn')
        ))
        el.click()
        time.sleep(5)
        #self.browser.find_element(by=By.CLASS_NAME, value='login-pass-btn').click()
        # driver.find_element_by_name('login').click()
        # driver.find_element(By.ID, 'submit').click()

        el = WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'menu-details active-menu')
        ))
        el.click()
        time.sleep(5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")



if __name__ == '__main__':
    unittest.main(verbosity=2)