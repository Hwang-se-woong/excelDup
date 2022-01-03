from selenium import webdriver
import private_info
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

delay = 3
url = "https://linedoctor-cms.line-beta.biz/login"
driver = webdriver.Chrome('/Users/user/Downloads/chromedriver')
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="login"]').click()

driver.find_element(By.NAME, 'email').send_keys(private_info.id)
driver.find_element(By.NAME, 'password').send_keys(private_info.pw)
driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div[2]/form/div/div[5]/button').click()

try:
    WebDriverWait(driver,1).until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()
except :
    print('no alert!?')

#driver.find_element(By.XPATH, '//*[@id="login_admin"]').click()
driver.find_element(By.XPATH, '//*[@id="login_doctor"]').click()
