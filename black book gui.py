#imports
from tkinter import *
from PIL import ImageTk, Image
#end imports

window=Tk()#mainloop

#fuck it we ball
def opensecondwindow():
    from Standardfieldmod import inputwindow

#window options
window.geometry("808x600")
window.config(bg="black")

#seperates the text module "yourcontacthere" using a black border
seperatorone=Frame(window, bg="white", width=618, height=60, bd=4, relief=SOLID)
seperatorone.grid(row=1, column=1)

#your contact here text
yourcontacthere=Label(window, text="Your contacts:", bg="white", font=("Helvetica", 19))
yourcontacthere.grid(row=1, column=1)

#add a new contact with this code
newcontact=Button(window, text="Add new contact", height=11, width=25, bd=4, relief=SOLID, command=opensecondwindow)
newcontact.grid(row=2, column=2)

#view existing contacts with this code
viewcontact=Button(window, text="view details on selected contact", height=10, width=25, bd=4, relief=SOLID)
viewcontact.grid(row=3, column=2)

#edit existing contacts with this code
editcontact=Button(window, text="edit selected contact", height=11, width=25, bd=3, relief=SOLID)
editcontact.grid(row=4, column=2)

#exit the program with this code
exitbutton=Button(window, text="exit", height=3, width=25, borderwidth=4, relief=SOLID, command=window.quit)
exitbutton.grid(row=1, column=2)

#module for adding new contacts.


#List
contactlist=Listbox(window, bd=4, height=32, width=101, relief=SOLID)
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