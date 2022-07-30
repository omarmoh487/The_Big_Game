from tkinter import *

x, y = 3, 0


def Water_Jug_GUI():
    window = Tk()
    window.title("water jug")
    window.resizable(False, False)
    window.geometry('700x600+100+0')

    def back():
        window.destroy()
        from T_BG import big_GUI
        big_GUI()

    def check():
        global x
        if x == 2:
            answer.config(text="congrats you solved it !!!", font=('Areal Bold', 12), fg='blue')
        else:
            answer.config(text="    wrong answer", font=('Areal Bold', 12), fg='red')

    def geti():
        global x, y
        try:
            rno = int(rule_entered.get())
            print_check.config(text="↓")
            if rno > 0 and rno < 9:
                if x != 2:
                    if rno == 1:
                        if x < 4:
                            x = 4
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]")
                            print_label.pack()
                    elif rno == 2:
                        if y < 3:
                            y = 3
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 3:
                        if x > 0:
                            x = 0
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 4:
                        if y > 0:
                            y = 0
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 5:
                        if x + y >= 4 and y > 0:
                            y = y - (4 - x)
                            x = 4
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 6:
                        if x + y >= 3 and x > 0:
                            x = x - (3 - y)
                            y = 3
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 7:
                        if x + y <= 4 and y > 0:
                            x = x + y
                            y = 0
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()
                    elif rno == 8:
                        if x + y <= 3 and x > 0:
                            y = x + y
                            x = 0
                            print_label = Label(window, text="["+str(x)+","+str(y)+"]").pack()

            else:
                print_check.config(text="wrong rule try again")
        except ValueError:
            print_check.config(text="You did not enter a number please try again")
    intro = Label(window, text="Welcome to water jug game!!!", font=('Areal Bold', 17)).pack()
    intor1 = Label(window, text="you have 2 jugs: the left one has a capacity of 4 while the right"
                                " one has a capacity of 3", font=('Areal Bold', 13)).pack()
    goal = Label(window, text="your goal is to make the 4 capacity jug into 2 capacity jug using the rules below ↓",
                 font=('Areal Bold', 12), fg='Red').pack()
    L1 = Label(window, text="1- Fill the 4 gallon jug").pack()
    L2 = Label(window, text="2- Fill the 3 gallon jug").pack()
    L3 = Label(window, text="3- Empty the 4 gallon jug").pack()
    L4 = Label(window, text="4- Empty the 3 gallon jug").pack()
    L5 = Label(window, text="5- Empty the 3 gallon jug on the ground Pour water from the 3-gallon jug "
                            "into the 4-gallon jug until the 4-gallon jug is full").pack()
    L6 = Label(window, text="6- Pour water from the 4-gallon jug into the 3-gallon jug "
                            "until the 3-gallon jug is full").pack()
    L7 = Label(window, text="7- Pour all the water from the 3-gallon jug into the 4gallon jug").pack()
    L8 = Label(window, text="8- Pour all the water from the 4-gallon jug into the 3 gallon jug").pack()
    note = Label(window, text="Note: use the check button to see if the answer is right", font=10).pack()
    rule_entered = StringVar()
    rule_entry = Entry(window, textvariable=rule_entered).pack()
    button = Button(window, text="enter", command=geti).pack()
    print_check = Label(window, text="")
    print_check.pack()
    answer = Label(window, text='')
    answer.place(x=120, y=350)
    check_button = Button(window, text="Check", font=('Areal Bold', 13), command=check).place(x=150, y=320)
    back_Button = Button(window, text="←back", command=back).place(x=0, y=0)

    window.mainloop()
