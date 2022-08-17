from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=./User_Data')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get('https://web.whatsapp.com/')

time.sleep(30)

contacts = ['Rocardio']
message = 'Eu sou Rocardio, eu vou realizar todas as suas fantasias: pagar suas contas, coçar suas costas, encher o tanque e calibrar os pneus.. hoje eu tô pro crime. #truecrime'


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
