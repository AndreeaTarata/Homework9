
import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogIn(unittest.TestCase):
    user = (By.ID, 'username')
    password = (By.ID, 'password')
    loginbtn = (By.CLASS_NAME, 'radius')
    textul = (By.XPATH, '//h2')
    actual = 'https://the-internet.herokuapp.com/login'
    meseroare = (By.ID, 'flash-messages')
    xbtn = (By.CLASS_NAME, 'close')
    label_username = (By.XPATH, '//*[@id="login"]/div[1]/div/label')
    label_psd = (By.XPATH, '//*[@id="login"]/div[2]/div/label')
    logoutbtn = (By.CLASS_NAME, 'icon-2x icon-signout')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.maximize_window()

    def test_valid_login(self):
        # self.assertEqual(self.driver.get())
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.implicitly_wait(3)
        time.sleep(5)
        # test1
        noul_url = self.driver.current_url
        expected_url = "https://the-internet.herokuapp.com/secure"
        self.assertEqual(noul_url, expected_url, "Redirected to the wrong page.")

    # def test1(self):
    #     actual = self.driver.current_url
    #     expected = 'https://the-internet.herokuapp.com/login'
    #     self.assertEqual(actual, expected)

    def test2_page_title(self):
        expected = "The Internet"
        actual = self.driver.title
        self.assertEqual(expected, actual)

    def test3_verifica_Xpath(self):
        element = self.driver.find_element(*self.textul).text
        expected_text = "Login Page"
        self.assertEqual(element, expected_text)

    def test4_verifica_btn_Login(self):
        afisat = self.driver.find_element(*self.loginbtn).is_displayed()
        if afisat is True:
            print("Login button is displayed")
        else:
            print("Login button is not displayed")

    def test5_href(self):
        linkul = self.driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
        actual_href = linkul.get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual_href, expected)

    def test6_empty_login(self):
        self.driver.find_element(*self.user).send_keys('')
        self.driver.find_element(*self.password).send_keys('')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.meseroare).is_displayed()

    def test7_invalid_login(self):
        self.driver.find_element(*self.user).send_keys('1')
        self.driver.find_element(*self.password).send_keys('2')
        self.driver.find_element(*self.loginbtn).click()
        actmes = self.driver.find_element(*self.meseroare).text
        expectedmes = 'Your username is invalid!'
        self.assertTrue(expectedmes in actmes, 'Error message text is incorrect')

    def test8_x_login(self):
        self.driver.find_element(*self.user).send_keys('')
        self.driver.find_element(*self.password).send_keys('')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.meseroare).is_displayed()
        self.driver.find_element(*self.xbtn).click()
        time.sleep(6)

    def test9_label(self):
        labels = self.driver.find_elements(By.TAG_NAME, 'label')
        lista = []
        for label in labels:
            lista.append(label.text)
        self.assertEqual(lista[0], 'Username')
        self.assertEqual(lista[1], 'Password')
        print(lista)

    def test10_secure(self):

        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.loginbtn).click()
        # noul_url = self.driver.current_url
        # self.assertIn('/secure', noul_url)
        # wait = WebDriverWait(self.driver, 10)
        # success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))) # de ce nu merge fara punct?
        # self.assertTrue(success_message.is_displayed())
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
        )
        self.assertTrue(success_message.is_displayed())

    def test11_logout(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.loginbtn).click()
        logout_url = self.driver.current_url
        expected_logout_url = 'https://the-internet.herokuapp.com/login'
        self.assertTrue(logout_url, expected_logout_url)



    def tearDown(self) -> None:
        self.driver.quit()

