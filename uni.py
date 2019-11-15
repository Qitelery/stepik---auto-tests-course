from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestScenario(unittest.TestCase):
    def test_scen1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("input.form-control.first")
        input1.send_keys("Alexey")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Dronov")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("x")
        
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(3)
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
    def test_scen2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector("input.form-control.first")
        input1.send_keys("Alexey")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
        input2.send_keys("Dronov")
        input3 = browser.find_element_by_css_selector("input.form-control.third")
        input3.send_keys("x")
                
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        
        time.sleep(3)
        
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        
        welcome_text = welcome_text_elt.text
        
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
    unittest.main()
