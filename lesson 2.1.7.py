from selenium import webdriver
import math
import time

    
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox_1 = browser.find_element_by_id("robotCheckbox")
    checkbox_1.click()

    radiobutton_1 = browser.find_element_by_id("robotsRule")
    radiobutton_1.click()

    button_1 = browser.find_element_by_class_name("btn.btn-default")
    button_1.click()
   
   
finally:
    print(x)
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    