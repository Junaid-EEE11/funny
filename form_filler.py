from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
driver.get('https://shop077.com/forgetPassword')

def generate_phone_number():
    return '1' + ''.join(random.choices(string.digits, k=9));

def fill_form(url, number):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Phone number"]')
    phone_number_input.send_keys(generate_phone_number())
    send_button = driver.find_element(By.CSS_SELECTOR, 'div.payment button')
    send_button.click()
    time.sleep(60)
    driver.quit()
