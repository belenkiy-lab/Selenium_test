from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://vk.com/')

first_url = driver.current_url
first_title = driver.title
print('заголовок страницы: ', first_title)

driver.get('https://ya.ru/')
second_title = driver.title
print('заголовок страницы: ', second_title)

driver.back()
assert driver.current_url == first_url
driver.refresh()
print('адресс страницы: ', driver.current_url)

driver.forward()
assert driver.current_url != first_url
