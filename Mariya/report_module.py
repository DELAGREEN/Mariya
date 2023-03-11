# -*- coding: utf-8 -*-
import os.path
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as load_workbook
from openpyxl.styles.borders import Border, Side
import os
import time
from config_module import(path_to_data_dir, path_to_data, path_to_final_exel_file, path_to_loads_dir) 

def what_in_folder(path_to_request_dir):
    path_to_dir = os.listdir(path_to_request_dir)
    #print(f"список список файлов, из {path_to_request_dir} >> {path_to_dir}")
    return path_to_dir


def make_book(path_to_data):
    '''
    Создаем xlsx файл для записи в него
    '''
    wb = Workbook()
    wb.save(path_to_data)     # сохнаняем с именем лежащей в переменной


def make_dirs(path_to_data_dir):
    '''
    Создаем папки для рабочих 'ДЛЯ УДОБСТВА' процессов
    '''
    os.makedirs(path_to_data_dir)


def read_exel(path = path_to_data):
    list = []
    book = load_workbook(path, read_only=True)
    sheet = book.active
    for row in sheet.iter_rows(min_col = 1, max_col=1, min_row=1, max_row = sheet.max_row):
        #nim_row минимальное количество строк 
        #max_col максимальное количество столбцов 
        #max_row максильманое колличество строк
        for data in row:
            out = data.value
            if out not in list:
                list.append(out)
            else:
                break
    print(list)
    return list
#read_exel(path_to_data)

def append_in_data(list, path_to_file = path_to_final_exel_file):
    wb = Workbook()
    ws = wb.active
    #print(value)
    for item in list:
        ws.append(item)
    wb.save(path_to_file)
    return(print('append in data >> ok'))


def list_in_list(list):
    '''
    ОБЕРТКА СПИСОК В СПИСОК list[list[]]
    '''
    total_list = []
    for i in list:
        u = [i]
        total_list.append(u)
    return total_list
 

def add_style():
    '''
    Работает
    '''
    #from openpyxl import Workbook
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thick'))  #жирная полоса
    wb = Workbook()
    ws = wb.active
    ws.cell(row=3, column=2).border = thin_border
    wb.save('border_test.xlsx')



def passage_in_folder_files(path_to_dir):
    folder = what_in_folder(path_to_dir)
    i = '\\'
    data = read_exel(path_to_dir + i + folder[0], 11)
    for item in data:
        print(data.index(item), item)

#passage_in_folder_files(loads_dir)



def exel_reader(path_to_file) -> list:
    book = load_workbook(path_to_file, read_only=True)
    sheet = book.active
    ws = sheet['A1' : 'K16']
    list = []
    for row in ws:
        for cell in row:
                out = cell.value
                if out is not None:
                    list.append(out)
                    #print(list.index(out), out)
                else:
                    break

    yield list
 

def example(list):
    for item in list:
        index = list.index(item)
        print(f'{index}>> {item}')

def top_matrix_to_file(path_to_file) -> None:
    list = ['ИНН', 'Индекс формы', 'Наименование формы', 'Периодичность формы', 'Срок сдачи формы', 
             'Отчетный период','Комментарий', 'ОКУД', 'Дата актуализации перечня форм']
            
    #wb = Workbook()
    wb = load_workbook(path_to_file)
    ws = wb.active
    ws.append(list)
    wb.save(path_to_file)
    wb.close
    return None
#top_matrix_to_file(test)


def read_exel_inn(path_to_data = path_to_data):
    list_inn = []
    book = load_workbook(path_to_data, read_only=True)
    sheet = book.active
    for row in sheet.iter_rows(min_col = 1, max_col=1, min_row=1, max_row = sheet.max_row):
        #nim_row минимальное количество строк 
        #max_col максимальное количество столбцов 
        #max_row максильманое колличество строк
        for data in row:
            out = data.value
            if type(out) is int and out not in list_inn:
                list_inn.append(out)
    yield list_inn



''' 
Данный блок проверяет создан ли файл базы данных
если нет, то просто создает его
таким образом мы пытаемся обойти ощибки со стороны 
обработки программой
'''
'''
Созадаем дерикторию
'''
if not os.path.exists(path_to_data_dir):             # Проверяем есть ли ДИРЕКТОРИЯ с таким именем, если нет, создает
    make_dirs(path_to_data_dir)
'''
Создаем базу данных в xlsx формате
'''
if not os.path.exists(path_to_data):                # проверяет существование пути, если нет, вызываем функцию создания
    make_book(path_to_data)                             
                                                    # Сюда нужно еще написать вызов функции которая вызывает окно пользователя и говорит ему
                                                    # что база пустая и необходимо ее пополнить INN для прохождения по ней
if not os.path.exists(path_to_final_exel_file):
    make_book(path_to_final_exel_file)
    top_matrix_to_file(path_to_final_exel_file)


def writer_a_report_file(list, path_to_file = path_to_final_exel_file):
    wb = load_workbook(path_to_file)
    ws = wb.active
    #for row in list:
    ws.append(list)
    wb.save(path_to_file)
    wb.close
    return(print(f'writer_a_report_file >> ok'))
