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



def EnterClick(Enter):                              # A - это заглушка, не понятно мне пока почему, но работает и так =_=
    AddInn()
    pass




def windows():

    windows.quit()
    pass

window = tk.Tk()                                # Создает окно
window.title('Мария')                           # Наименование окна
window.geometry('400x300+650+300')              # Размеры окна
#window.resizable(width=False, height=False)     # ограничивает размеры рамки
window['bg'] = 'gray'                           # Цвет земли окна или как её называют еще фон
    
btn_add_inn = tk.Button(window, text='Добавить', command=AddInn, font='Arial 15 bold', fg='black', bg='gray')       # Добавляет кнопку - Добавить
btn_add_inn.grid(row=3, column=3)
btn_add_inn.place(x=10, y = 100)                                                                                    # Расположение элемента
window.bind('<Return>', EnterClick)                                                                                 # Добавляет функцию срабатывания кнопки - Добавить - натино через клавишу - Enter
lbPath = tk.Label(window, text='Введите INN', font='Arial 15 bold', fg='black', bg='gray')                          # Любой текст
lbPath.place(x=10, y=5)
    
Enter_Text_Inn = tk.Entry(fg='black', width = 50)                                                                   # Поле ввода                                                                
Enter_Text_Inn.place(x=10, y=40)
    
    
    
    
    
btn_add_inn = tk.Button(window, text='Парсить', font='Arial 15 bold', fg='black', bg='gray')             # Добавляет кнопку - Парсера
btn_add_inn.place(x=10, y = 200)  
    
window.protocol('WM_DELETE_WINDOW', windows)
    
window.mainloop()                                                                                                   # Ну соответственно луп окна, что бы не закрывалось    
 