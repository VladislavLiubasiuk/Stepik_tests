import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("test1")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("test2")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test3")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
finally:
    time.sleep(10)
    browser.quit()