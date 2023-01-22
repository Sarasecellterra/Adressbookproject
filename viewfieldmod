#imports
from tkinter import *
#end imports

def viewwindow():

    outlinewindow3=Tk()

    #change to true on release, false when debugging.
    outlinewindow3.overrideredirect(False)

    #window size
    outlinewindow3.geometry("558x150")

    #used to make the borders around the text (normal text borders dont work without iffy formatting)
    contentoutline1=Frame(outlinewindow3, width=130, height=30, borderwidth=3, relief=SOLID)
    contentoutline1.grid(row=0, column=0)

    contentoutline2=Frame(outlinewindow3, width=130, height=30, borderwidth=3, relief=SOLID)
    contentoutline2.grid(row=1, column=0)

    contentoutline3=Frame(outlinewindow3, width=130, height=30, borderwidth=3, relief=SOLID)
    contentoutline3.grid(row=2, column=0)

    contentoutline4=Frame(outlinewindow3, width=130, height=30, borderwidth=3, relief=SOLID)
    contentoutline4.grid(row=3, column=0)

    contentoutline5=Frame(outlinewindow3, width=130, height=30, borderwidth=3, relief=SOLID)
    contentoutline5.grid(row=4, column=0)

    #helps the user figure out what each textbox is reffering to.
    textdefiner1=Label(outlinewindow3, font="Helvetica 12", text="First name")
    textdefiner1.grid(row=0, column=0)

    textdefiner2=Label(outlinewindow3, font="helvetica 12", text="Second name")
    textdefiner2.grid(row=1, column=0)

    textdefiner3=Label(outlinewindow3, font="helvetica 12", text="Phone number")
    textdefiner3.grid(row=2, column=0)

    textdefiner4=Label(outlinewindow3, font="helvetica 12", text="Mobile number")
    textdefiner4.grid(row=3, column=0)

    textdefiner5=Label(outlinewindow3, font="helvetica 12", text="Email adress")
    textdefiner5.grid(row=4, column=0)

    #Serves to make borders around the contact data
    outputoutline1=Frame(outlinewindow3, width=352, height=30, borderwidth=3, relief=SOLID)
    outputoutline1.grid(row=0, column=1)

    outputoutline2=Frame(outlinewindow3, width=352, height=30, borderwidth=3, relief=SOLID)
    outputoutline2.grid(row=1, column=1)

    outputoutline3=Frame(outlinewindow3, width=352, height=30, borderwidth=3, relief=SOLID)
    outputoutline3.grid(row=2, column=1)

    outputoutline4=Frame(outlinewindow3, width=352, height=30, borderwidth=3, relief=SOLID)
    outputoutline4.grid(row=3, column=1)

    outputoutline5=Frame(outlinewindow3, width=352, height=30, borderwidth=3, relief=SOLID)
    outputoutline5.grid(row=4, column=1)

    #Serves to store and display the loaded data from the selected contact.
    #katie when implementing your code, port over the variables into the text modules, that way it should auto display into them
    outputlabel1=Label(outlinewindow3, font="helvetica 12", text="f")
    outputlabel1.grid(row=0, column=1, sticky=W)

    outputlabel2=Label(outlinewindow3, font="helvetica 12", text="f")
    outputlabel2.grid(row=1, column=1, sticky=W)

    outputlabel3=Label(outlinewindow3, font="helvetica 12", text="f")
    outputlabel3.grid(row=2, column=1, sticky=W)

    outputlabel4=Label(outlinewindow3, font="helvetica 12", text="f")
    outputlabel4.grid(row=3, column=1, sticky=W)

    outputlabel5=Label(outlinewindow3, font="helvetica 12", text="f")
    outputlabel5.grid(row=4, column=1, sticky=W)

    #exit button
    exitbutton=Button(outlinewindow3, height=9, width=9, bd=4, relief=SOLID, text="Exit", command=outlinewindow3.destroy)
    exitbutton.grid(row=0, column=5, rowspan=100)#rowspan is set to arbtitrarily huge number to maintain formatting

    #end main loop
    outlinewindow3.mainloop()
    
if __name__ == "__main__":
    viewwindow()
