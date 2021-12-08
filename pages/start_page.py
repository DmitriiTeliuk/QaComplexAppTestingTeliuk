import random

from selenium.webdriver.common.by import By

from QaComplexAppTestingTeliuk.Constance.start_page import StartPageConst
from QaComplexAppTestingTeliuk.pages.base_page import BasePage
from QaComplexAppTestingTeliuk.pages.main_page import MainPage


class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.constance = StartPageConst()

    def login(self, user_name, user_password):
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_NAME_XPATH, some_value=user_name)
        self.fill_field(By.XPATH, self.constance.FIELD_SIGN_IN_USER_PASSWORD_XPATH, some_value=user_password)
        sign_in_button = self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_IN_XPATH)
        sign_in_button.click()
        return MainPage(self.driver)

    def reg_new_user(self,user_name, user_email, user_password):
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_EMAIL_XPATH, some_value=user_email)
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_PASSWORD_XPATH, some_value=user_password)
        sign_up_button = self.driver.find_element(by=By.XPATH, value=self.constance.BUTTON_SIGN_UP_XPATH)
        sign_up_button.click()
        return MainPage(self.driver)

    def fill_new_user_name(self,user_name):
        self.fill_field(By.XPATH, self.constance.FIELD_NEW_USER_NAME_XPATH, some_value=user_name)
