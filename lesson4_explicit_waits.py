from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time
import math

def calc(x:int):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.maximize_window()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
     # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price =  WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
   
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(int(x))
    
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    submit = browser.find_element(By.ID, "solve")
    submit.click()
    
    # message = browser.find_element(By.ID, "verify_message")
    
    # assert "successful" in message.text
    




except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()

