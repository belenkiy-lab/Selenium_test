"""Инициализация Chrome"""


import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get('https://wikipedia.org/')

url = driver.current_url
current_title = driver.title
print('адресс страницы: ', url)
print('заголовок страницы: ', current_title)
assert url == 'https://www.wikipedia.org/', 'открылся не тот адрес'
assert current_title == 'Wikipedia', 'ошибка в заголовке'

print(driver.page_source)

time.sleep(4)
