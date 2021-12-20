import datetime
import logging
from time import sleep


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
