import random
from time import sleep
import pytest
from selenium.webdriver.chrome import webdriver
from QaComplexAppTestingTeliuk.Constance.base import BaseConst
from QaComplexAppTestingTeliuk.conftest import BaseTest
from QaComplexAppTestingTeliuk.pages.start_page import StartPage


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
    def reg_user_and_sign_out(self, open_start_page):
        user_name = f"User{self.random_num()}"
        user_email = f"BOX{self.random_num()}@testmail.com"
        user_password = f"MYTESTPASS{self.random_num()}"
        # register new user
        main_page = open_start_page.reg_new_user(user_name, user_email, user_password)
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
        self.log.info("Registration fields are filled and 'sign in' button clicked")
        main_page.is_displayed_create_post_button()
        self.log.info("test_new_reg completed successfully")

    def test_log_in(self, open_start_page, reg_user_and_sign_out):
        """
        1. Загрузить страницу
        2.Ввести  логин / пароль уже существующего юзера
        Ожидание: Юзер  успешно залогинен.
        """
        username, password = reg_user_and_sign_out
        login = open_start_page.log_in(username, password)
        self.log.info("Log in credentials added.'Sign IN' button clicked")
        login.is_displayed_create_post_button()
        self.log.info("test_log_in completed successfully")

    def test_base_validation_messages_in_reg_fields(self, open_start_page):
        """
        1. Загрузить страницу
        2. Нажать Sign UP
        Ожидание: Вылетают 3 сообщения об ошибке, юзер нe зарегистрирован
        """
        open_start_page.sign_up_button_click()
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

    def test_log_in_with_no_exist_user(self, open_start_page):
        """
        1.Загрузить страницу
        2.Залогиниться  с логин/пароль НЕсуществующего юзера
        Ожидание: Ошибка юзер не найден. Сообщение:'Error'
        """
        open_start_page.log_in("asdksd@jax.com", "sjakd222")
        self.log.info("Non existent login/password added")
        open_start_page.is_displayed_login_message_alert()
        self.log.info("'Log in Alert' message  is correct. test_log_in_with_no_exist_user completed successfully")
