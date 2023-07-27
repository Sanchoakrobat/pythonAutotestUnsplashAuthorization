import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_class import Base


class Main_page(Base):


# Locators
    text_Advertise = "//a[@class='Ue8P3 KHq0c BWSMq']"



# Getters
    def get_text_Advertise(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.text_Advertise)))




# Methods
    def assert_Advertise(self):
        with allure.step("assert_Advertise"):
            self.assert_word(self.get_text_Advertise(), "Advertise")
        # сравнивает надпись с заданной





