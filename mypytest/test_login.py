from selenium import webdriver
import pytest
class Test_method():
    @classmethod
    def setupclass(cls):
        cls.driver = webdriver.chrome(executable_path='C:/Users/kramk/PycharmProjects/selenium/godse/chromedriver.exe')
        cls.driver.maximize_browser_window
        test_url = cls.driver.get("https://demo.nopcommerce.com/login")
    def test_logintest(self):
        self.driver.find_element_by_id("Email").send_keys("kranthi13@gmail.com")
        self.driver.find_element_by_id("Password").send_keys("Krna@1223")
        self.driver.find_element_by_class("button-1 login-button").click()
    @classmethod
    def teardown(cls):
        print("completed program........")


