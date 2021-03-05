from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin

def calc(x):
    return str(log(abs(12*sin(x))))
    
try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = browser.find_element_by_id("book")
    button.click()

    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    result = calc(int(x))
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(result))
    
    final = browser.find_element_by_id("solve")
    final.click()

finally:
    time.sleep(10)
    browser.quit()