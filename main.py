from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contacts = ['Rocardio', 'Jardel Frank']
message = 'Hello World!'


def search_contact(contact):
    input_search = driver.find_element("xpath", '//div[contains(@class, "selectable-text")]')
    time.sleep(3)
    input_search.click()
    input_search.send_keys(contact)
    input_search.send_keys(Keys.ENTER)


def send_message(message):
    input_message = driver.find_element("xpath", f"//div[@title='Mensagem']")
    input_message.click()
    time.sleep(3)
    input_message.send_keys(message)
    input_message.send_keys(Keys.ENTER)


for contact in contacts:
    search_contact(contact)
    send_message(message)
