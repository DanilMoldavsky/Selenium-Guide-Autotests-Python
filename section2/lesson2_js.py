from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    
    
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    robo_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robo_checkbox.click()
    
    robots_rule = browser.find_element(By.ID, 'robotsRule')
    robots_rule.click()
    
    
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


except Exception as e:
    print(e)
# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
finally:
    time.sleep(3)
    browser.quit()
