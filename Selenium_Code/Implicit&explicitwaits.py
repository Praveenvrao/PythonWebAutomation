import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://demo.nopcommerce.com/register?")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element(By.XPATH, "//a[@class='ico-login']").click()

driver = webdriver.Chrome()

# waitdec = WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions="Exception")  #explicit wait declaration
# driver.get("https://demo.nopcommerce.com/register?")
# driver.maximize_window()
# login_element = waitdec.until(EC.presence_of_element_located((By.XPATH, "//a[@class='ico-login']")))
# login_element.click()
# print(login_element.text)

waitdoc1 = WebDriverWait(driver,10,poll_frequency=2, ignored_exceptions='Exception')
driver.get("https://www.youtube.com/")
driver.maximize_window()
shorts = waitdoc1.until(EC.presence_of_element_located((By.XPATH, "//a[@id='endpoint' and @title ='Shorts' and @tabindex ='-1']")))
shorts.click()
print(shorts.text)
