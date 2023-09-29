from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

os.environ['PATH'] += r"C:\Chromedriver"
driver = webdriver.Chrome()

# Open a webpage
url = 'https://the-internet.herokuapp.com/tinymce'
driver.get(url)
button_elements = driver.find_elements(By.TAG_NAME ,'button')

buttons_with_title = [button for button in button_elements if button.get_attribute('title')]
buttons_without_title = [button for button in button_elements if button.get_attribute('title') == False]

target_text3 = 'Format'
xpath_expression3 = f"//*[contains(text(), '{target_text3}')]"
btn_format = driver.find_element(By.XPATH, xpath_expression3)

for button in buttons_without_title:
    span = button.find_element(By.TAG_NAME, 'span')
    button_title = button.get_attribute('title')

btn_bold = buttons_with_title[0]
btn_center = buttons_with_title[0]
formatsButton = buttons_with_title[0]
for button in buttons_with_title:
    button_title = button.get_attribute('title')
    if button_title == "Bold":
       btn_bold = button
    if button_title == "Align center":
        btn_center = button
    if button_title == "Format":
        formatsButton = button

Text_box = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(Text_box)
type_text = driver.find_element(By.ID, "tinymce")
time.sleep(1)
type_text.clear()
driver.switch_to.default_content()
btn_bold.click()
driver.switch_to.frame(Text_box)
texto = "Hola buenas tardes esperadno en Dios que se encuentren bien este es mi scrip para esta prueba espero que haya cumplido satisfactoriamente sus expectativas estoy muy feliz de formar parte de este proceso de seleccion y espero pronte ser parte del equipo :)"
type_text.send_keys(texto)
Capturar_texto = type_text

action = ActionChains(driver)
time.sleep(2)
action.double_click(type_text).pause(0.1)
action.double_click(type_text).pause(0.1)
action.double_click(type_text).perform()


driver.switch_to.default_content()
btn_center.click()
btn_format.click()

target_text2 = 'Text color' 
xpath_expression2 = f"//*[@title='{target_text2}']" 
lbl_color = driver.find_element(By.XPATH, xpath_expression2)
lbl_color.click()

target_text = 'Red' 
xpath_expression = f"//*[@title='{target_text}']" 
redBox = driver.find_element(By.XPATH, xpath_expression) 
redBox.click()
driver.switch_to.frame(Text_box)
action = ActionChains(driver)
action.click(type_text).perform()
print(texto)
time.sleep(3)