from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='/src/part_2_automation/bdd_example/features/steps/chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/login')
driver.implicitly_wait(5)
driver.maximize_window()

# Test invalid username login
USERNAME = (By.ID, 'username')
PASSWORD = (By.ID, 'password')
LOGIN = (By.CLASS_NAME, 'radius')
MESSAGE = (By.ID, 'flash')
SUB_HEADER = (By.CLASS_NAME, 'subheader')
LOGOUT = (By.CSS_SELECTOR, '#content > div > a')

driver.find_element(*USERNAME).send_keys('username')
driver.find_element(*PASSWORD).send_keys('password')
driver.find_element(*LOGIN).click()

actual_message = driver.find_element(*MESSAGE).text
assert 'invalid' in actual_message


# Test valid username and password login
user_pwd = driver.find_element(*SUB_HEADER).text
new_list = user_pwd.split('.')[1].split()

# First variant
# user, pwd = '', ''
# for i in range(len(new_list)):
#     if new_list[i] == 'Enter':
#         user = new_list[i + 1]
#     if new_list[i] == 'and':
#         pwd = new_list[i + 1]

# Second variant
user_pass = driver.find_elements(By.XPATH, '//h4[@class="subheader"]//em')
user = user_pass[0].text
pwd = user_pass[1].text

driver.find_element(*USERNAME).send_keys(user)
driver.find_element(*PASSWORD).send_keys(pwd)
driver.find_element(*LOGIN).click()

actual_message = driver.find_element(*MESSAGE).text
assert 'logged' in actual_message

driver.find_element(*LOGOUT).click()

# Username and Password empty
driver.find_element(*USERNAME).send_keys('')
driver.find_element(*PASSWORD).send_keys('')
driver.find_element(*LOGIN).click()

actual_message = driver.find_element(*MESSAGE).text
assert 'invalid' in actual_message

# time.sleep(5)
driver.quit()
