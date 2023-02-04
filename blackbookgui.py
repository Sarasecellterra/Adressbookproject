#imports
from tkinter import *
from tkinter import PhotoImage
from Standardfieldmod import inputwindow
from viewfieldmod import viewwindow
from Editfield import editfunctionality
import os
import sys
#end imports
#updates the contactlist every 3 seconds to ensure it remains up to date

def main():

    window=Tk()#mainloop

    #lists the filepath of which the foldder storage is contained, which has the user created 
    files = [f for f in os.listdir() if os.path.isfile(f)]
    storagepath=os.path.join(os.getcwd(), "Storage")

    #lists the contents of the folder: storage
    storagecontents=os.listdir(storagepath)

    #once selected an item can be found in the storage folder using this function, then deleted
    def deleteselected():
        tobedeleted=contactlist.get(contactlist.curselection())
        subfolder = "Storage"
        file = tobedeleted
        deletedfilelocation=os.path.join(subfolder, file)
        os.remove(deletedfilelocation)

    def updatelist():
        window.destroy()
        main()

    #window options
    window.geometry("806x792")
    window.config(bg="black")

    #seperates the text module "yourcontacthere" using a black border
    seperatorone=Frame(window, bg="#3d3d3d", width=618, height=60, bd=4, relief=SOLID)
    seperatorone.grid(row=1, column=1)

    #your contact here text
    yourcontacthere=Label(window, text="Your contacts:", font="helvetica 19", bg="#3d3d3d", fg="white")
    yourcontacthere.grid(row=1, column=1)

    #framework for logo, Koye when youre done making it youll have to install it here. he didnt, I ended up doing it-tom
    logo=PhotoImage(file="Blackedbook(1).png")
    logospace=Label(image=logo)
    logospace.grid(row=1, column=0, columnspan=10, sticky=W, padx=10)

    #add a new contact with this code
    newcontact=Button(window, text="Add new contact", height=11, width=25, bd=4, relief=SOLID, command=inputwindow, bg="#3d3d3d", fg="white")
    newcontact.grid(row=2, column=2)

    #update existing contact list with this code
    editcontact=Button(window, text="Update contactlist", height=11, width=25, bd=3, relief=SOLID, command=updatelist, bg="#3d3d3d", fg="white")
    editcontact.grid(row=4, column=2)

    #view existing contacts with this code
    viewcontact=Button(window, text="View details on selected contact", height=10, width=25, bd=4, relief=SOLID, command=viewwindow, bg="#3d3d3d", fg="white")
    viewcontact.grid(row=3, column=2)

    #exit the program with this code
    exitbutton=Button(window, text="Exit", height=3, width=25, borderwidth=4, relief=SOLID, command=window.quit, bg="#3d3d3d", fg="white")
    exitbutton.grid(row=1, column=2)

    #delete a contact with this code
    deletebutton=Button(window, text="Delete contact", height=6, width=25, borderwidth=4, relief= SOLID, command=deleteselected, bg="#3d3d3d", fg="white")
    deletebutton.grid(row=5, column=2)

    editbutton=Button(window, text="Edit contact", height=6, width=25, borderwidth=4, relief=SOLID, command=editfunctionality, bg="#3d3d3d", fg="white")
    editbutton.grid(row=6, column=2)

    #List
    contactlist=Listbox(window, bd=4, height=45, width=101, relief=SOLID, bg="#3d3d3d", fg="white")
    contactlist.grid(row=2, column=1, rowspan=30, sticky=NE)

    def populatelist():
        contactlist.delete(0, END) # Clear the listbox
        for filename in storagecontents:
            contactlist.insert(END, filename)

    #items in the list
    def uponselection(event):
        # Get the selected item index
        selecteditem = contactlist.get(contactlist.curselection())
        with open("varstore.txt", "w") as f:
            f.write(selecteditem)
        
    # Bind the function to the Listbox widget
    contactlist.bind('<<ListboxSelect>>', uponselection)
    
    populatelist()

    #end script
    window.mainloop()
main()