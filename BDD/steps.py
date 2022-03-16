from behave import *
from selenium import webdriver

# driver = webdriver.Chrome(executable_path='C:\\Users\\Moldoveanu\\Documents\\GitHub\\IT_Factory_Course\\src\\part_2_automation\\bdd_example\\features\\steps\\chromedriver.exe')
# driver.get('https://www.yahoo.com')
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.find_element_by_name('agree').click()
# driver.find_element_by_link_text('Conectare').click()
# email_address = ''
# pwd = ''

@given('I am willing to lear BDD')
def step_impl(context):
    print('First step')


@when('Taking IT Class from Paul')
def step_impl(context):
    print('Second step')


@then('I will get a better job')
def step_impl(context):
    print('Third step')


@given('My email address exists')
def step_impl(context):
    email_address = ''


@given('My password is correct')
def step_impl(context):
    pwd = ''


@given('I am not a robot')
def step_impl(context):
    print('First step')


@given('Password incorrect')
def step_impl(context):
    print('First step')


@when('I enter my credentials')
def step_impl(context):
    print('x')


@when('I click login')
def step_impl(context):
    print('Second step')


@then('Load my page')
def step_impl(context):
    print('Third step')


@then('Please fill user and password')
def step_impl(context):
    print('Third step')


@then('Please add a new password or click forgot password')
def step_impl(context):
    print('Third step')
