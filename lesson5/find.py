import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://www.freeconferencecall.com/login')

time.sleep(5)

driver.find_element('id','loginformsubmit').click()

time.sleep(5) 
