#coding=1251


import tkinter as tk 
from tkinter import messagebox



window = tk.Tk()
window.title('�����')
window.geometry('400x300+650+300')
window.resizable(width=False, height=False)
window['bg'] = 'gray'

butn = tk.Button(window, text='��������', font='Arial 15 bold', fg='black', bg='gray')
butn.place(x=100, y = 100)
lbPath = tk.Label(window, text='������� INN',  )

window.mainloop()