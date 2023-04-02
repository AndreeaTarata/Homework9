'''
Intrati pe site-ul https://www.elefant.ro/ si efectuati urmatoarele teste:

- Test 1: Identificati butonul "accept cookies" si dai click pe el
- Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
- Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "] -> //img[@class="product-image"]
- Test 4: Extrageti titlul paginii si verificati ca este corect
- Test 5: Intrati pe site, accesati butonul cont si click pe conectare.Identificati elementele de tip user si parola si inserati valori incorecte (valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
- Dati click pe butonul "conectare" si verificati urmatoarele:
            1. Faptul ca nu s-a facut logarea in cont
            2. Faptul ca se returneaza eroarea corecta
- Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin(unittest.TestCase):
    cookies = (By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    search = (By.NAME, 'SearchTerm')
    searchbtn = (By.NAME, 'search')

    cel_mai_mic_pret = (By.XPATH, '//*[@id="SortByDialog"]/div/div/div/ul/li[5]/a')

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://elefant.ro')
        self.driver.maximize_window()
        time.sleep(2)

    def test1_accept_cookies(self):
        self.driver.find_element(*self.cookies).click()

    def test2_seach_item(self):
        self.driver.find_element(*self.cookies).click()
        time.sleep(3)
        self.driver.find_element(*self.search).send_keys('iphone 14')
        self.driver.find_element(*self.searchbtn).click()
        time.sleep(3)
        rezultate = self.driver.find_elements(By.CLASS_NAME, "product-title")
        if len(rezultate) > 10:
            print(f'Sunt mai mult ede 10 rezultate, respectiv sunt {rezultate}')
        else:
            print(f'Cautarea a esuat. Sunt doar {rezultate}')

    # def test3_pret_mic(self):
    #     self.driver.find_element(*self.cookies).click()
    #     self.driver.find_element(*self.search).send_keys('iphone 14')
    #     self.driver.find_element(*self.searchbtn).click()
    #     time.sleep(4)
    #     self.driver.find_element(By.ID, "SortingAttribute").click()
    #     # self.driver.find_element(*self.cel_mai_mic_pret).click()
    #     time.sleep(5)
    #     elemet_prices = self.driver.find_elements(By.CLASS_NAME, 'current-price')
    #     dict_elemente = {}
    #     return_elements = self.driver.find_element(By.CLASS_NAME, 'product-title')
    #     for i in range(len(return_elements)):
    #         dict_elemente[return_elements[i].text] = elemet_prices[i].text.replace(".", "").replace(",", "").replace(" lei", "")[:-3]
    #     min_price = 99999999999999
    #     prod_min = ""
    #     for key, value in dict_elemente.items():
    #         min_price = value
    #         prod_min = key
    #     print(f'Produsul cu cel mai mic pret este: {prod_min} si valoarea de {min_price} lei')


    def tearDown(self) -> None:
        self.driver.close()
