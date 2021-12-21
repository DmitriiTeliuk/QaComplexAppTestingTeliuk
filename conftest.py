"""Conftest"""
import logging
import os
from constance.base import BaseConst


def pytest_runtest_setup(item):
    item.cls.log = logging.getLogger(".".join((item.module.__name__, item.cls.__name__, item.name)))


def pytest_sessionstart(session):
    os.environ["PATH"] = os.environ["PATH"] + f":{os.path.abspath(BaseConst.DRIVER_PATH)}"
    print(os.environ["PATH"])


class BaseTest:
    """Set some fields to provide autocomplete for dynamically added fields"""
    log = logging.getLogger(__name__)
