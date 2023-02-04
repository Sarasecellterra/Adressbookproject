#imports
from tkinter import *
import os
#end imports

def viewwindow():

    outlinewindow3=Tk()

    #change to true on release, false when debugging.
    outlinewindow3.overrideredirect(False)

    #window size
    outlinewindow3.geometry("565x215")

    #opens the file that blackbookgui writes the name to and stores the name of the file in "filename"
    with open("varstore.txt", "r") as file:
        filename = file.read().strip()
        print(filename)

    storage="Storage"

    filedirectory=os.path.join(storage, filename)
    with open(filedirectory, "r") as f:
        chosen=f.readlines()
    
    line1=chosen[0]
    line2=chosen[1]
    line3=chosen[2]
    line4=chosen[3]
    line5=chosen[4]
    f.close()

    #used to make the borders around the text (normal text borders dont work without iffy formatting)
    contentoutline1=Frame(outlinewindow3, width=130, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    contentoutline1.grid(row=0, column=0)

    contentoutline2=Frame(outlinewindow3, width=130, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    contentoutline2.grid(row=1, column=0)

    contentoutline3=Frame(outlinewindow3, width=130, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    contentoutline3.grid(row=2, column=0)

    contentoutline4=Frame(outlinewindow3, width=130, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    contentoutline4.grid(row=3, column=0)

    contentoutline5=Frame(outlinewindow3, width=130, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    contentoutline5.grid(row=4, column=0)

    #helps the user figure out what each textbox is reffering to.
    textdefiner1=Label(outlinewindow3, font="Helvetica 12", text="First Name:", bg="#3d3d3d", fg="white")
    textdefiner1.grid(row=0, column=0)

    textdefiner2=Label(outlinewindow3, font="helvetica 12", text="Second Name:", bg="#3d3d3d", fg="white")
    textdefiner2.grid(row=1, column=0)

    textdefiner3=Label(outlinewindow3, font="helvetica 12", text="Phone Number:", bg="#3d3d3d", fg="white")
    textdefiner3.grid(row=2, column=0)

    textdefiner4=Label(outlinewindow3, font="helvetica 12", text="Mobile Number:", bg="#3d3d3d", fg="white")
    textdefiner4.grid(row=3, column=0)

    textdefiner5=Label(outlinewindow3, font="helvetica 12", text="Email Adress:", bg="#3d3d3d", fg="white")
    textdefiner5.grid(row=4, column=0)

    #Serves to make borders around the contact data
    outputoutline1=Frame(outlinewindow3, width=352, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    outputoutline1.grid(row=0, column=1)

    outputoutline2=Frame(outlinewindow3, width=352, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    outputoutline2.grid(row=1, column=1)
    
    outputoutline3=Frame(outlinewindow3, width=352, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    outputoutline3.grid(row=2, column=1)

    outputoutline4=Frame(outlinewindow3, width=352, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    outputoutline4.grid(row=3, column=1)

    outputoutline5=Frame(outlinewindow3, width=352, height=43, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    outputoutline5.grid(row=4, column=1)

    #Serves to store and display the loaded data from the selected contact.
    #katie when implementing your code, port over the variables into the text modules, that way it should auto display into them
    outputlabel1=Label(outlinewindow3, font="helvetica 9", text=line1, bg="#3d3d3d", fg="white")
    outputlabel1.grid(row=0, column=1)

    outputlabel2=Label(outlinewindow3, font="helvetica 9", text=line2, bg="#3d3d3d", fg="white")
    outputlabel2.grid(row=1, column=1)

    outputlabel3=Label(outlinewindow3, font="helvetica 9", text=line3, bg="#3d3d3d", fg="white")
    outputlabel3.grid(row=2, column=1)

    outputlabel4=Label(outlinewindow3, font="helvetica 9", text=line4, bg="#3d3d3d", fg="white")
    outputlabel4.grid(row=3, column=1)

    outputlabel5=Label(outlinewindow3, font="helvetica 9", text=line5, bg="#3d3d3d", fg="white")
    outputlabel5.grid(row=4, column=1)

    #exit button
    exitbutton=Button(outlinewindow3, height=13, width=9, bd=7, relief=SOLID, text="Exit", command=outlinewindow3.destroy, bg="#3d3d3d", fg="white")
    exitbutton.grid(row=0, column=5, rowspan=100)#rowspan is set to arbtitrarily huge number to maintain formatting

    #end main loop
    outlinewindow3.mainloop()

if __name__ == "__main__":
    viewwindow()