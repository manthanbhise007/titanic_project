import sys
from src.logger import logging

def error_detail_message(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in [{0}] at line [{1}] and the error is [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_detail_message(error_message, error_detail)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("divided by zero")
        raise CustomException(e, sys)