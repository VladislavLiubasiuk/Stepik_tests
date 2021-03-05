from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_value = browser.find_element_by_id("treasure")
    xval = x_value.get_attribute("valuex")

    result = calc(xval)
    input1 = browser.find_element_by_id("answer")
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