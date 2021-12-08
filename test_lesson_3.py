from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome(executable_path='/Users/mac/tms-automated-course/osipau_aliaksandr/chromedriver')
browser.get(link)

fn = browser.find_element_by_css_selector('[name="firstname"]')
fn.send_keys('Mr')
ln = browser.find_element_by_css_selector('[name="lastname"]')
ln.send_keys('Li')
email = browser.find_element_by_css_selector('[name="email"]')
email.send_keys('email')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')

addfilebtn = browser.find_element_by_css_selector('[name="file"]')
addfilebtn.send_keys(file_path)
button = browser.find_element_by_tag_name("button")
button.click()
time.sleep(10)

