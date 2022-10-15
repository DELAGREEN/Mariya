#coding=1251

import json
import os


#with open ('data.json', 'r') as file:
#    data = json.dump()

Path_in_Data = os.getcwd()
s = "10"


def read_data_file():
    data = open('C:\\Users\\igorm\\source\\repos\\DELAGREEN\\Mariya\\Mariya\\data.txt', 'a+')
    data.write(s + "\n")
    data.close()
    print(s)    
    pass


read_data_file()


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