import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

import locators


class TestStartPage:

    def test_start_page(self):
        """Sample test"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        user_name = driver.find_element(by=By.XPATH, value=locators.sign_in_user_name_field)
        user_name.clear()
        user_pass = driver.find_element(by=By.XPATH, value=locators.sign_in_password_field)
        user_pass.clear()
        sing_in_button = driver.find_element(by=By.XPATH, value=locators.sign_in_butt)
        sing_in_button.click()
        sleep(1)
        message = driver.find_element(by=By.XPATH, value=locators.login_alert)
        assert message.text == "Error"

    def random_num(self):
        return str(random.choice(range(11111, 99999)))

    def test_start_page_1(self):
        """Sample test"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # add user name
        user_name = driver.find_element(by=By.XPATH, value=locators.sign_in_user_name_field)
        user_name.clear()
        user_name.send_keys(f"User{self.random_num()}")
        sleep(1)
        # add user password
        user_pass = driver.find_element(by=By.XPATH, value=locators.sign_in_password_field)
        user_pass.clear()
        user_pass.send_keys(f"password{self.random_num()}")
        sleep(1)
        # click sign in button
        sing_in_button = driver.find_element(by=By.XPATH, value=locators.sign_in_butt)
        sing_in_button.click()
        sleep(1)
        message = driver.find_element(by=By.XPATH, value=locators.login_alert)
        assert message.text == "Error"
