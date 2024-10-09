"""Conftest"""
import logging
import os

import pytest

from constants.base import BaseConst
from pages.data_for_tests import User
from pages.decor import create_driver
from pages.start_page import StartPage


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))


def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConst.DRIVER_PATH)}"
    print(os.environ["PATH"])


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)

    @pytest.fixture(scope="function")
    def driver(self, browser):
        """Create driver and close after tests"""
        driver = create_driver(browser=browser)
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
