import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.find_element(By.XPATH, "//input[@class ='wikipedia-search-input']").send_keys("selenium")
# search = driver.find_element(By.XPATH, "//input[@class ='wikipedia-search-button']")
# print(search.get_attribute("class"))
# search.click()
# #searchresults = driver.find_elements(By.XPATH, "//div[@id ='wikipedia-search-result-link']/a[@target = '_blank']")
# selenium_b = driver.find_element(By.LINK_TEXT, "Selenium in biology")
# print(selenium_b)
#
# for result in searchresults:
#     print(result.text)

driver.find_element(By.XPATH, "//a[normalize-space()='merrymoonmary']").click()
print(driver.current_window_handle.title())

windowids = driver.window_handles
print(windowids)
parentwindow = windowids[0]
childwindow = windowids[1]

driver.switch_to.window(parentwindow)
driver.find_element(By.XPATH, "//a[normalize-space()='Blogger']").click()
m_wids = driver.window_handles
print(m_wids)
print(m_wids[0].title())
print(m_wids[1].title())
print(m_wids[2].title())

for ids in m_wids:
    driver.switch_to.window(ids)
    print(driver.title)
    if driver.title == "merrymoonmary Stock Image and Video Portfolio - iStock" or driver.title == "Blogger.com - Create a unique and beautiful blog easily.":
        driver.close()


time.sleep(200)