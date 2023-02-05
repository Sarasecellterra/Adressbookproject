#imports
from tkinter import *
import shutil
import os
#end imports

def inputwindow():

    outlinewindow2=Tk()

    #change to true on release, false when debugging.
    outlinewindow2.overrideredirect(True)

    #window size
    outlinewindow2.geometry("482x150")

    #this will take the text from the entry widgets and writes it to a .txt file the "print" is used for debugging to confirm the code runs when told to
    def retrieve_text():
        text1 = E1.get()
        with open(text1+".txt", "w") as file:
            print(text1, file=file)
            text2 = E2.get()
            print(text2, file=file)
            text3 = E3.get()
            print(text3, file=file)
            text4 = E4.get()
            print(text4, file=file)
            text5 = E5.get()
            print(text5, file=file)
            print("file saved")
            #This then closes the file and moves it into the storage folder, of which the gui program calls from and inserts into the list.
            file.close()
            program_dir = os.path.dirname(os.path.abspath(__file__))
            source_path = os.path.join(program_dir, text1+".txt")
            destination_path = os.path.join(program_dir, "Storage", text1+".txt")

            shutil.move(source_path, destination_path)

    #frames for aesthetics:
    #first name:
    Textoutline1=Frame(outlinewindow2, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline1.grid(row=0, column=0)
    #second name:
    Textoutline2=Frame(outlinewindow2, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline2.grid(row=1, column=0)
    #phone number:
    Textoutline3=Frame(outlinewindow2, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline3.grid(row=2, column=0)
    #mobile number:
    Textoutline4=Frame(outlinewindow2, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline4.grid(row=3, column=0)
    #email adress
    Textoutline5=Frame(outlinewindow2, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline5.grid(row=4, column=0)

    #entry 1 (first name)
    L1=Label(outlinewindow2, text="First name:", bg="#3d3d3d", fg="white")
    L1.grid(row=0, column=0)
    E1=Entry(outlinewindow2, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E1.grid(row=0, column=1)

    #entry 2 (second name)
    L2=Label(outlinewindow2, text="Second name:", bg="#3d3d3d", fg="white")
    L2.grid(row=1, column=0)
    E2=Entry(outlinewindow2, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E2.grid(row=1, column=1)

    #entry 3 (Phone number)
    L3=Label(outlinewindow2, text="Phone number:", bg="#3d3d3d", fg="white")
    L3.grid(row=2, column=0)
    E3=Entry(outlinewindow2, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E3.grid(row=2, column=1)

    #entry 4 (Mobile number)
    L1=Label(outlinewindow2, text="Mobile number:", bg="#3d3d3d", fg="white")
    L1.grid(row=3, column=0)
    E4=Entry(outlinewindow2, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E4.grid(row=3, column=1)

    #entry 5 (Email adress)
    L1=Label(outlinewindow2, text="Email adress:", bg="#3d3d3d", fg="white")
    L1.grid(row=4, column=0)
    E5=Entry(outlinewindow2, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E5.grid(row=4, column=1)

    #Save contact button:
    commitchange=Button(outlinewindow2, height=9, width=9, bd=4, relief=SOLID, text="Save contact", bg="#3d3d3d", fg="white", command=retrieve_text)
    commitchange.grid(row=0, column=4, rowspan=100)#rowspan is set to arbitrarily huge number to maintain formatting, do not touch or it will destroy the format
    #exit button:
    exitbutton=Button(outlinewindow2, height=9, width=9, bd=4, relief=SOLID, text="Exit", command=outlinewindow2.destroy, bg="#3d3d3d", fg="white")
    exitbutton.grid(row=0, column=5, rowspan=100)#rowspan is set to arbtitrarily huge number to maintain formatting
    
    #end script
    outlinewindow2.mainloop()

#prevents the code from running when being imported, solving an infinite loop
if __name__ == "__main__":
    inputwindow()