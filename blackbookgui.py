#imports
from tkinter import *
from PIL import ImageTk, Image
from Standardfieldmod import inputwindow
from viewfieldmod import viewwindow
#end imports


def main():

    window=Tk()#mainloop

    #window options
    window.geometry("808x600")
    window.config(bg="black")

    #seperates the text module "yourcontacthere" using a black border
    seperatorone=Frame(window, bg="#3d3d3d", width=618, height=60, bd=4, relief=SOLID)
    seperatorone.grid(row=1, column=1)

    #your contact here text
    yourcontacthere=Label(window, text="Your contacts:", font="helvetica 19", bg="#3d3d3d", fg="white")
    yourcontacthere.grid(row=1, column=1)

    #add a new contact with this code
    newcontact=Button(window, text="Add new contact", height=11, width=25, bd=4, relief=SOLID, command=inputwindow, bg="#3d3d3d", fg="white")
    newcontact.grid(row=2, column=2)

    #view existing contacts with this code
    viewcontact=Button(window, text="View details on selected contact", height=10, width=25, bd=4, relief=SOLID, command=viewwindow, bg="#3d3d3d", fg="white")
    viewcontact.grid(row=3, column=2)

    #edit existing contacts with this code
    editcontact=Button(window, text="edit selected contact", height=11, width=25, bd=3, relief=SOLID, bg="#3d3d3d", fg="white")
    editcontact.grid(row=4, column=2)

    #exit the program with this code
    exitbutton=Button(window, text="exit", height=3, width=25, borderwidth=4, relief=SOLID, command=window.quit, bg="#3d3d3d", fg="white")
    exitbutton.grid(row=1, column=2)

    #List
    contactlist=Listbox(window, bd=4, height=32, width=101, relief=SOLID, bg="#3d3d3d", fg="white")
    contactlist.grid(row=2, column=1, rowspan=30, sticky=NE)

    #scrollbar
    scrollbar=Scrollbar(window, orient=VERTICAL, command=contactlist.yview)
    contactlist.config(yscrollcommand=scrollbar.set)

    #arbitrary fill data for list please delete once done
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 1")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")
    contactlist.insert(END, "item 3")

    selecteditem=contactlist.get(ACTIVE)

    #end script
    window.mainloop()
main()