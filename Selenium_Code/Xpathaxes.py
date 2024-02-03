import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/gainers")
driver.maximize_window()
#text_name=driver.find_element(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/self::*').text   #self
#print(text_name)

#child
#childs = driver.find_elements(By.XPATH,'//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/child::*')
#print(len(childs))

#parent
#parent = driver.find_element(By.XPATH,'//*[contains(text(),"Texmaco Infrastructu")]/parent::*').text
#print(parent)

#ancestor
#ancstr = driver.find_element(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr').text
#print(ancstr)

#descendent
#desc = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/descendant::*')
#print(len(desc))

#precedent
#prec = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/preceding::*')
#print(len(prec))
#prec1 = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/preceding::*')
#print(len(prec1))

#following
#following = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/following::*')
#print(len(following))
#following1 = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/following::*')
#print(len(following1))

#following sibling
following_siblings = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/following-sibling::*')
print(len(following_siblings))

#preseding siblings
preceding_siblings = driver.find_elements(By.XPATH, '//*[contains(text(),"Texmaco Infrastructu")]/ancestor::tr/preceding-sibling::*')
print(len(preceding_siblings))
time.sleep(3)

