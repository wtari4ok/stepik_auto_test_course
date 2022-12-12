from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


URL = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))


driver = webdriver.Chrome()
driver.get(URL)
link = driver.find_element(By.LINK_TEXT, link_text)
link.click()
first_name = driver.find_element(By.NAME, "first_name")
first_name.send_keys("Tema")
last_name = driver.find_element(By.NAME, "last_name")
last_name.send_keys("Horkov")
city = driver.find_element(By.CSS_SELECTOR, ".form-control.city")
city.send_keys("Saint-P")
country = driver.find_element(By.ID, "country")
country.send_keys("Russia")
submit_button = driver.find_element(By.TAG_NAME, "button")
submit_button.click()
time.sleep(5)
driver.quit()
