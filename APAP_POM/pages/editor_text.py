from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
class TinyMCEPage(BasePage):
    URL = 'https://the-internet.herokuapp.com/tinymce'

    
    def open(self):
        self.driver.get(self.URL)

    def switch_to_text_frame(self):
        self.driver.switch_to.default_content()
        text_box = self.driver.find_element(By.ID, "mce_0_ifr")
        self.driver.switch_to.frame(text_box)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def set_text(self, text):
        self.switch_to_text_frame()
        type_text = self.driver.find_element(By.ID, "tinymce")
        time.sleep(3)
        type_text.clear()
        type_text.send_keys(text)

    def get_text(self):
        type_text = self.driver.find_element(By.ID, "tinymce")
        return type_text.text

    def apply_format_bold(self):
        self.select_all_text()
        self.switch_to_default_content()
        btn_bold = self.driver.find_element(By.CSS_SELECTOR, 'button[title="Bold"]')
        btn_bold.click()

    def apply_format_center(self):
        self.switch_to_default_content()
        btn_center = self.driver.find_element(By.CSS_SELECTOR, 'button[title="Align center"]')
        btn_center.click()

    def apply_format_color(self, color_name):
        self.switch_to_default_content()
        btn_format = self.driver.find_element(By.CSS_SELECTOR, 'button[title="Format"]')
        btn_format.click()

        target_text = f'{color_name}'
        xpath_expression = f"//*[@title='{target_text}']"
        lbl_color = self.driver.find_element(By.XPATH, xpath_expression)
        lbl_color.click()

    def select_color(self, color_name):
        self.switch_to_default_content()
        target_text = f'{color_name}'
        xpath_expression = f"//*[@title='{target_text}']"
        color_box = self.driver.find_element(By.XPATH, xpath_expression)
        color_box.click()

    def double_click_text(self):
        self.switch_to_text_frame()
        type_text = self.driver.find_element(By.ID, "tinymce")
        self.actions.double_click(type_text).perform()
    
    def select_all_text(self):
        self.switch_to_text_frame()
        type_text = self.driver.find_element(By.ID, "tinymce")
        time.sleep(2)
        self.actions.double_click(type_text).pause(0.1)
        self.actions.double_click(type_text).pause(0.1)
        self.actions.double_click(type_text).perform()

    def select_all_text_private(self, type_text):
        self.actions.double_click(type_text).pause(0.1)
        self.actions.double_click(type_text).pause(0.1)
        self.actions.double_click(type_text).perform()

class HomePage(BasePage):
    pass
