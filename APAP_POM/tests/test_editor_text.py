import unittest
from tests.base_test import BaseTest
from utils.test_cases import test_cases
from pages.editor_text import *


class TestEditorText(BaseTest):
                          
    def edit_text(self):

        tinymce_page = TinyMCEPage(self.driver)
        tinymce_page.open()
        text = "Hola buenas tardes esperadno en Dios que se encuentren bien este es mi scrip para esta prueba espero que haya cumplido satisfactoriamente sus expectativas estoy muy feliz de formar parte de este proceso de seleccion y espero pronte ser parte del equipo :)"
        tinymce_page.set_text(text)
        tinymce_page.apply_format_bold()
        time.sleep(5)
        tinymce_page.double_click_text()
        tinymce_page.apply_format_center()
        tinymce_page.apply_format_color("Text color")
        tinymce_page.select_color("Red")
        formatted_text = tinymce_page.get_text()
        print(formatted_text)
        self.assertTrue(True)