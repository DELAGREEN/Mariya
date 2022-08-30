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
        tk.messagebox.showinfo('Ошибочка вышла!!!', ("Поле для ввода не может быть пустым."))
        pass



def EnterClick(A):   # A - это заглушка, не понятно мне пока почему, но работает и так =_=
    AddInn()
    pass




window = tk.Tk()                                # Создает окно
window.title('Мария')                           # Наименование окна
window.geometry('400x300+650+300')              # Размеры окна
window.resizable(width=False, height=False)     # Пока не понял для чего
window['bg'] = 'gray'                           # Цвет земли окна или как её называют еще фон

btn_add_inn = tk.Button(window, text='Добавить', command=AddInn, font='Arial 15 bold', fg='black', bg='gray')       # Добавляет кнопку - Добавить
btn_add_inn.place(x=10, y = 100)                                                                                    # Расположение элемента
window.bind('<Return>', EnterClick)                                                                                 # Добавляет функцию срабатывания кнопки - Добавить - натино через клавишу - Enter
lbPath = tk.Label(window, text='Введите INN', font='Arial 15 bold', fg='black', bg='gray')                          # Любой текст
lbPath.place(x=10, y=5)

Enter_Text_Inn = tk.Entry(fg='black', width = 50)                                                                   # Поле ввода                                                                
Enter_Text_Inn.place(x=10, y=40)

window.mainloop()                                                                                                   # Ну соответственно луп окна, что бы не закрывалось    