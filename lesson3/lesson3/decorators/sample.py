import logging

logging.basicConfig(format="%(levelname)s:%(name)s:%(message)s")



def logger(func):
    def wrapper(*args, **kwargs):
        logging.warning("Starting execution of: %s", {func.__name__})
        result = func(*args, **kwargs)
        logging.warning("Execution finished.")
        return result
    return wrapper


@logger
def multiply(a:int, b:int) -> int:
    logging.warning("result: %d",a * b)
