import time
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
cookiestotal = driver.get_cookies()
print(len(cookiestotal))
print(cookiestotal)

driver.delete_cookie("orangehrm")
cookiestotal = driver.get_cookies()
print(len(cookiestotal))
print(cookiestotal)
driver.implicitly_wait(5)
driver.add_cookie({'domain': 'opensource-demo.orangehrmlive.com', 'httpOnly': True, 'name': 'orangehrm', 'path': '/web', 'sameSite': 'Lax', 'secure': True, 'value': 'a3d64dc5b79e7406a34ecdea43ea0299'})
cookiestotal = driver.get_cookies()
print(len(cookiestotal))
print(cookiestotal)