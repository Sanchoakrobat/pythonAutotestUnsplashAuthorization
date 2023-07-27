

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_class import Base


class Start_page(Base):
    url = 'https://unsplash.com'


    # Locators
    login_button = "//a[@class='cLLOA p1cWU jpBZ0 EzsBC KHq0c XHI2L']"



    # Getters
    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
    # выбирает кнопку Логин


    # Actions
    def click_login_button(self):
        self.get_login_button().click()
        print("click login button")
        # кликает кнопку Логин



    # Methods
    def start(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()









