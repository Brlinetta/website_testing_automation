from base_page import BasePage
from selenium.webdriver.common.by import By

login_button = (By.CLASS_NAME, 'login-button')


class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://gymlog.ru/')

    def open_sign_in(self):
        self.find_element(login_button).click()