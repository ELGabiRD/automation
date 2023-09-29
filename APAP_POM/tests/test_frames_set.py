import unittest
from selenium import webdriver
import os
from pages.frames_set import *
from tests.base_test import BaseTest
from utils.test_cases import test_cases
import os
from selenium import webdriver

class TestRunFramesText(BaseTest):

    def print_frames_text(self):  
        
        nested_frames_page = NestedFramesPage(self.driver)
        nested_frames_page.open()
        nested_frames_page.find_main_frame()
        texts = nested_frames_page.get_top_frame_texts()

        for text in texts:
            print(text)

        bottom_frame_text = nested_frames_page.get_bottom_frame_text()
        print(bottom_frame_text)
        self.assertTrue(True)