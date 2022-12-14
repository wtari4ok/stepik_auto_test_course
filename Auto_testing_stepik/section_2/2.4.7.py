import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.implicitly_wait(15)

browser.get(link)

WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

book_button = browser.find_element(By.ID, "book")
book_button.click()

x = browser.find_element(By.ID, "input_value").text
x = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(x)

submit_button = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

time.sleep(15)



