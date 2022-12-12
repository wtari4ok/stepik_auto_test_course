from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "https://SunInJuly.github.io/execute_script.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")

browser.execute_script("return arguments[0].scrollIntoView(true);", button)

browser.switch_to.window(window_name)
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]


button.click()

