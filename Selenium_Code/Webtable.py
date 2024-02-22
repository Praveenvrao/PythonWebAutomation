import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#1 Count number of rows and colomns

no_rows = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr"))
print(no_rows)
no_clms = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr[1]/th"))
print(no_clms)

#2 Read specific row & colomn data

data1 = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr[6]/td[1]").text
data2 = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr[4]/td[3]").text
print(data1, "-----", data2)

# 3 Read all the rows and coloms data

for r in range(2, no_rows+1):
    for c in range(1, no_clms+1):
        totaldata = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(totaldata,end="             ")
    print('')