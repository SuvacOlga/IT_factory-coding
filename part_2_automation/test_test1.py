# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://www.wikipedia.org/")
    self.driver.set_window_size(1920, 1040)
    self.driver.find_element(By.ID, "searchInput").click()
    self.driver.find_element(By.ID, "searchInput").send_keys("Romania")
    self.driver.find_element(By.ID, "searchInput").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".tocsection-21 .toctext").click()
    self.driver.execute_script("window.scrollTo(0,10634)")
    self.driver.find_element(By.CSS_SELECTOR, ".thumb:nth-child(30) .thumbimage").click()
    self.driver.execute_script("window.scrollTo(0,0)")