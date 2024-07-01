import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.nopcommerce.com/en/demo")
# driver.maximize_window()
# #driver.switch_to.new_window("Tab")
# driver.switch_to.new_window("window")
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
ORANGEHRMRIGHTS = Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").send_keys(ORANGEHRMRIGHTS)
time.sleep(5)