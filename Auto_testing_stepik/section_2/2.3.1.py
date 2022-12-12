from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/alert_accept.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    num = calc(x)
    input_x = browser.find_element(By.ID, "answer")
    input_x.send_keys(num)

    button2 = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button2.click()

    time.sleep(20)
