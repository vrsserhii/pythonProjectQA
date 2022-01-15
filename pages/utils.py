import datetime
import logging
from time import sleep


def wait_until_ok(timeout=10, period=0.25):
    logger = logging.getLogger("[WaitUntilOk]")

    def decorator(original_function):

        def wrapper(*args, **kwargs):
            end_time = datetime.datetime.now() + datetime.timedelta(seconds=timeout)
            while True:
                try:
                    result = original_function(*args, **kwargs)
                except Exception as err:
                    if datetime.datetime.now() > end_time:
                        logger.warning(f"Catch: {err}")
                        raise err
                    else:
                        sleep(period)
                else:
                    return result

        return wrapper

    return decorator
