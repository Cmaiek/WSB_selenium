from selenium import webdriver
from time import sleep



# driver.get("https://altostratus.pl")

# sleep(10)

# driver.quit()

import unittest

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.driver.get("http://www.wizzair.com")


    def tearDown(self):
        print("Sprzątanie po teście")
        self.driver.quit()

    def testInvalidEmail(self):
        print("Prawdziwy test")
        signin_button = self.driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        signin_button.click()
        sleep(10)

    def testDrugi(self):
        print("Prawdziwy test drugi")

# Jeśli uruchamiamy z tego pliku
if __name__=="__main__":
    # Włączamy testy
    unittest.main()
