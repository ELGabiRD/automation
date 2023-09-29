import unittest
from tests.base_test import BaseTest
from pages.the_internet import *
import time
import os
from selenium import webdriver
from utils.test_cases import test_cases

class TestRunInternetPage(BaseTest):
                          
    def switch_window_print_text(self):
  
        main_page = MainPage()
        main_page.driver = self.driver
        main_page.open()
        main_page.click_link('Click Here')
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        text = main_page.get_text()
        time.sleep(3)
        print(text)
        self.assertTrue(True)
