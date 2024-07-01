import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/")
driver.maximize_window()
time.sleep(3)

#driver.save_screenshot(os.getcwd()+"\\homepagesn.png")
driver.get_screenshot_as_file("C:\\Users\\91766\\OneDrive\\Documents\\samplescreenshot.png")