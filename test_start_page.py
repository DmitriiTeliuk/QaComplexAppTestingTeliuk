import random
from time import sleep

import pytest
from selenium.webdriver.chrome import webdriver


from QaComplexAppTestingTeliuk.Constance.base import BaseConst
from QaComplexAppTestingTeliuk.pages.start_page import StartPage


class TestStartPage:
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(executable_path=BaseConst.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def open_start_page(self, driver):
        driver.get(BaseConst.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def reg_user_and_sign_out(self, open_start_page):
        user_name = f"User{self.random_num()}"
        user_email = f"BOX{self.random_num()}@testmail.com"
        user_password = f"MYTESTPASS{self.random_num()}"
        # register new user
        main_page = open_start_page.reg_new_user(user_name, user_email, user_password)
        sleep(2)
        main_page.log_out()
        return user_name, user_password

    def random_num(self):
        return str(random.choice(range(11111, 99999)))

    def test_new_reg(self, open_start_page):
        """ 1.Загрузить страницу
            2.Ввести имя нового юзера
            3.Ввести валидную почту
            4.Ввести валидный пароль
            5. Нажать Sign UP Ожидание: Юзер успешно зарегистрирован
        """
        user_name = f"User{self.random_num()}"
        user_email = f"BOX{self.random_num()}@testmail.com"
        user_password = f"MYTESTPASS{self.random_num()}"
        # register new user
        main_page = open_start_page.reg_new_user(user_name, user_email, user_password)
        sleep(3)
        main_page.is_displayed_create_post_button()

    def test_log_in(self, open_start_page, reg_user_and_sign_out):
        """
        1. Загрузить страницу
        2.Ввести  логин / пароль уже существующего юзера
        Ожидание: Юзер  успешно залогинен.
        """
        username, password = reg_user_and_sign_out
        login = open_start_page.log_in(username, password)
        login.is_displayed_create_post_button()

    def test_base_validation_messages_in_reg_fields(self, open_start_page):
        """
        1. Загрузить страницу
        2. Нажать Sign UP
        Ожидание: Вылетают 3 сообщения об ошибке, юзер нe зарегистрирован
        """
        sleep(1)
        open_start_page.click_sign_up_button()
        sleep(1)
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username must be at least 3 characters."

        email_alert = open_start_page.get_new_user_email_field_alert()
        assert email_alert == "You must provide a valid email address."

        password_alert = open_start_page.get_new_user_password_field_alert()
        assert password_alert == "Password must be at least 12 characters."

    def test_reg_user_name_validation_message_2(self, open_start_page):
        """
        1. Загрузить страницу
        2. Ввести имя с пробелом
        Ожидание: Вылетает oшибка с текстом
        'Username can only contain letters and numbers.'
        """
        open_start_page.fill_new_user_name("Dmitrii Teliuk")
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username can only contain letters and numbers."

    def test_log_in_with_no_exist_user(self, open_start_page):
        """
        1.Загрузить страницу
        2.Залогиниться  с логин/пароль НЕсуществующего юзера
        Ожидание: Ошибка юзер не найден. Сообщение:'Error'
        """
        open_start_page.log_in("asdksdja", "sjakd222")
        open_start_page.is_displayed_login_message_alert()

