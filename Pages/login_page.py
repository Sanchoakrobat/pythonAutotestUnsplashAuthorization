import allure

from Base.base_class import Base
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Login_page(Base):


    # Locators

    email = "//input[@name='user[email]']"
    password = "//input[@name='user[password]']"
    button_login = "//input[@class='btn btn-default btn-block-level']"


    # Getters
    def get_input_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.email)))
    # выбирает поле ввода email

    def get_input_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))
    # выбирает поле ввода password

    def get_button_login(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))
    # выбирает button login


    # Actions
    def input_email(self, input_email):
        self.get_input_email().send_keys(input_email)
        print("input email")
        # вводит email

    def input_password(self, input_password):
        self.get_input_password().send_keys(input_password)
        print("input password")
        # вводит password

    def click_button_login(self):
        self.get_button_login().click()
        print("click button login")
        # кликает  кнопку login


    # Methods
    def input_and_login(self):
        with allure.step("input_and_login"):
            self.get_input_email()
            self.input_email("kashin.alexandr.vasilevich@gmail.com")
            self.get_input_password()
            self.input_password("1234Trend+")
            self.get_button_login()
            self.click_button_login()
    # вводит данные и кликает кнопку login

