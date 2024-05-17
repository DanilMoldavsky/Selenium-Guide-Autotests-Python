from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



def main():
    link = "http://suninjuly.github.io/find_link_text"
    decode:str = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(decode)
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        link = browser.find_element(By.PARTIAL_LINK_TEXT, decode)
        link.click()
        
        first_name = browser.find_element(By.NAME, "first_name")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.NAME, "last_name")
        last_name.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
        button.click()
        print("Всё прошло успешно!")
        
    finally:
        time.sleep(20)
        browser.quit()

if __name__ == "__main__":
    main()
