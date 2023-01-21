#imports
from tkinter import *
#end imports
def inputwindow():
    outlinewindow=Tk()

    outlinewindow.overrideredirect(True)

    #window size
    outlinewindow.geometry("482x150")

    #frames for aesthetics:
    #first name:
    Textoutline1=Frame(outlinewindow, width=100, height=30, borderwidth=3, relief=SOLID)
    Textoutline1.grid(row=0, column=0)
    #second name:
    Textoutline2=Frame(outlinewindow, width=100, height=30, borderwidth=3, relief=SOLID)
    Textoutline2.grid(row=1, column=0)
    #phone number:
    Textoutline3=Frame(outlinewindow, width=100, height=30, borderwidth=3, relief=SOLID)
    Textoutline3.grid(row=2, column=0)
    #mobile number:
    Textoutline4=Frame(outlinewindow, width=100, height=30, borderwidth=3, relief=SOLID)
    Textoutline4.grid(row=3, column=0)
    #email adress
    Textoutline5=Frame(outlinewindow, width=100, height=30, borderwidth=3, relief=SOLID)
    Textoutline5.grid(row=4, column=0)

    #if it aint broken dont fix it
    #entry 1 (first name)
    L1=Label(outlinewindow, text="First name:")
    L1.grid(row=0, column=0)
    E1=Entry(outlinewindow, bd=3, relief=SOLID, font="Helvetica 14")
    E1.grid(row=0, column=1)


    #entry 2 (second name)
    L2=Label(outlinewindow, text="Second name:")
    L2.grid(row=1, column=0)
    E2=Entry(outlinewindow, bd=3, relief=SOLID, font="Helvetica 14")
    E2.grid(row=1, column=1)

    #entry 3 (Phone number)
    L3=Label(outlinewindow, text="Phone number:")
    L3.grid(row=2, column=0)
    E3=Entry(outlinewindow, bd=3, relief=SOLID, font="Helvetica 14")
    E3.grid(row=2, column=1)

    #entry 4 (Mobile number)
    L1=Label(outlinewindow, text="Mobile number:")
    L1.grid(row=3, column=0)
    E4=Entry(outlinewindow, bd=3, relief=SOLID, font="Helvetica 14")
    E4.grid(row=3, column=1)

    #entry 5 (Email adress)
    L1=Label(outlinewindow, text="Email adress:")
    L1.grid(row=4, column=0)
    E5=Entry(outlinewindow, bd=3, relief=SOLID, font="Helvetica 14")
    E5.grid(row=4, column=1)

    #Save contact button:
    commitchange=Button(outlinewindow, height=9, width=9, bd=4, relief=SOLID, text="Save contact")
    commitchange.grid(row=0, column=4, rowspan=100)#rowspan is set to arbitrarily huge number to maintain formatting, do not touch or it will destroy the format
    #exit button:
    exitbutton=Button(outlinewindow, height=9, width=9, bd=4, relief=SOLID, text="Exit", command=outlinewindow.destroy)
    exitbutton.grid(row=0, column=5, rowspan=100)#rowspan is set to arbtitrarily huge number to maintain formatting

    #end script
    outlinewindow.mainloop()
inputwindow()