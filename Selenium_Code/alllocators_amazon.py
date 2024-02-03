import  time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH, '//a[@data-csa-c-type = "link" and @data-csa-c-content-id ="nav_avod_desktop_topnav" ]').click()
driver.find_element(By.XPATH, "//span[normalize-space()='Movies']").click()
time.sleep(3)
driver.find_element(By.XPATH, '//span[@data-testid ="appnavbar_menuitem_comedy"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//img[contains(@data-testid,"appnavbar_menuitem_mshopicon")]').click()
time.sleep(5)
driver.quit()