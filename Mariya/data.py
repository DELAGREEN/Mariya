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


path_to_home_dir = os.getcwd()                          #����� ����������� main
name_to_dir = path_to_home_dir + '\\data'               #���� � �����
path_to_data = path_to_home_dir + '\\data\\data.xlsx'   #���� � ����� DATA 
test_path = name_to_dir + '\\����� 01.07.22 (2).xlsx'   #�������� ����
sourses = "\\sourses"
loads = "\\loads"
loads_dir = sourses + loads


def list_dir():
    path_to_dir = os.listdir(name_to_dir)
    #p = str(*path_to_dir)
    print(f"������ ������ ������, �� {name_to_dir} >> {path_to_dir}")



def work_book():
    '''
    ������� xlsx ���� ��� ������ � ����
    '''
    wb = Workbook()
    wb.save(path_to_data)     # ��������� � ������ ������� � ����������

def make_dirs():
    '''
    ������� ����� ��� ������� '��� ��������' ���������
    '''
    os.makedirs(name_to_dir)


''' 
������ ���� ��������� ������ �� ���� ���� ������
���� ���, �� ������ ������� ���
����� ������� �� �������� ������ ������ �� ������� 
��������� ����������
'''
'''
�������� ����������
'''
if not os.path.exists(name_to_dir):             # ��������� ���� �� ���������� � ����� ������, ���� ���, �������
    make_dirs()
'''
������� ���� ������ � xlsx �������
'''
if not os.path.exists(path_to_data):           # ��������� ������������� ����, ���� ���, �������� ������� ��������
    work_book()                             
                                                # ���� ����� ��� �������� ����� ������� ������� �������� ���� ������������ � ������� ���
                                                # ��� ���� ������ � ���������� �� ��������� INN ��� ����������� �� ���



def read_dataFile2():
    '''
    ���������� ������ xlsx
    '''
    book = load_workbook(path_to_data, read_only=True)
    sheet = book["Sheet"]
    for row in sheet.iter_rows(min_row=1, max_col=1, max_row=999):
        '''
        nim_row ����������� ���������� ����� 
        max_col ������������ ���������� �������� 
        max_row ������������ ����������� �����
        '''
        for data_list in row:
            #print(data_list)
            data_list = data_list.value
            print(data_list)
            #auto_page_pass(data_list)
#read_dataFile2()

def read_dataFile22():
    '''
    ���������� ������ xlsx
    '''
    wb = Workbook()
    book = load_workbook(test_path, read_only=True)
    #sheet = book["Sheet1"]
    #sheet1 = book.active
    #print(sheet1)
    #print(book.get_sheet_names()) #�������� ������ �������
    i = 2
    sheet = book.active                                                                 #��������� �������� ��������
    print(sheet.max_row)                                                                #�� ���� �������� ��� len �����
    print(sheet.max_column)                                                             #�� ���� �������� ��� len ��������
    for row in sheet.iter_rows(min_col = 1,  min_row=i, max_col=9, max_row=i):
        '''
        nim_row ����������� ���������� ����� 
        max_col ������������ ���������� �������� 
        max_row ������������ ����������� �����
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
    ������� ������ � ������ list[list[]]
    '''
    total_list = []
    for i in list:
        u = [i]
        total_list.append(u)
    return total_list
 

def add_style():
    '''
    ��������
    '''
    #from openpyxl import Workbook
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thick'))  #������ ������
    wb = Workbook()
    ws = wb.active
    ws.cell(row=3, column=2).border = thin_border
    wb.save('border_test.xlsx')


#(read_exel_inn(path_to_data))



append_in_data2(list_in_list(read_exel_inn(test_path)))


end = time.time()

print('����� ����������: ',end - start)
if __name__ == '__data__':
    
    pass