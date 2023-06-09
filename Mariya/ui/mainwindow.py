from tkinter import Tk, Button
from singleton import Singleton
from eqswindow import Extra
from progressbar import ProgressBar


class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()



        self.button = Button(self, text='Open eqs window', command=self.create_window_eqs)
        self.button.pack(expand=True)


    def create_window_eqs(self):
        global extraWindow
        extraWindow = Extra()

    def create_progressbar(self):
        global extraWindow
        extraWindow = ProgressBar()
    

    def __init__(self):
        print('calling from __init__')