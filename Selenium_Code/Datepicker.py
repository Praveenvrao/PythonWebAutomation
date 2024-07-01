import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[normalize-space()='Datepicker']").click()
driver.switch_to.frame(0)
# driver.find_element(By.XPATH, '//*[@id="datepicker"]').send_keys("11/24/2024")
# time.sleep(5)

month = "March"
date = "12"
year = "2025"

driver.find_element(By.XPATH, '//*[@id="datepicker"]').click()

while True:
    mon = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    yr = driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/div/span[2]').text

    if mon == month and yr == year:
        break;
    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]/span').click()

correctdate = driver.find_elements(By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')

for ele in correctdate:
    if ele.text == date:
        ele.click()
        break

time.sleep(10)
