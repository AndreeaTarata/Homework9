import time

from selenium import webdriver
from selenium.webdriver.common.by import By

user = (By.ID, 'username')
pwd = (By.ID, 'password')
Button = (By.CLASS_NAME, 'radius')
text = (By.CLASS_NAME, 'subheader')

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

assert driver.find_element(*text).text == 'This is where you can log into the secure area. ' \
                                          'Enter tomsmith for the username and SuperSecretPassword! for the password. ' \
                                          'If the information is wrong you should see error messages.'

driver.find_element(*user).send_keys('Andreea')
driver.find_element(*pwd).send_keys('tot')
driver.find_element(*Button).click()
driver.implicitly_wait(3)
time.sleep(5)

driver.find_element(*user).send_keys('tomsmith')
driver.find_element(*pwd).send_keys('SuperSecretPassword!')
driver.find_element(*Button).click()
driver.implicitly_wait(3)
time.sleep(5)

# TODO sa integram explicit wait pt butonul de login
# TODO sa incercam sa luam dinamic userul si parola din acel text field (adica sa introducem textul intr-un string si sa extragem sin el
# TODO sa verificam si acele mesaje de sucesfull login sau not
# TODO un test de logout si intradevar ne-am logat cu succes

