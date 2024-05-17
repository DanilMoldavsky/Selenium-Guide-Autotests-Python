from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    
    
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    
    robo_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robo_checkbox.click()
    
    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()
