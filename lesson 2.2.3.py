from selenium import webdriver
import math
import time
from selenium.webdriver.support.ui import Select


 
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    answer = str(int(x)+int(y))
    
    browser.find_element_by_tag_name("select").click()
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(answer)
        
    button_1 = browser.find_element_by_class_name("btn.btn-default")
    button_1.click()
          
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()