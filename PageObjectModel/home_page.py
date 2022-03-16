from selenium.webdriver.common.by import By
from src.part_2_automation.PageObjectModel.pages.base_page import BasePage


class HomePage(BasePage):
    AUTOCOMPLETE = (By.LINK_TEXT, 'Autocomplete')
    BUTTONS = 'Buttons'

    def go_to_autocomplete(self):
        self._driver.find_element(*self.AUTOCOMPLETE).click()

    def click_on_buttons(self):
        self._driver.find_element(By.LINK_TEXT, self.BUTTONS).click()
