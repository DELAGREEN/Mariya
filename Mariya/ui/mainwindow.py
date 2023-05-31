from tkinter import Tk
from singleton import Singleton


class Window(Tk, Singleton):
    def init(self):
        print('calling from init')
        super().__init__()

    def __init__(self):
        print('calling from __init__')