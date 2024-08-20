import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config import config
import time
import math


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',#])
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
class TestTaskParametrize:
    
    POP_UP_LOGIN = (By.CSS_SELECTOR, ".light-tabs")
    ENTER_BUTTON = (By.CSS_SELECTOR, "#ember459")
    TEXT_AREA = (By.CSS_SELECTOR, "textarea")
    OPTIONAL_FEEDBACK = (By.CSS_SELECTOR, ".smart-hints__hint")
    
    def test_to_learn_parametrize(self, browser: webdriver.Chrome, link):
        wait =  WebDriverWait(browser, 10)

        browser.get(link)
        enter = wait.until(EC.element_to_be_clickable(self.ENTER_BUTTON))
        enter.click()
        email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        email.send_keys(config.LOGIN_STEPIK)
        password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        password.send_keys(config.PASS_STEPIK)
        browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        wait.until_not(EC.presence_of_element_located(self.POP_UP_LOGIN))
        text_area = wait.until(EC.presence_of_element_located(self.TEXT_AREA), 'текст ареа')
        again = browser.find_elements(By.CSS_SELECTOR, '.again-btn')
        if len(again) > 0:
            again[0].click()
            text_area = wait.until(EC.element_to_be_clickable(self.TEXT_AREA), 'текст ареа')
        text_area.clear()
        answer = math.log(int(time.time()))
        text_area.send_keys(str(answer))
        browser.find_element(By.CSS_SELECTOR, 'button.submit-submission').click()
        result = wait.until(EC.presence_of_element_located(self.OPTIONAL_FEEDBACK))
        # result = wait.until(EC.presence_of_element_located(self.OPTIONAL_FEEDBACK))
        assert "Correct!" == result.text