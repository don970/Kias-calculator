class Tkinter_Layouts:
    # use for framewidget
    # create a var and set equal to
    def __init__(self, framewidget: object):
        framewidget.place(relheight=1.0, relwidth=1.0)
        self.complete = None
        pass

    def widget(self, what: object, relh: float, relw: float, x1: int, y1: int) -> bool:
        what.place(relheight=relh, relwidth=relw, x=x1, y=y1)
        self.complete = True
        if self.complete:
            return True
        return False

    def relwidget(self, what: object, relh: float, relw: float, x1: float, y1: float) -> bool:
        what.place(relheight=relh, relwidth=relw, relx=x1, rely=y1)
        self.complete = True
        if self.complete:
            return True
        return False

    def textarea(self, what: object, relh: float, relw: float) -> bool:
        what.place(relheight=relh, relwidth=relw, x=0, y=20)
        self.complete = True
        if self.complete:
            return True
        return False
        pass

    # for testing purposes
    def pack(self, what: object) -> bool:
        what.pack()
        self.complete = True
        if self.complete:
            return True
        return False
        pass
