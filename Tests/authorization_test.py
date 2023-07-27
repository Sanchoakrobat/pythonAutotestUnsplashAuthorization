import time
import allure
from selenium import webdriver
from Pages.start_page import Start_page
from Pages.login_page import Login_page
from Pages.main_page import Main_page

@allure. description("Test authorization")
def test_authorization():

    driver = webdriver.Chrome()
    print("start authorization test")

    start = Start_page(driver)
    start.start()

    login = Start_page(driver)
    login.click_login_button()

    input_and_log = Login_page(driver)
    input_and_log.input_and_login()

    assert_adv = Main_page(driver)
    assert_adv.assert_Advertise()

    time.sleep(4)

    print("Finish authorization test")
    driver.quit()