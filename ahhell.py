from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from math import log, sin

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(log(abs(12*sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    result = calc(int(x))
    input1 = browser.find_element_by_class_name("form-control")
    input1.send_keys(str(result))
    
    final = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", final)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
       
    final.click()
    
finally:
    time.sleep(5)
    browser.quit()