from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    num = calc(x)
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(num)

    button2 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button2.click()

    time.sleep(20)
