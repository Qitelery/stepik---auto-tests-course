import pytest
import time
import math
from selenium import webdriver

testdata = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize("part_link", testdata)
def test_parts_of_word(browser, part_link):       
    link = f"{part_link}"
    browser.implicitly_wait(5)
    browser.get(link)
    answer = str(math.log(int(time.time())))
    inp = browser.find_element_by_class_name("textarea.string-quiz__textarea.ember-text-area.ember-view")
    inp.send_keys(answer)

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()
    massage = browser.find_element_by_css_selector("pre.smart-hints__hint")
    massage_text = massage.text

    assert "Correct!" in massage_text

    
    
