from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    y = int(num1) + int(num2)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    

finally:
    time.sleep(10)
    browser.quit()
