import pytest
from selenium.webdriver.chrome import webdriver
from constance.base import BaseConst
from conftest import BaseTest
from pages.data_for_tests import User
from pages.start_page import StartPage


class TestStartPage(BaseTest):
    @pytest.fixture(scope="function")
    def driver(self):
        """Create driver and close after tests"""
        driver = webdriver.WebDriver(executable_path=BaseConst.DRIVER_PATH)
        # driver.implicitly_wait(1)
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def open_start_page(self, driver):
        """Return start page"""
        driver.get(BaseConst.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def random_user(self):
        """Create random user data"""
        user = User()
        user.fill_user_data()
        return user

    @pytest.fixture(scope="function")
    def reg_user_and_sign_out(self, open_start_page, random_user):
        """Register new user"""
        main_page = open_start_page.reg_new_user(random_user)
        main_page.log_out()
        return random_user

    def test_new_reg(self, open_start_page, random_user):
        """
        Pre-conditions:
            1.Upload StartPage
        Steps:
            2.Enter user name
            3.Enter valid email
            4.Enter valid password
            5. Click Sign UP
        Expected:
            User is registered successfully
        """
        # register new user
        main_page = open_start_page.reg_new_user(random_user)
        main_page.is_displayed_create_post_button()
        self.log.info("test_new_reg completed successfully")

    def test_log_in(self, open_start_page, reg_user_and_sign_out):
        """
        Pre-conditions:
            1.Register new user
        Steps:
            2.Enter user name/password
            3.Click Log in
        Expected:
            User is logged in successfully
        """
        login = open_start_page.log_in(reg_user_and_sign_out)
        login.is_displayed_create_post_button()
        self.log.info("test_log_in completed successfully")

    def test_base_validation_messages_in_reg_fields(self, open_start_page):
        """
        Pre-conditions:
            1.Upload StartPage
        Steps:
            2. Click Sign UP
        Expected:
            3 Alerts for user name/email/password appears
        """
        open_start_page.sign_up_button_click(0)
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username must be at least 3 characters."

        email_alert = open_start_page.get_new_user_email_field_alert()
        assert email_alert == "You must provide a valid email address."

        password_alert = open_start_page.get_new_user_password_field_alert()
        assert password_alert == "Password must be at least 12 characters."
        self.log.info("Test_base_validation_messages_in_reg_fields completed successfully")

    def test_reg_user_name_validation_message_2(self, open_start_page):
        """
        Pre-conditions:
            1.Upload StartPage
        Steps:
            2. Enter user name with whitespace
        Expected:
            Error message: 'Username can only contain letters and numbers.'
        """
        open_start_page.fill_new_user_name("Dmitrii Teliuk")
        name_alert = open_start_page.get_new_user_name_field_alert()
        assert name_alert == "Username can only contain letters and numbers."
        self.log.info("'Name Alert' message  is correct test_reg_user_name_validation_message_2 completed successfully")

    def test_log_in_with_no_exist_user(self, open_start_page, random_user):
        """
        Pre-conditions:
            1.Upload StartPage
        Steps:
            2.Log in with username/password of a non-existent user
        Expected: Log in Alert:'Error'
        """
        open_start_page.log_in(random_user)
        open_start_page.is_displayed_login_message_alert()
        self.log.info("'Log in Alert' message  is correct. test_log_in_with_no_exist_user completed successfully")
