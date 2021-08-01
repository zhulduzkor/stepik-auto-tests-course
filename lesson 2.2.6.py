from selenium import webdriver
import math
import time

    
link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
            
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    
    browser.execute_script("window.scrollBy(0, 110);")
    
    checkbox_1 = browser.find_element_by_id("robotCheckbox")
    checkbox_1.click()

    radiobutton_1 = browser.find_element_by_id("robotsRule")
    radiobutton_1.click()

    button_1 = browser.find_element_by_class_name("btn.btn-primary")
    button_1.click()
      
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()