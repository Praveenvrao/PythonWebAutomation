import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
dragbox = driver.find_element(By.XPATH, '//*[@id="box3"]')
sourcebox = driver.find_element(By.XPATH, '//*[@id="box103"]')

act = ActionChains(driver)
act.drag_and_drop(dragbox,sourcebox).perform()
time.sleep(5)