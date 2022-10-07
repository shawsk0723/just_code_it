from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time 


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = 'https://naver.com' 
#driver.maximize_window() 
#action = ActionChains(driver) 
driver.implicitly_wait(5)
driver.get(url) 
#driver.maximize_window() 

elem = driver.find_element(By.CLASS_NAME, 'link_login')
elem.click()

driver.find_element(By.NAME, 'id').send_keys('xxxxx')
driver.find_element(By.NAME, 'pw').send_keys('yyyyy')

elem = driver.find_element(By.CLASS_NAME, 'btn_login')
elem.click()

print('press Enter to Quit ~')
input()

