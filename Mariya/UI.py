#coding=1251

import tkinter as tk 
from tkinter import messagebox


def AddInn():
    value = Enter_Text_Inn.get()
    if value != '':                                                  
        with open ('dataInn.txt', 'a+', encoding = "utf-8") as file:
            file.write(value + '\n')
        Enter_Text_Inn.delete(0, 'end')

    else:
        tk.messagebox.showinfo('�������� �����!!!', ("���� ��� ����� �� ����� ���� ������."))
        pass



def EnterClick(Enter):                              # A - ��� ��������, �� ������� ��� ���� ������, �� �������� � ��� =_=
    AddInn()
    pass




def windows():

    windows.quit()
    pass

window = tk.Tk()                                # ������� ����
window.title('�����')                           # ������������ ����
window.geometry('400x300+650+300')              # ������� ����
#window.resizable(width=False, height=False)     # ������������ ������� �����
window['bg'] = 'gray'                           # ���� ����� ���� ��� ��� � �������� ��� ���
    
btn_add_inn = tk.Button(window, text='��������', command=AddInn, font='Arial 15 bold', fg='black', bg='gray')       # ��������� ������ - ��������
btn_add_inn.grid(row=3, column=3)
btn_add_inn.place(x=10, y = 100)                                                                                    # ������������ ��������
window.bind('<Return>', EnterClick)                                                                                 # ��������� ������� ������������ ������ - �������� - ������ ����� ������� - Enter
lbPath = tk.Label(window, text='������� INN', font='Arial 15 bold', fg='black', bg='gray')                          # ����� �����
lbPath.place(x=10, y=5)
    
Enter_Text_Inn = tk.Entry(fg='black', width = 50)                                                                   # ���� �����                                                                
Enter_Text_Inn.place(x=10, y=40)
    
    
    
    
    
btn_add_inn = tk.Button(window, text='�������', font='Arial 15 bold', fg='black', bg='gray')             # ��������� ������ - �������
btn_add_inn.place(x=10, y = 200)  
    
window.protocol('WM_DELETE_WINDOW', windows)
    
window.mainloop()                                                                                                   # �� �������������� ��� ����, ��� �� �� �����������    
 