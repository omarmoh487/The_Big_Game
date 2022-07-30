from tkinter import *
from Snake import snake_GUI
from TOH import toh_GUI
from Water_Jug import Water_Jug_GUI


def big_GUI():
    def snake_G():
        big_Gui.destroy()
        snake_GUI()

    def TOH_G():
        big_Gui.destroy()
        toh_GUI()

    def Water_G():
        big_Gui.destroy()
        Water_Jug_GUI()

    big_Gui = Tk()
    big_Gui.geometry('500x500+420+100')
    big_Gui.resizable(False, False)
    big_Gui.title('The Big Game')

    label_name = Label(big_Gui, text="Welcome To The Big GAME !!!!", font=('Areal Bold', 22)).pack()
    label_select = Label(big_Gui, text="please select a game :)", font=('Areal Bold', 15)).pack(pady=12)

    snake_button = Button(big_Gui, text="Snake", font=('Areal Bold', 11), command=snake_G).place(x=80, y=250)
    TOH_button = Button(big_Gui, text="Tower of Hanoi", font=('Areal Bold', 11), command=TOH_G).place(x=185, y=250)
    WJ_button = Button(big_Gui, text="Water Jug", font=('Areal Bold', 11), command=Water_G).place(x=350, y=250)

    big_Gui.mainloop()


big_GUI()  # For Starting The GUI
