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
    ������� xlsx ���� ��� ������ � ����
    '''
    wb = Workbook()
    wb.save(name_from_data)     # ��������� � ������ ������� � ����������
    pass                        # ������ � �������

def make_dirs():
    '''
    ������� ����� ��� ������� '��� ��������' ���������
    '''
    os.makedirs(name_to_dir)


#def append_data(cell.value):
#    return(data_list.append = cell.value)



   


# ������ ���� ��������� ������ �� ���� ���� ������
# ���� ���, �� ������ ������� ���
# ����� ������� �� �������� ������ ������ �� ������� ��������� 
# ����������

if not os.path.exists(name_to_dir):             # ��������� ���� �� ���������� � ����� ������, ���� ���, �������
    make_dirs()

if not os.path.exists(name_from_data):           # ��������� ������������� ����, ���� ���, �������� ������� ��������
    work_book()                             
                                                # ���� ����� ��� �������� ����� ������� ������� �������� ���� ������������ � ������� ���
                                                # ��� ���� ������ � ���������� �� ��������� INN ��� ����������� �� ���



#def read_dataFile():
#    '''
#    ���������� ������ xlsx
#
#    �.� ���� ������������� ����
#    ���� ������ ������ ���������� None
#    ����� ������������ ��� ����, � ����� � ��� :D
#    '''
#    book = load_workbook(name_from_data, read_only=True)
#    print(book)
#    sheet = book["Sheet"]
#    for row in sheet.iter_rows():                          # ������ ���������� 
#        for cell in row:                                   # ������ ����� �� �������
#            print(cell.value)
#



def read_dataFile2():
    #import Mariya
    '''
    ���������� ������ xlsx

    �.� ���� ������������� ����
    ���� ������ ������ ���������� None
    ����� ������������ ��� ����, � ����� � ��� :D
    '''
    book = load_workbook(name_from_data, read_only=True)
    sheet = book["Sheet"]
    for row in sheet.iter_rows():                               # ������ ���������� 
        for data_list in row:                                   # ������ ����� �� �������
            data_list = data_list.value
            dataList.append(data_list)
            print(dataList)
            #Mariya.auto_page_pass(data_list)                    # �������� �������� � Main ��� ����������� �������������
        return(data_list)

                     


#read_dataFile()
read_dataFile2()



#
#def exampe():
#    """
#     ������� xlsx ���� ��� ��� ������ � ����
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