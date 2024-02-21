import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,'OrangeHRM, Inc').click()
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(4)

# currentwindow = driver.current_window_handle
# print(currentwindow)
#
# #Approach 1
# windowids = driver.window_handles
# print(windowids[0], windowids[1])

# driver = webdriver.Chrome()
# driver.get("https://www.cricbuzz.com/")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//a[@title='Live Cricket Score']").click()