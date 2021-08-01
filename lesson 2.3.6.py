from selenium import webdriver
import time
import math

    
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    button = browser.find_element_by_class_name("trollface.btn.btn-primary")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
        
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
       
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()