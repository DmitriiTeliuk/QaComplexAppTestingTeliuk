import random
from time import sleep

from selenium.webdriver.common.by import By

from QaComplexAppTestingTeliuk.Constance.start_page import StartPageConst
from QaComplexAppTestingTeliuk.pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = StartPageConst()

    def log_in(self, user_name, user_password):
        from QaComplexAppTestingTeliuk.pages.main_page import MainPage
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_NAME_XPATH, some_value=user_name)
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_PASSWORD_XPATH, some_value=user_password)
        sign_in_button = self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_IN_XPATH)
        sleep(1)
        sign_in_button.click()
        sleep(1)
        return MainPage(self.driver)

    def reg_new_user(self, user_name, user_email, user_password):
        from QaComplexAppTestingTeliuk.pages.main_page import MainPage
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_EMAIL_XPATH, some_value=user_email)
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_PASSWORD_XPATH, some_value=user_password)
        sign_up_button = self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_UP_XPATH)
        sleep(1)
        sign_up_button.click()
        return MainPage(self.driver)

    def fill_new_user_name(self, user_name):
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
        sleep(1)

    def click_sign_up_button(self):
        self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_UP_XPATH).click()
        sleep(1)

    def click_sign_in_button(self):
        self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_IN_XPATH).click()
        sleep(1)

    def get_new_user_name_field_alert(self):
        alert = self.driver.find_element(by=By.XPATH, value=self.constance.ALERT_NEW_USER_NAME_XPATH)
        assert alert.is_displayed()
        return alert.text

    def get_new_user_email_field_alert(self):
        alert = self.driver.find_element(by=By.XPATH, value=self.constance.ALERT_NEW_USER_EMAIL_XPATH)
        assert alert.is_displayed()
        return alert.text

    def get_new_user_password_field_alert(self):
        alert = self.driver.find_element(by=By.XPATH, value=self.constance.ALERT_NEW_USER_PASSWORD_XPATH)
        assert alert.is_displayed()
        return alert.text

    def is_displayed_login_message_alert(self):
        error_message = self.driver.find_element(by=By.XPATH, value=self.constance.ALERT_LOG_IN_XPATH)
        assert error_message.is_displayed()
