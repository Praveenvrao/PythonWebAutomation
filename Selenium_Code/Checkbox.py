import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1 Selecting oneday
# sunday = driver.find_element(By.XPATH, "//input[@type='checkbox' and contains(@id, 'sunday')]")
# sunday.click()
# driver.implicitly_wait(5)
# print(sunday.get_attribute("id"))

#2 selecting all days at a time
alldays = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(alldays))
#driver.quit()

#Approach1 selecting all days at a time
# for i in range(len(alldays)):
#     alldays[i].click()
# time.sleep(5)

# #Approach2 selecting all days at a time
# for checkboxes in alldays:
#     checkboxes.click()
# time.sleep(4)

#4 Selecting specific days from the week

# for checkboxes in alldays:
#     week = checkboxes.get_attribute('id')
#     if week == 'sunday' or week == 'monday' or week == 'tuesday':
#         checkboxes.click()
# time.sleep(4)

#5 selecting last 3 days in week
#
# for i in range(len(alldays)-3, len(alldays)):
#     alldays[i].click()
#     time.sleep(4)

#6 selecting first 3 days in week

# for i in range(len(alldays)):
#     if i<=2:
#         alldays[i].click()
# time.sleep(4)

#7 clearing all boxes and checking all

for checkboxes in alldays:
    checkboxes.click()
time.sleep(4)
for checkboxes in alldays:
    if checkboxes.is_selected():
        checkboxes.click()
time.sleep(4)

