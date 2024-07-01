import time

from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(text(),'Buy Ticket')]").click()
driver.find_element(By.XPATH, "//input[@id='dob']").click()

months = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select month']"))
months.select_by_visible_text("Dec")
years = Select(driver.find_element(By.XPATH, "//select[@aria-label='Select year']"))
years.select_by_value("2010")

alldates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in alldates:
    if date.text == "16":
        date.click()
        break

time.sleep(7)
