import datetime
import logging
from time import sleep


# def wait_until_ok(timeout=3, period=0.25):
#     log = logging.getLogger("[WaitUntilOK]")
#
#     def decorator(main_func):
#
#         def wrapper(*args, **kwargs):
#             end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
#             while True:
#                 try:
#                     return main_func(*args, **kwargs)
#                 except Exception as err:
#                     if datetime.datetime.now() > end_time:
#                         log.warning(f"Error: {err} .Left time {end_time - datetime.datetime.now()}")
#                         raise err
#                     sleep(period)
#
#         return wrapper()
#
#     return decorator

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
