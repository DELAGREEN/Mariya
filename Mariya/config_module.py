# -*- coding: utf-8 -*-
import os
from datetime import datetime


# region important
'''
TIME
'''
time = datetime.now()
current_time = time.strftime('%H:%M')
current_day = time.strftime('%d/%m/%Y').replace('/', '.')
print(current_time, current_day)
# endregion


# region important
'''
System conf
'''
time_sleep = 3
path_to_home_dir = os.getcwd()                                  # пусть распложения main

path_to_data_dir = path_to_home_dir + '\\data'
path_to_loads_dir = path_to_data_dir + '\\loads'                  # путь к папке
path_to_data = path_to_data_dir + '\\data.xlsx'                 # путь к файлу EXEL
path_to_final_exel_file = path_to_home_dir + '\\finalfile.xlsx'
# endregion
print(path_to_final_exel_file)

