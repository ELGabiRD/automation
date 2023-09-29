from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\Chromedriver"
driver = webdriver.Chrome()

# Open a webpage
url = 'https://the-internet.herokuapp.com/windows'
driver.get(url)

hyperlinkTag = driver.find_elements(By.TAG_NAME ,'a')

# Find element by its text using XPath
targetText = 'Click Here'
xpathExpression = f"//*[contains(text(), '{targetText}')]"
anchorElement = driver.find_element(By.XPATH, xpathExpression)
anchorElement.click()

driver.switch_to.window(driver.window_handles[0])

time.sleep(2)
driver.close()

driver.switch_to.window(driver.window_handles[0])
textElement = driver.find_element(By.TAG_NAME, 'h3')

print(textElement.text)

time.sleep(3)