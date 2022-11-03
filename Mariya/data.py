#coding=1251
from asyncore import readwrite
from fileinput import filename
import os.path
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as load_workbook
import os



home_dir = os.getcwd()
name_from_data = home_dir + '\\data\\data.xlsx'
name_to_dir = home_dir + '\\data'

dataList = []


def work_book():
    '''
    Создаем xlsx файл для записи в него
    '''
    wb = Workbook()
    wb.save(name_from_data)     # сохнаняем с именем лежащей в переменной
    pass                        # проход в пустоту

def make_dirs():
    '''
    Создаем папки для рабочих 'ДЛЯ УДОБСТВА' процессов
    '''
    os.makedirs(name_to_dir)


#def append_data(cell.value):
#    return(data_list.append = cell.value)



   


# Данный блок проверяет создан ли файл базы данных
# Если нет, то просто создает его
# Таким образом мы пытаемся обойти ощибки со стороны обработки 
# Программой

if not os.path.exists(name_to_dir):             # Проверяем есть ли ДИРЕКТОРИЯ с таким именем, если нет, создаем
    make_dirs()

if not os.path.exists(name_from_data):           # проверяет существование пути, если нет, вызываем функцию создания
    work_book()                             
                                                # Сюда нужно еще написать вызов функции которая вызывает окно пользователя и говорит ему
                                                # что база пустая и необходимо ее пополнить INN для прохождения по ней



#def read_dataFile():
#    '''
#    Построчное чтение xlsx
#
#    П.С Есть занимательный факт
#    если строка пустая возвращает None
#    Можно использовать как фичу, а можно и нет :D
#    '''
#    book = load_workbook(name_from_data, read_only=True)
#    print(book)
#    sheet = book["Sheet"]
#    for row in sheet.iter_rows():                          # чтение построчное 
#        for cell in row:                                   # чтение строк по клеткам
#            print(cell.value)
#



def read_dataFile2():
    #import Mariya
    '''
    Построчное чтение xlsx

    П.С Есть занимательный факт
    если строка пустая возвращает None
    Можно использовать как фичу, а можно и нет :D
    '''
    book = load_workbook(name_from_data, read_only=True)
    sheet = book["Sheet"]
    for row in sheet.iter_rows():                               # чтение построчное 
        for data_list in row:                                   # чтение строк по клеткам
            data_list = data_list.value
            dataList.append(data_list)
            print(dataList)
            #Mariya.auto_page_pass(data_list)                    # Передаем значение в Main для дальнейшего использования
        return(data_list)

                     


#read_dataFile()
read_dataFile2()



#
#def exampe():
#    """
#     Создаем xlsx файл для для записи в него
#
#    """
#    book = openpyxl.Workbook()
#    book.remove(book.active)
#
#def json_data_input():
#
#    return
#
#
#
#def data_inject():
#    inn = ['5260477034']
#    return inn
#