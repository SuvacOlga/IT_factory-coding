from behave import *
import time

from selenium.webdriver.common.by import By


@given('I go to autocomplete form')
def step_impl(context):
    context.driver.get('https://formy-project.herokuapp.com/')
    time.sleep(2)
    context.driver.find_element(By.LINK_TEXT, 'Autocomplete').click()
    time.sleep(2)


@when('I type CJ in address field')
def step_impl(context):
    # context.driver.find_element(By.ID, 'autocomplete').send_keys('CJ')
    context.autocomplete.enter_address_name('CJ')
    time.sleep(2)


@then('Cluj should be return')
def step_impl(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,
                                                'body > div.pac-container > div > div:nth-child(2) > span').text
    assert 'Cluj' in actual_result


@then('Postal code')
def step_impl(context):
    pass


@when('I type "{city}" in address field')
def step_impl(context, city):
    context.driver.find_element(By.ID, 'autocomplete').send_keys(city)
    time.sleep(2)


@then('"{actual_city}" should be return')
def step_impl(context, actual_city):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,
                                                'body > div.pac-container > div > div:nth-child(2) > span').text
    assert actual_city in actual_result
