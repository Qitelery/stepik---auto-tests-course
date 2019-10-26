from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
buttonBook = browser.find_element_by_id("book")
buttonBook.click()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(int(x))

inp = browser.find_element_by_id("answer")
inp.send_keys(y)

button = browser.find_element_by_id("solve")
button.click()

browser.quit()
