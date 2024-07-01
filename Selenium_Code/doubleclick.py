import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.implicitly_wait(2)
dragframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")
driver.switch_to.frame(dragframe)
field1 = driver.find_element(By.XPATH, "//input[@id='field1']")
field1.clear()
field1.send_keys("Doubleclick")

copytext = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")

Act = ActionChains(driver)
Act.double_click(copytext).perform()
time.sleep(5)