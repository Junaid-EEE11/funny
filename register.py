def generate_user_name():
    return ''.join(random.choices(string.ascii_letters, k=8))+'@gmail.com'
def generate_phone_number():
    return '1' + ''.join(random.choices(string.digits, k=9))
def generate_password():
    return 'T0@_' + ''.join(random.choices(string.digits, k=9))
def set_payemnt_password():
    number_inputs = driver.find_elements(By.CSS_SELECTOR, 'div');
    phone_number_input=[str(i.text=="Set payment password") for i in number_inputs]
    number_input[phone_number_input.index('True')].click()
    phone_number=driver.find_elements(By.CSS_SELECTOR, 'div.van-key')
    [phone_number[i].click() for i in random.choice(range(0,10), k=6)]

def fill_form(url):
    options =Options()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Please enter the user name"]')
    phone_number_input.send_keys(generate_user_name())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Please enter the phone number"]')
    phone_number_input.send_keys(generate_phone_number())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Enter password"]')
    phone_number_input.send_keys(generate_password())
    phone_number_input = driver.find_element(By.CSS_SELECTOR, 'div.phone input[placeholder="Set 6 digit payment password"]')
    phone_number_input.click();
    set_payemnt_password()
    send_button = driver.find_element(By.CSS_SELECTOR, 'div.Register Now')
    send_button.click()
    time.sleep(5)
    driver.quit()
