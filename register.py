from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox()
driver.get('https://shop077.com/register?invite_code=fa49ec')
def generate_phone_number1():
    #return ''.join(random.choices(string.ascii_letters, k=8))+'@gmail.com'
def generate_phone_number2():
    #return '1' + ''.join(random.choices(string.digits, k=9))
def generate_phone_number3():
    #return 'T0@_' + ''.join(random.choices(string.digits, k=9))
def generate_phone_number4():
    #return '1' + ''.join(random.choices(string.digits, k=5))
def fill_form(url, number):
    options =Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Please enter the user name"]')
    phone_number_input.send_keys(generate_phone_number1())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Please enter the phone number"]')
    phone_number_input.send_keys(generate_phone_number2())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Enter password"]')
    phone_number_input.send_keys(generate_phone_number3())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Set 6 digit payment password"]')
    phone_number_input.send_keys(generate_phone_number4())
    send_button = driver.find_element(By.CSS_SELECTOR, 'div.Register Now')
    send_button.click()
    time.sleep(5)  # Wait for the action to complete (adjust as needed)
    driver.quit()
