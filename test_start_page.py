import random
import pytest
from selenium.webdriver.chrome import webdriver
from constance.base import BaseConst
from conftest import BaseTest
from pages.data_for_tests import User
from pages.start_page import StartPage


class TestStartPage(BaseTest):
    @pytest.fixture(scope="function")
    def driver(self):
        driver = webdriver.WebDriver(executable_path=BaseConst.DRIVER_PATH)
        # driver.implicitly_wait(1)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def open_start_page(self, driver):
        driver.get(BaseConst.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def random_user(self):
        """Create values for user"""
        user = User()
        user.fill_user_data()
        return user

    @pytest.fixture(scope="function")
    def reg_user_and_sign_out(self, open_start_page, random_user):
        """register new user"""
        main_page = open_start_page.reg_new_user(random_user)
        main_page.log_out()
        return random_user

    def random_num(self):
        return str(random.choice(range(11111, 99999)))

    def test_new_reg(self, open_start_page, random_user):
        """ 1.Загрузить страницу
            2.Ввести имя нового юзера
            3.Ввести валидную почту
            4.Ввести валидный пароль
            5. Нажать Sign UP Ожидание: Юзер успешно зарегистрирован
        """
        # register new user
        main_page = open_start_page.reg_new_user(random_user)
        self.log.info("Registration fields are filled and 'sign in' button clicked")
        main_page.is_displayed_create_post_button()
        self.log.info("test_new_reg completed successfully")

    def test_log_in(self, open_start_page, reg_user_and_sign_out):
        """
        1. Загрузить страницу
        2.Ввести  логин / пароль уже существующего юзера
        Ожидание: Юзер  успешно залогинен.
        """
        login = open_start_page.log_in(reg_user_and_sign_out)
        self.log.info("Log in credentials added.'Sign IN' button clicked")
        login.is_displayed_create_post_button()
        self.log.info("test_log_in completed successfully")

    def test_base_validation_messages_in_reg_fields(self, open_start_page):
        """
        1. Загрузить страницу
        2. Нажать Sign UP
        Ожидание: Вылетают 3 сообщения об ошибке, юзер нe зарегистрирован
        """
        open_start_page.sign_up_button_click(0)
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username must be at least 3 characters."
        self.log.info("name alert checked")

        email_alert = open_start_page.get_new_user_email_field_alert()
        assert email_alert == "You must provide a valid email address."
        self.log.info("email alert checked")

        password_alert = open_start_page.get_new_user_password_field_alert()
        assert password_alert == "Password must be at least 12 characters."
        self.log.info("password alert checked. test_base_validation_messages_in_reg_fields completed successfully")

    def test_reg_user_name_validation_message_2(self, open_start_page):
        """
        1. Загрузить страницу
        2. Ввести имя с пробелом
        Ожидание: Вылетает oшибка с текстом
        'Username can only contain letters and numbers.'
        """
        open_start_page.fill_new_user_name("Dmitrii Teliuk")
        self.log.info("invalid name added to new_user name field")
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username can only contain letters and numbers."
        self.log.info("'Name Alert' message  is correct/ test_reg_user_name_validation_message_2 completed successfully")

    def test_log_in_with_no_exist_user(self, open_start_page, random_user):
        """
        1.Загрузить страницу
        2.Залогиниться  с логин/пароль НЕсуществующего юзера
        Ожидание: Ошибка юзер не найден. Сообщение:'Error'
        """
        open_start_page.log_in(random_user)
        self.log.info("Non existent login/password added")
        open_start_page.is_displayed_login_message_alert()
        self.log.info("'Log in Alert' message  is correct. test_log_in_with_no_exist_user completed successfully")
