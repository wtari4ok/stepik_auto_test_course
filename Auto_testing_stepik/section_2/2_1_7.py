import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    num = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(num)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robot_cbox = browser.find_element(By.ID, "robotCheckbox")
    robot_cbox.click()

    robot_rbutton = browser.find_element(By.ID, "robotsRule")
    robot_rbutton.click()

    button.click()

    time.sleep(10)
