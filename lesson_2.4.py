# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/cats.html")
# button = browser.find_element(By.ID, "button")
# button.click()

from selenium import webdriver
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    element = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book")
    button.click()
    x = browser.find_element(By.ID, "input_value").text
    result = calc(x)
    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(result)
    button_2 = browser.find_element(By.XPATH, "//button[@type='submit']")
    button_2.click()
finally:
    time.sleep(10)
    browser.quit()