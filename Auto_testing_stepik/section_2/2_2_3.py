import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text

    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    total = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(total))

    s_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    s_button.click()

    time.sleep(30)

