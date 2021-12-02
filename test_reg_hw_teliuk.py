import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

import locators


class TestStartPage:

    def random_num(self):
        return str(random.choice(range(11111, 99999)))

    def test_reg_check_by_create_post_button(self):
        """Sample test"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # add user name
        sleep(1)
        user_name = driver.find_element(by=By.XPATH, value=locators.reg_user_name_field)
        user_name.clear()
        user_name.send_keys(f"user{self.random_num()}")
        sleep(1)
        # add user email
        user_email = driver.find_element(by=By.XPATH, value=locators.reg_user_email_field)
        user_email.clear()
        user_email.send_keys(f"BOX{self.random_num()}@ads.com")
        # add user password
        user_pass = driver.find_element(by=By.XPATH, value=locators.reg_user_pass_field)
        user_pass.clear()
        user_pass.send_keys(f"password{self.random_num()}")
        sleep(1)
        # click sign UP  button
        sing_up_button = driver.find_element(by=By.XPATH, value=locators.reg_submit_butt)
        sing_up_button.click()
        sleep(1)
        # find new post button and check it
        create_post = driver.find_element(by=By.XPATH, value=locators.create_post_butt)
        assert create_post.is_displayed()

    def test_reg_check_by_profile_ref(self):
        """Random user registration and check that my profile element displayed"""
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        # add user name and remember value for user name field to use it in my profile locator
        sleep(1)
        user_name = driver.find_element(by=By.XPATH, value=locators.reg_user_name_field)
        user_name.clear()
        user_name_value = f"user{self.random_num()}"
        user_name.send_keys(user_name_value)
        sleep(1)
        # add user email
        user_email = driver.find_element(by=By.XPATH, value=locators.reg_user_email_field)
        user_email.clear()
        user_email.send_keys(f"BOX{self.random_num()}@ads.com")
        # add user password
        user_pass = driver.find_element(by=By.XPATH, value=locators.reg_user_pass_field)
        user_pass.clear()
        user_pass.send_keys(f"password{self.random_num()}")
        sleep(1)
        # click sign UP  button
        sing_up_button = driver.find_element(by=By.XPATH, value=locators.reg_submit_butt)
        sing_up_button.click()
        sleep(1)
        print(user_name_value)
        # find my profile button and check it is displayed
        my_profile_button_locator = f"//a[@href='/profile/{user_name_value}']"
        my_profile_button = driver.find_element(by=By.XPATH, value=my_profile_button_locator)
        assert my_profile_button.is_displayed()
