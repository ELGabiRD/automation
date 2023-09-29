from selenium import webdriver
import os
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Chromedriver"

driver = webdriver.Chrome()

# Open a webpage

url = 'https://the-internet.herokuapp.com/nested_frames'

driver.get(url)


principalFrames = driver.find_elements(By.TAG_NAME ,'frame')

framesWithName = [frame for frame in principalFrames if frame.get_attribute('name')] 

topFrame = framesWithName[0]
bottomFrame = framesWithName[0]

for frame in framesWithName:

    frameTitle = frame.get_attribute('name')

    if frameTitle == "frame-top":
        topFrame = frame

    if frameTitle == "frame-bottom":
        bottomFrame = frame

driver.switch_to.frame(topFrame)

topFrameChildren = driver.find_elements(By.TAG_NAME ,'frame')

topFrameWithNames = [frame for frame in topFrameChildren if frame.get_attribute('name')]

for frame in topFrameWithNames:
    driver.switch_to.frame(frame)
    frameBody = driver.find_element(By.TAG_NAME ,'body')
    print(frameBody.text)
    driver.switch_to.default_content()
    driver.switch_to.frame(topFrame)

driver.switch_to.default_content()
driver.switch_to.frame(bottomFrame)
bottomFrameBody = driver.find_element(By.TAG_NAME ,'body')
print(bottomFrameBody.text)