from tkinter import *


class Functions:
    from os import system

    def __init__(self):
        self.complete = False
        self.ip = None
        self.port = None

    def nc(self, ip, port):
        self.ip = ip
        self.port = port
        try:
            self.system(f"xterm -e 'nc -zv {ip} {port} &> out.txt'")
            a = open('out.txt', 'r')
            a1 = a.read()
            a2 = "succeeded!" in a1
            if a2:
                self.complete = True
                return True
            else:
                return False
        except OSError as e:
            print(e)
            return False

    def tk_end(self, what):
        Tk.destroy(what)
        self.complete = True
        a = True
        if a:
            self.complete = True
            return True
        else:
            return False

    def runas(self, python_code: str):
        self.system(f'sudo python -c "{python_code}"')
