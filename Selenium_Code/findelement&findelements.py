import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()

#Locator matching with single element
#element1 = driver.find_element(By.XPATH,"//input[@id = 'twotabsearchtextbox']")
#element1.send_keys("Iphone")
#time.sleep(5)
#print(element1.text)
#print(element1.get_attribute('placeholder'))
#driver.quit()

#Locator matching with multiple elements
#element2 = driver.find_element(By.XPATH,"//div[@class = 'navFooterColHead']")
#print(element2.text)
#print(element2.get_attribute('class'))
#driver.quit()

#Element not available then throwing NoSuchElementException
#element3 = driver.find_element(By.XPATH,"//div[@class = 'navFooterCol']")
#element3.click()


##FINDELEMENTS
#Locator matching with single element
# element1 = driver.find_elements(By.XPATH,"//input[@id = 'twotabsearchtextbox']")
# time.sleep(3)
# print(len(element1))
# driver.quit()

#Locator matching with multiple elements
# element2 = driver.find_elements(By.XPATH,"//div[@class = 'navFooterColHead']")
# print(len(element2))
#driver.quit()

#Element not available - then it will give count 0
element3 = driver.find_elements(By.XPATH,"//div[@class = 'navFooterCol']")
print(len(element3))