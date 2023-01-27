#coding=1251
from asyncore import readwrite
from fileinput import filename
import os.path
from re import I
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as load_workbook
import os
from main import auto_page_pass 


path_to_home_dir = os.getcwd()                          #пусть распложения main
name_to_dir = path_to_home_dir + '\\data'               #путь к папке
path_to_data = path_to_home_dir + '\\data\\data.xlsx'   #путь к файлу DATA 

test_path = name_to_dir + '\\Итого 01.07.22 (2).xlsx'   #тестовый путь


def list_dir():
    path_to_dir = os.listdir(name_to_dir)
    #p = str(*path_to_dir)
    print(f"список список файлов, из {name_to_dir} >> {path_to_dir}")
list_dir()



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
read_dataFile22()


def append_in_data():
    wb = Workbook()
    i = 1
    y = 1
    u = 1
    data = [[i, str(y)],
           [y, i, u], 
           [u]]

    for r in data:
        wb.active.append(r)
        i,y,u + 1
        print(data)
    #wb.active.auto_filter.ref = "A1:C7"
    #wb.active.add_filter_column(0.)
    wb.save("data.xlsx")
    pass
#append_in_data()





def odd_in():
    '''
    Работает
    '''


    from openpyxl.styles.borders import Border, Side
    #from openpyxl import Workbook
    
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thick'))  #жирная полоса
    
    wb = Workbook()
    ws = wb.active
   
    # property cell.border should be used instead of cell.style.border
    ws.cell(row=3, column=2).border = thin_border
    wb.save('border_test.xlsx')
    
odd_in()





def modify_data(record_data):
    
    pass
#def data_inject():
#    
#    return inn