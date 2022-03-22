from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME,"firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME,"lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME,"email")
    input3.send_keys("petrov@gmail.com")

    file = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
