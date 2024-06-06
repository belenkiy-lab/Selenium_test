import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://testautomationpractice.blogspot.com/')

time.sleep(5)
wiki_icon = driver.find_element('class name', 'wikipedia-icon')
print('лемент вики', wiki_icon)
print()
wiki_form = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
print('форма', wiki_form)
print()
wiki_button = driver.find_element('class name', 'wikipedia-search-button')
print('кнопка вики', wiki_button)
print()
new_b_w = driver.find_elements(By.TAG_NAME, 'h2')[3]
print('new bro window', new_b_w)
print(new_b_w.text)
print()
