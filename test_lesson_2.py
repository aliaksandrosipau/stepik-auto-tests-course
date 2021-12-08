from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome(executable_path='/Users/mac/tms-automated-course/osipau_aliaksandr/chromedriver')
browser.get(link)

x_text = browser.find_element_by_xpath('//span[@id="input_value"]')
x_text2 = x_text.text
x = int(x_text2)

y = calc(x)

input_field = browser.find_element_by_xpath('//input[@id="answer"]')
input_field.send_keys(y)

checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
checkbox.click()

radio = browser.find_element_by_css_selector('[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
radio.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()