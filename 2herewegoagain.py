from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"

def calc(x):
    return str(ln(abs(12*sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    result = calc(x)
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(result)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    
    final = browser.find_element_by_class_name("btn.btn-default")
    final.click()
finally:
    time.sleep(10)
    browser.quit()