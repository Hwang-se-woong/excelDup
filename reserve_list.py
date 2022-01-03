from selenium import webdriver
import private_info
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
import requests
import login

driver = login.driver

try:
    WebDriverWait(driver,1).until(EC.alert_is_present())
    alert = driver.switch_to_alert()
    alert.accept()
except :
    print('no alert!?')

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/aside/div[1]/ul/li/a/span').click()

try:
    print('try')
except:
    print('no alert!!!')

print(driver.find_elements(By.CSS_SELECTOR, '#__BVID__158 > tbody'))
driver.find_element(By.CSS_SELECTOR, '#__BVID__158 > tbody').click()
#driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/main/div/div/div/div/div/div[1]/button').click()
#driver.find_element(By.XPATH,'//*[@id="Medical_history_download"]').click()

#driver.quit()