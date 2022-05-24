from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'

browser = webdriver.Chrome()
browser.get(('https://accounts.google.com/ServiceLogin?'
'service=mail&continue=https://mail.google'
'.com/mail/#identifier'))


#another_account_btn = browser.find_element(by=By.XPATH, value='//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div')
#another_account_btn.click()

email = browser.find_element(by=By.XPATH, value='//*[@id="identifierId"]')
email.send_keys(usernameStr)

#next_btn = browser.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/div[3]')
next_btn = browser.find_element(by=By.CLASS_NAME, value="VfPpkd-vQzf8d")
next_btn.click()


# wait for transition then continue to fill items
passw = WebDriverWait(browser, 10).until(
EC.presence_of_element_located((By.NAME, 'password')))
passw.send_keys(passwordStr)

#passw = browser.find_element(by=By.NAME, value='password')
#passw.send_keys(passwordStr)

show_btn = browser.find_element(by=By.XPATH, value='//*[@id="c2"]')
show_btn.click()

next_btn_2 = browser.find_element(by=By.XPATH, value='//*[@id="passwordNext"]/div/button/span')
next_btn_2.click()


