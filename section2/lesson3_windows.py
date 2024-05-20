from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    link = "https://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)
    alert.accept()
    
    x = browser.find_element(By.ID, "input_value")
    y = calc(int(x.text))
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    
    btn = browser.find_element(By.TAG_NAME, "button")
    btn.click()
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()


except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()
