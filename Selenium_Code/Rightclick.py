import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
rightclick = driver.find_element(By.XPATH, "//span[normalize-space() = 'right click me']")
driver.implicitly_wait(3)

Act = ActionChains(driver)
Act.context_click(rightclick).perform()
time.sleep(5)