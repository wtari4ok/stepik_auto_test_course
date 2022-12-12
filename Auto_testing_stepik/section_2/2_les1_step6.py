import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    c_button = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    c_button.click()

    r_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    r_button.click()

    s_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    s_button.click()

    time.sleep(30)

