import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").click()
driver.find_element(By.XPATH, '//*[@id="select2-billing_country-container"]').click()
time.sleep(1)
countrieslist = driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']//li")
print(len(countrieslist))

for country in countrieslist:
    if country.text == "Iceland":
        country.click()
        break

time.sleep(10)