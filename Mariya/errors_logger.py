import logging
from config_module import current_day, current_time
class ErrorsLogger():
    def __init__(self, error_message) -> None:
        self._error_message = error_message
        self._current_day = current_day
        self._current_time = current_time

    def _log_config(func):
        def printer(*args, **kwgs):
            logging.basicConfig(level=logging.INFO, 
                            filename="py_log.log",
                            filemode="a+",
                            format="%(asctime)s %(levelname)s %(message)s")
            return func(*args, **kwgs)
        return printer
    
    @_log_config
    def print_error(self):
        return logging.error(f'Организация с ИНН: {self._error_message} не найдена.')
        
        #with open('log.txt', 'a+') as file:
        #    file.write(f'{self._current_day} {self._current_time} [ERROR/Ошибка] Организация с ИНН: {self._error_message} не найдена.')

#ErrorsLoger('Message').write_in_txt_log_file()


#logging.debug("A DEBUG Message")
#logging.info("An INFO")
#logging.warning("A WARNING")
#logging.error("An ERROR")
#logging.critical("A message of CRITICAL severity")



class MyClass:
#```
#В этом примере класс `MyClass` имеет метод `my_method`, который принимает два аргумента `arg1` и `arg2`. Этот метод может быть декорирован декоратором `my_decorator`.
#Для создания декоратора можно использовать синтаксис `@decorator_name`:
#```python
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Функция декорирована!")
            return func()
        return wrapper
 
 #Здесь мы определяем декоратор `my_decorator`, который принимает функцию `func` в качестве аргумента. Затем мы создаем функцию-обертку `wrapper`, которая выводит сообщение "Функция декорирована!" и затем вызывает исходную функцию `func`. Наконец, мы возвращаем эту функцию-обертку.
#Затем мы можем использовать этот декоратор внутри класса `MyClass`:
#```python
    @my_decorator # decorator_name = 'my_decorator'
    def my_method():
        return 'Ghbdtn'

#MyClass().my_method()