from selenium.webdriver.common.by import By

class TheInternet:
    def _init_(self, driver):
        self.driver = driver

class MainPage(TheInternet):
    URL = 'https://the-internet.herokuapp.com/windows'

    def open(self):
        self.driver.get(self.URL)

    def click_link(self, target_text):
        xpath_expression = f"//*[contains(text(), '{target_text}')]"
        anchor_element = self.driver.find_element(By.XPATH, xpath_expression)
        anchor_element.click()

    def get_text(self):
        return self.driver.find_element(By.TAG_NAME, 'h3').text

class HomePage(TheInternet):
    pass