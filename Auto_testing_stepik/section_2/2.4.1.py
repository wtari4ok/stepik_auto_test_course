from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get(link)

    button = browser.find_element(By.ID, "verify")
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text