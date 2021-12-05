import random
from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

import locators


class TestFirstFive:
    @pytest.fixture(scope="function")
    def open_link(self):
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver")
        driver.get("https://qa-complex-app-for-testing.herokuapp.com/")
        sleep(1)
        yield driver
        driver.close()

    def random_num(self):
        return str(random.choice(range(11111, 99999)))

    def test_new_reg(self, open_link):
        """ 1.Загрузить страницу
            2.Ввести имя нового юзера
            3.Ввести валидную почту
            4.Ввести валидный пароль
            5. Нажать Sign UP Ожидание: Юзер успешно зарегистрирован
        """
        # add user name
        user_name = open_link.find_element(by=By.XPATH, value=locators.reg_user_name_field)
        user_name.clear()
        user_name.send_keys(f"user{self.random_num()}")
        sleep(1)
        # add user email
        user_email = open_link.find_element(by=By.XPATH, value=locators.reg_user_email_field)
        user_email.clear()
        user_email.send_keys(f"BOX{self.random_num()}@ads.com")
        # add user password
        user_pass = open_link.find_element(by=By.XPATH, value=locators.reg_user_pass_field)
        user_pass.clear()
        user_pass.send_keys(f"password{self.random_num()}")
        sleep(1)
        # click sign UP  button
        sing_up_button = open_link.find_element(by=By.XPATH, value=locators.reg_submit_butt)
        sing_up_button.click()
        sleep(1)
        # find new post button and check it
        create_post = open_link.find_element(by=By.XPATH, value=locators.create_post_butt)
        assert create_post.is_displayed()

    def test_log_in(self, open_link):
        """
        1. Загрузить страницу
        2.Ввести  логин / пароль уже существующего юзера
        Ожидание: Юзер  успешно залогинен.
        """
        # add already registered user name
        user_name = open_link.find_element(by=By.XPATH, value=locators.sign_in_user_name_field)
        user_name.clear()
        user_name.send_keys("DmytriiTeliuk")
        sleep(1)
        # add user password
        user_password = open_link.find_element(by=By.XPATH, value=locators.sign_in_password_field)
        user_name.clear()
        user_password.send_keys("goldenmask3421L")
        sleep(1)
        # click SIGN IN button
        sign_in_button = open_link.find_element(by=By.XPATH, value=locators.sign_in_butt)
        sign_in_button.click()
        sleep(1)
        # find new post button and check it
        create_post = open_link.find_element(by=By.XPATH, value=locators.create_post_butt)
        assert create_post.is_displayed()

    def test_base_validation_messages_in_reg_fields(self, open_link):
        """
        1. Загрузить страницу
        2. Нажать Sign UP
        Ожидание: Вылетают 3 сообщения об ошибке, юзер нe зарегистрирован
        """
        sign_up_button = open_link.find_element(by=By.XPATH, value=locators.reg_submit_butt)
        sign_up_button.click()
        sleep(1)
        name_error = open_link.find_element(by=By.XPATH, value=locators.reg_name_allert)
        email_error = open_link.find_element(by=By.XPATH, value=locators.reg_mail_allert)
        pass_error = open_link.find_element(by=By.XPATH, value=locators.reg_pass_alert)
        assert name_error.text == "Username must be at least 3 characters."
        assert email_error.text == "You must provide a valid email address."
        assert pass_error.text == "Password must be at least 12 characters."

    def test_reg_user_name_validation_message_2(self, open_link):
        """
        1. Загрузить страницу
        2. Ввести имя с пробелом
        Ожидание: Вылетает oшибка с текстом
        'Username can only contain letters and numbers.'
        """
        user_name = open_link.find_element(by=By.XPATH, value=locators.reg_user_name_field)
        user_name.clear()
        user_name.send_keys(f"David Jackson")
        sleep(1)
        user_name_message = open_link.find_element(by=By.XPATH, value=locators.reg_name_allert)
        assert user_name_message.text == "Username can only contain letters and numbers."

    def test_log_in_with_no_exist_user(self, open_link):
        """
        1.Загрузить страницу
        2.Залогиниться  с логин/пароль НЕсуществующего юзера
        Ожидание: Ошибка юзер не найден. Сообщение:'Error'
        """
        # add NO registered user name
        user_name = open_link.find_element(by=By.XPATH, value=locators.sign_in_user_name_field)
        user_name.clear()
        user_name.send_keys("DmytroPypko")
        sleep(1)
        # add NO registered user password
        user_password = open_link.find_element(by=By.XPATH, value=locators.sign_in_password_field)
        user_name.clear()
        user_password.send_keys("wqwddsddd2333")
        sleep(1)
        # click SIGN IN button
        sign_in_button = open_link.find_element(by=By.XPATH, value=locators.sign_in_butt)
        sign_in_button.click()
        sleep(1)
        # find new post button and check it
        error_message = open_link.find_element(by=By.XPATH, value=locators.login_alert)
        assert error_message.is_displayed()
