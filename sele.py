from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys



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
        driver = self.driver

        signin_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        signin_btn.click()

        registration_btn = driver.find_element_by_xpath('//button[@data-test="registration"]')
        registration_btn.click()

        reg_form_name = driver.find_element_by_xpath('//input[@data-test="registrationmodal-first-name-input"]')
        reg_form_name.send_keys("Stefan")
        
        reg_form_surname = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
        reg_form_surname.send_keys("Siarzewski")

        reg_form_gender = driver.find_element_by_id('register-gender-male')
        reg_form_gender.click()

        reg_form_countrycode = driver.find_element_by_class_name("phone-number__calling-code-selector__empty__placeholder")
        reg_form_countrycode.click()

        reg_form_countrycode_input = driver.find_element_by_name('phone-number-country-code')
        reg_form_countrycode_input.send_keys("pl", Keys.ENTER)

        reg_form_phone = driver.find_element_by_xpath('//input[@data-test="check-in-step-contact-phone-number"]')
        reg_form_phone.send_keys('123456789')

        reg_form_email = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        reg_form_email.send_keys('adres#bezmalpy.pl')

        reg_form_passwd = driver.find_element_by_xpath('//input[@data-test="booking-register-password"]')
        reg_form_passwd.send_keys('jakispasse23456*')

        reg_form_nationality = driver.find_element_by_xpath('//*[@data-test="booking-register-country"]')
        reg_form_nationality.send_keys('pol', Keys.ENTER)

        actions = webdriver.ActionChains(driver)

        checkbox_offers = driver.find_element_by_xpath('//input[@id="checkbox-newsletter"]')

        checkbox_priv_notice = driver.find_element_by_xpath('//input[@id="checkbox-privacyPolicy"]')

        checkbox_terms = driver.find_element_by_xpath('//input[@id="checkbox-wizzAccountPolicy"]')
        
        actions.click(checkbox_offers).click(checkbox_priv_notice).click(checkbox_terms).perform()

        sleep(3)

        possible_errors = driver.find_elements_by_xpath('//span[@class="input-error__message"]/span')
        visible_errors = []
        
        for error in possible_errors:
            if error.is_displayed():
                visible_errors.append(error)
                print(error)

        # assert len(visible_errors) == 1 
        self.assertEqual(len(visible_errors), 1)

        self.assertEqual(visible_errors[0].text, "Invalid e-mail") 


    # def testDrugi(self):
    #     print("Prawdziwy test drugi")

# Jeśli uruchamiamy z tego pliku
if __name__=="__main__":
    # Włączamy testy
    unittest.main()
