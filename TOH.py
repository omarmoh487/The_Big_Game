from tkinter import *


def toh_GUI():
    def back():
        window.destroy()
        from T_BG import big_GUI
        big_GUI()

    def tower(n, start, end, middle):   # this function is used to move the discs
        if n == 1:
            # in case of 1 disc it is moved from the first tower to the last tower
            label2 = Label(window, text="Move %i from tower %s to tower %s" % (n, start, end),
                           font=("Arial Bold", 20), bg="Pink", height=1).pack()
        else:
            tower(n-1, start, middle, end)
            label2 = Label(window, text="Move %i from tower %s to tower %s" % (n, start, end),
                           font=("Arial Bold", 20), bg="Pink", height=1).pack()
            tower(n-1, middle, end, start)

    def getting():
        try:
            x = int(number_entered.get())
            if x > 0 and x <= 4:
                tower(x, "A", "C", "B")
            else:
                check.config(text="you either entered a number less than or equal zero or greater than 4")
        except ValueError:
            check.config(text="you did not enter a number please try again")

    window = Tk()
    window.geometry('500x700+420+0')
    window.title('Tower of Hanoi')
    window.configure(background='Pink')
    number_entered = StringVar()

    intro = Label(window, text="You have 3 towers A, B, and C", bg='Gold').pack()
    intro2 = Label(window, text="the goal of the game is to show the minimum number of moves to be solved",
                   bg='Gold').pack()
    num_of_rings_Label = Label(window, text="Enter number of rings bigger than 0 and less than 5 in the text below",
                               font=10, fg='Red', bg='Gold').pack()
    num_Entry = Entry(window, textvariable=number_entered)
    num_Entry.pack()

    but = Button(window, text="start", command=getting).pack()

    backButton = Button(window, text="←back", command=back).place(x=0, y=0)
    check = Label(window, text="", bg='Pink')
    check.pack()

    window.mainloop()
