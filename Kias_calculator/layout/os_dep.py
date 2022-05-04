import os
from tkinter import *


class os_check:
    def __init__(self, a, size):
        self.unameVariables = None
        self.android = None
        self.osType()
        if self.android == True:
            self.androids(a)
        else:
            self.pc(a, size)

    def osType(self):
        a = 'ANDROID_DATA' in os.environ
        self.android = a
        self.unameVariables = (str(os.uname()))
        data = {'android': self.android, 'uname_variables': self.unameVariables}
        return data

    def androids(self, a):
        width = a.winfo_screenwidth()
        height = a.winfo_screenheight()
        a.geometry(f'{str(width)}x{str(height)}')

    def pc(self, a, size: str):
        a.geometry(str(size))



