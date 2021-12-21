import datetime
import logging
from time import sleep

from selenium.webdriver.chrome import webdriver as chrome
from selenium.webdriver.firefox import webdriver as firefox

from constance.base import BaseConst


def wait_until_okk(timeout, period):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    return original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    else:
                        sleep(period)

        return wrapper

    return decorator


def new_logdecor(func):
    """Creates logs"""

    def wrapper(*args, **kwargs):
        log = logging.getLogger("[NewLogger]")
        result = func(*args, **kwargs)
        log.info("%s", func.__doc__)
        return result

    return wrapper


def create_driver(browser):
    """Create driver according to browser"""
    if browser == BaseConst.CHROME:
        driver = chrome.WebDriver()
    elif browser == BaseConst.FIREFOX:
        driver = firefox.WebDriver()
    else:
        raise RuntimeError(f"Unknown browser, name: {browser}")
    return driver
