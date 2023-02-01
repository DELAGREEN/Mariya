#coding=1251
from asyncore import readwrite
from fileinput import filename
import os.path
from re import I
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as load_workbook
from openpyxl.styles.borders import Border, Side
import os
from main import auto_page_pass 
import time


start = time.time()


path_to_home_dir = os.getcwd()                          #пусть распложения main
name_to_dir = path_to_home_dir + '\\data'               #путь к папке
path_to_data = path_to_home_dir + '\\data\\data.xlsx'   #путь к файлу DATA 
test_path = name_to_dir + '\\Итого 01.07.22 (2).xlsx'   #тестовый путь
sourses = "\\sourses"
loads = "\\loads"
loads_dir = sourses + loads


def list_dir():
    path_to_dir = os.listdir(name_to_dir)
    #p = str(*path_to_dir)
    print(f"список список файлов, из {name_to_dir} >> {path_to_dir}")



def work_book():
    '''
    Создаем xlsx файл для записи в него
    '''
    wb = Workbook()
    wb.save(path_to_data)     # сохнаняем с именем лежащей в переменной

def make_dirs():
    '''
    Создаем папки для рабочих 'ДЛЯ УДОБСТВА' процессов
    '''
    os.makedirs(name_to_dir)


''' 
Данный блок проверяет создан ли файл базы данных
если нет, то просто создает его
таким образом мы пытаемся обойти ощибки со стороны 
обработки программой
'''
'''
Созадаем дерикторию
'''
if not os.path.exists(name_to_dir):             # Проверяем есть ли ДИРЕКТОРИЯ с таким именем, если нет, создает
    make_dirs()
'''
Создаем базу данных в xlsx формате
'''
if not os.path.exists(path_to_data):           # проверяет существование пути, если нет, вызываем функцию создания
    work_book()                             
                                                # Сюда нужно еще написать вызов функции которая вызывает окно пользователя и говорит ему
                                                # что база пустая и необходимо ее пополнить INN для прохождения по ней



def read_dataFile2():
    '''
    Построчное чтение xlsx
    '''
    book = load_workbook(path_to_data, read_only=True)
    sheet = book["Sheet"]
    for row in sheet.iter_rows(min_row=1, max_col=1, max_row=999):
        '''
        nim_row минимальное количество строк 
        max_col максимальное количество столбцов 
        max_row максильманое колличество строк
        '''
        for data_list in row:
            #print(data_list)
            data_list = data_list.value
            print(data_list)
            #auto_page_pass(data_list)
#read_dataFile2()

def read_dataFile22():
    '''
    Построчное чтение xlsx
    '''
    wb = Workbook()
    book = load_workbook(test_path, read_only=True)
    #sheet = book["Sheet1"]
    #sheet1 = book.active
    #print(sheet1)
    #print(book.get_sheet_names()) #проверка списка страниц
    i = 2
    sheet = book.active                                                                 #открываем активную страницу
    print(sheet.max_row)                                                                #по сути работает как len строк
    print(sheet.max_column)                                                             #по сути работает как len столбцов
    for row in sheet.iter_rows(min_col = 1,  min_row=i, max_col=9, max_row=i):
        '''
        nim_row минимальное количество строк 
        max_col максимальное количество столбцов 
        max_row максильманое колличество строк
        '''
        for data in row:
            #print(data_list)
            out_data = data.value
            print(out_data)
            #auto_page_pass(data_list)
#read_dataFile22()


def read_exel_inn(path):
    list = []
    i = 1
    book = load_workbook(path, read_only=True)
    sheet = book.active
    for row in sheet.iter_rows(min_col = 1,  min_row=i, max_col=1, max_row = sheet.max_row):
        for data in row:
            out = data.value
            if type(out) is int and out not in list:
                list.append(out)
            else:
                break
    for u in list:
        auto_page_pass(u)
    return list


def append_in_data2(value):
    wb = Workbook()
    ws = wb.active
    #print(value)
    for i in value:
        ws.append(i)
    wb.save(path_to_data)
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


#(read_exel_inn(path_to_data))



append_in_data2(list_in_list(read_exel_inn(test_path)))


end = time.time()

print('Время выполнения: ',end - start)
if __name__ == '__data__':
    
    pass