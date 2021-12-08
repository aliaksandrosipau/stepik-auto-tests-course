from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import os
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome(executable_path='/Users/mac/tms-automated-course/osipau_aliaksandr/chromedriver')
browser.get(link)

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_xpath('//button[@id="book"]')
button.click()
x_text = browser.find_element_by_xpath('//span[@id="input_value"]')
x_text2 = x_text.text
x = int(x_text2)
y = calc(x)

input_field = browser.find_element_by_xpath('//input[@id="answer"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", input_field)
input_field.send_keys(y)
button2 = browser.find_element_by_id("solve")
button2.click()
time.sleep(10)

# first_window = browser.window_handles[0]
# second_window = browser.window_handles[1]
#
# browser.switch_to.window(second_window)