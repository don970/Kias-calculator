class Errors:
    from tkinter.messagebox import showerror

    def __int__(self, error: str, data: str, tk: bool):
        self.main(error, data, tk)
        pass

    def main(self, data: str, error: str, tk: bool):
        if data == 'os':
            if not tk:
                print(error)
            else:
                self.showerror(title='OS Error',
                               message=str(error)
                               )
