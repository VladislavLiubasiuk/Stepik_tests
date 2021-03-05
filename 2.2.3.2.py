import os, time
from math import log, sin
from selenium import webdriver

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(log(abs(12*sin(x))))
    
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element_by_class_name("trollface.btn.btn-primary")
    input1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    result = calc(int(x))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(result))
    
    final = browser.find_element_by_class_name("btn.btn-primary")
    final.click()
    
finally:
    time.sleep(7)
    browser.quit()