import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# clicking on link
# link = driver.find_element(By.LINK_TEXT, "Documentation")
# link.click()
# time.sleep(3)

#finding all the links
# links = driver.find_elements(By.XPATH, '//a')
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))
