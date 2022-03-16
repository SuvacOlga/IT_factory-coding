from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()

    def quit(self):
        self.driver.quit()
© 2022 GitHub, Inc.
Terms
Privacy
