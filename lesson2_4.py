# Задание: ждем нужный текст на странице

# Сценарий:
# 1)Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2)Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3)Нажать на кнопку "Book"
# 4)Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение



from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    var_x = browser.find_element_by_css_selector('[id="input_value"]').text
    value = calc(var_x)

    input_1 = browser.find_element_by_css_selector('[id="answer"]')
    input_1.send_keys(value)

    button_2 = browser.find_element_by_css_selector("[id='solve']")
    button_2.click()
    

    time.sleep(1)

finally:
    time.sleep(5)
    browser.quit()
