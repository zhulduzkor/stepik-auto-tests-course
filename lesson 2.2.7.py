from selenium import webdriver
import time
import os 

    
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_css_selector('[name="firstname"]')             
    input1.send_keys("+")

    input2 = browser.find_element_by_css_selector('[name="lastname"]')             
    input2.send_keys("+") 
    
    input3 = browser.find_element_by_css_selector('[name="email"]')             
    input3.send_keys("+") 
        
    input4 = browser.find_element_by_css_selector('[name="file"]')    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)
    
    button = browser.find_element_by_css_selector(".btn")
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()