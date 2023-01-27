#coding=1251
from asyncore import readwrite
from fileinput import filename
import os.path
from re import I
from openpyxl.workbook import Workbook as Workbook
from openpyxl.reader.excel import load_workbook as load_workbook
import os
from main import auto_page_pass 


path_to_home_dir = os.getcwd()                          #����� ����������� main
name_to_dir = path_to_home_dir + '\\data'               #���� � �����
path_to_data = path_to_home_dir + '\\data\\data.xlsx'   #���� � ����� DATA 

test_path = name_to_dir + '\\����� 01.07.22 (2).xlsx'   #�������� ����


def list_dir():
    path_to_dir = os.listdir(name_to_dir)
    #p = str(*path_to_dir)
    print(f"������ ������ ������, �� {name_to_dir} >> {path_to_dir}")
list_dir()



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
    ��������
    '''


    from openpyxl.styles.borders import Border, Side
    #from openpyxl import Workbook
    
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thick'))  #������ ������
    
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