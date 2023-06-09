import sys

class ErrorsLoger():
    def __init__(self, error_message) -> None:
        self.error_message = error_message
        pass

    def print_error_not_found_organization(self) -> None:
        print(f'[ERROR/Ошибка] Организация с ИНН: {self.error_message} не найдена.')
        return None
    
    def write_in_txt_log_file(self):
        pass
