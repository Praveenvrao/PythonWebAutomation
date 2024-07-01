import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()
inputbox1 = driver.find_element(By.XPATH, "//textarea[@id = 'inputText1']")
inputbox2 = driver.find_element(By.XPATH, "//textarea[@id = 'inputText2']")
inputbox1.send_keys("Welcome to Python selenium")

Keyboardact = ActionChains(driver)

Keyboardact.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
Keyboardact.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
Keyboardact.send_keys(Keys.TAB).perform()
Keyboardact.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)