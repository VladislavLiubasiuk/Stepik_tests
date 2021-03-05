from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_not = browser.find_element_by_id("num1")
    x = x_not.text
    y_not = browser.find_element_by_id("num2")
    y = y_not.text
    result = int(x) + int(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(result))
    
    final = browser.find_element_by_class_name("btn.btn-default")
    final.click()
finally:
    time.sleep(5)
    browser.quit()