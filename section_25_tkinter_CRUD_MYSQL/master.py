from tkinter import *
from window_crud import *

def main():
    root = Tk()
    root.wm_title("CRUD MYSQL")
    app = WindowCrud(root)
    app.mainloop()

if __name__ == '__main__':
    main()