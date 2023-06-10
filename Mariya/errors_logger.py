import logging
from config_module import current_day, current_time
class ErrorsLogger():
    def __init__(self, message = None) -> None:
        self._message = message
        self._current_day = current_day
        self._current_time = current_time

    def _log_config(func) -> object:
        def printer(*args, **kwgs) -> object:
            logging.basicConfig(level=logging.INFO, 
                            filename="py_log.log",
                            filemode="a+",
                            format="%(asctime)s %(levelname)s %(message)s")
            return func(*args, **kwgs)
        return printer
    
    @_log_config
    def print_error(self) -> object:
        return logging.warning(f'Организация с ИНН: {self._message} не найдена.')
    @_log_config
    def print_info(self) -> object:
        return logging.info(f'{self._message}')
    @_log_config
    def print_warning(self) -> object:
        return logging.warning(f'{self._message}')
    @_log_config
    def print_critical(self) -> object:
        return logging.critical(f'{self._message}')
    @_log_config
    def print_debug(self) -> object:
        return logging.debug(f'{self._message}')

'''
#############
###Example###
#############

logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

'''