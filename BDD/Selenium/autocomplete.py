from selenium.webdriver.common.by import By

from src.part_2_automation.bdd_selenium.features.browser import Browser


class Autocomplete(Browser):
    ADDRESS_ID = 'autocomplete'
    STREET_ADDRESS_ID = 'street_number'

    def enter_address_name(self, address):
        self.driver.find_element(By.ID, self.ADDRESS_ID).send_keys(address)

    def enter_street_address_name(self, street_number):
        self.driver.find_element(By.ID, self.STREET_ADDRESS_ID).send_keys(street_number)
