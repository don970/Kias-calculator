#!/bin/python3
class Connections:
    from os import setuid, setgid, system

    def __init__(self):
        self.complete = False
        self.passwd = None
        self.ip = None
        self.port = None
        self.code = None
        self.data = None
        self.url = None

    def sock_send(self, ip, port, data):
        self.ip = ip
        self.port = port
        self.data = data
        print(data)
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, int(port)))
        s.send(data.encode())
        s.close()

    # designed for framework 2.0 application returns true if open false if port closed
    def sock_check(self, ip, port):
        self.ip = ip
        self.port = port
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a = s.connect_ex((ip, int(port)))
        if a == 0:
            s.close()
            return True
        else:
            s.close()
            return False

    def wget(self, url):
        self.url = url
        self.system(f'wget {url}')

    def run(self, ip, port):
        self.ip = ip
        self.port = port
        ss = self.sock_check(str(ip), int(port))  # returns true if the port is open, and false if the port is closed
        if ss:
            return True
        else:
            return False
        pass
