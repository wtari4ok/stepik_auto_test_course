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

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    input1.send_keys("firstname")

    input2 = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input2.send_keys("lastname")

    input3 = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input3.send_keys("email")

    load_file = browser.find_element(By.CSS_SELECTOR, "input#file")
    load_file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    time.sleep(20)
