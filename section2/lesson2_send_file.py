from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    # element.send_keys(file_path)
    
    forms = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for form in forms:
        form.send_keys("Мой ответ")
    
    file_form = browser.find_element(By.ID, "file")
    
    file_form.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


except Exception as e:
    print(e)
finally:
    time.sleep(5)
    browser.quit()
