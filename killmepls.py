import pygubu
from tkinter import *
from tkinter import ttk
import numpy as np


class hi:

    def __init__(self, master):
        self.frame = 'startpage'
        self.builder = builder = pygubu.Builder()

        builder.add_from_file('app.ui')

        self.mainwindow = builder.get_object(self.frame, master)

        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def to_sqrt(self):
        builder2 = pygubu.Builder()
        builder2.add_from_file('app.ui')
        top3 = Toplevel(self.mainwindow)
        frame3 = builder2.get_object('sqrtr', top3)
        builder2.connect_callbacks(self)


if __name__ == '__main__':
    root = Tk()
    app = hi(root)
    app.run()
