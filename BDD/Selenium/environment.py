from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src.part_2_automation.bdd_selenium.features.browser import Browser
from src.part_2_automation.bdd_selenium.features.pages.autocomplete import Autocomplete


def before_all(context):
    # context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver = Browser()
    context.home = HomePage()
    context.autocomplete = Autocomplete()


def after_all(context):
    context.driver.quit()
