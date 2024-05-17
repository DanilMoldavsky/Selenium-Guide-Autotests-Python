from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def main():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # input1 = browser.find_element(By.TAG_NAME, 'label')
        # input1.send_keys("Ivan")
        first_name = browser.find_element(By.NAME, "first_name")
        first_name.send_keys("Ivan")
        last_name = browser.find_element(By.NAME, "last_name")
        last_name.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.ID, "submit_button")
        button.click()
        print("Всё прошло успешно!")
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(20)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    main()

# не забываем оставить пустую строку в конце файла