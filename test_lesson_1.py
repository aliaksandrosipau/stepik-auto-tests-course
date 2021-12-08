from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path='/Users/mac/tms-automated-course/osipau_aliaksandr/chromedriver')
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    fn = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
    fn.send_keys("Ivan")
    sn = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    sn.send_keys("Petrov")
    email = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    email.send_keys("email@email.email")

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath('//button[@type="submit"]')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


