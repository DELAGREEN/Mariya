import logging
from config_module import current_day, current_time
class ErrorsLoger():
    def __init__(self, error_message) -> None:
        self._error_message = error_message
        self._current_day = current_day
        self._current_time = current_time

    def print_error_not_found_organization(self):
        logging.basicConfig(level=logging.INFO, 
                            filename="py_log.log",
                            filemode="a+",
                            format="%(asctime)s %(levelname)s %(message)s")
        logging.error(f'Организация с ИНН: {self._error_message} не найдена.')