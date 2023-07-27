import allure


class Base():

    def __init__(self, driver):
        self.driver = driver

    #  method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    #  method assert word
    def assert_word(self, word, result):
        with allure.step("assert word"):
            value_word = word.text
            print(value_word)
            assert value_word == result
            print("Good value word")
    # сравнивает парсенный текст с заданным