from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage:
    def __init__(self, driver):
        self.driver = driver

class NestedFramesPage(BasePage):
    URL = 'https://the-internet.herokuapp.com/nested_frames'

    def open(self):
        self.driver.get(self.URL)

    def find_main_frame(self):
        frames = self.driver.find_elements(By.TAG_NAME, 'frame')
        frames_with_name = [frame for frame in frames if frame.get_attribute('name')]

        for frame in frames_with_name:
            frame_title = frame.get_attribute('name')
            if frame_title == "frame-top":
                self.top_frame = frame
            if frame_title == "frame-bottom":
                self.bottom_frame = frame    

    def get_top_frame_texts(self):
        self.driver.switch_to.frame(self.top_frame)
        topFrameChildren = self.driver.find_elements(By.TAG_NAME ,'frame')
        topFrameWithNames = [frame for frame in topFrameChildren if frame.get_attribute('name')]

        text_list_from_frame = []

        for frame in topFrameWithNames:
            self.driver.switch_to.frame(frame)
            frameBody = self.driver.find_element(By.TAG_NAME ,'body')
            text_list_from_frame.append(frameBody.text)
            self.driver.switch_to.default_content()
            self.driver.switch_to.frame(self.top_frame)       
        return text_list_from_frame
    
    def get_bottom_frame_text(self):
        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.bottom_frame)
        bottomFrameBody = self.driver.find_element(By.TAG_NAME ,'body')
        return bottomFrameBody.text