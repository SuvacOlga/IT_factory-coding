from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/src/part_2_automation/bdd_example/features/steps/chromedriver.exe')
driver.get('https://www.google.com')
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.ID, 'L2AGLb').click()
search_form = driver.find_element(By.NAME, 'q')
# search_form.send_keys('Romania', Keys.ENTER)
search_form.send_keys('Romania')
search_form.submit()
