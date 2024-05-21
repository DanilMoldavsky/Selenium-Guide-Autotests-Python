from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.maximize_window()
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)
    
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    




except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()

