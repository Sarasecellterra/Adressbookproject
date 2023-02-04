#imports
from tkinter import *
import os
import shutil
#end imports 
   
#almost all of this is scrapped from standardfieldmod, this saves on time, like, alot.
def editfunctionality():

    #opens the file that blackbookgui writes the name to and stores the name of the file in "filename"
    with open("varstore.txt", "r") as file:
        filename = file.read().strip()
        print(filename)

    #defines the name of the folder being pulled from
    storage="Storage"

    #opens the file by passing the folder/filename
    filedirectory=os.path.join(storage, filename)
    with open(filedirectory, "r") as f:
        chosen=f.readlines()
    
    line1=chosen[0]
    line2=chosen[1]
    line3=chosen[2]
    line4=chosen[3]
    line5=chosen[4]
    f.close()
    os.remove(filedirectory)

    #this will take the text from the entry widgets and writes it to a .txt file the "print" is used for debugging to confirm the code runs when told to
    def retrieve_text():
        text1 = E6.get()
        with open(text1+".txt", "w") as file:
            print(text1, file=file)
            text2 = E7.get()
            print(text2, file=file)
            text3 = E8.get()
            print(text3, file=file)
            text4 = E9.get()
            print(text4, file=file)
            text5 = E10.get()
            print(text5, file=file)
            print("file saved")
            #This then closes the file and moves it into the storage folder, of which the gui program calls from and inserts into the list.
            file.close()
            program_dir = os.path.dirname(os.path.abspath(__file__))
            source_path = os.path.join(program_dir, text1+".txt")
            destination_path = os.path.join(program_dir, "Storage", text1+".txt")

            shutil.move(source_path, destination_path)

    outlinewindow3=Tk()

    #window options
    outlinewindow3.config(bg="black")

    #frames for aesthetics:
    #first name:
    Textoutline1=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline1.grid(row=0, column=0)
    #second name:
    Textoutline2=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline2.grid(row=1, column=0)
    #phone number:
    Textoutline3=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline3.grid(row=2, column=0)
    #mobile number:
    Textoutline4=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline4.grid(row=3, column=0)
    #email adress
    Textoutline5=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline5.grid(row=4, column=0)

    #entry 1 (first name)
    L1=Label(outlinewindow3, text="First name:", bg="#3d3d3d", fg="white")
    L1.grid(row=0, column=0)
    E1=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E1.grid(row=0, column=1)

    #entry 2 (second name)
    L2=Label(outlinewindow3, text="Second name:", bg="#3d3d3d", fg="white")
    L2.grid(row=1, column=0)
    E2=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E2.grid(row=1, column=1)

    #entry 3 (Phone number)
    L3=Label(outlinewindow3, text="Phone number:", bg="#3d3d3d", fg="white")
    L3.grid(row=2, column=0)
    E3=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E3.grid(row=2, column=1)

    #entry 4 (Mobile number)
    L1=Label(outlinewindow3, text="Mobile number:", bg="#3d3d3d", fg="white")
    L1.grid(row=3, column=0)
    E4=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E4.grid(row=3, column=1)

    #entry 5 (Email adress)
    L1=Label(outlinewindow3, text="Email adress:", bg="#3d3d3d", fg="white")
    L1.grid(row=4, column=0)
    E5=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E5.grid(row=4, column=1)

    outputlabel1=Label(outlinewindow3, font="helvetica 5", text=line1, bg="#3d3d3d", fg="white")
    outputlabel1.grid(row=0, column=1)

    outputlabel2=Label(outlinewindow3, font="helvetica 5", text=line2, bg="#3d3d3d", fg="white")
    outputlabel2.grid(row=1, column=1)

    outputlabel3=Label(outlinewindow3, font="helvetica 5", text=line3, bg="#3d3d3d", fg="white")
    outputlabel3.grid(row=2, column=1)

    outputlabel4=Label(outlinewindow3, font="helvetica 5", text=line4, bg="#3d3d3d", fg="white")
    outputlabel4.grid(row=3, column=1)

    outputlabel5=Label(outlinewindow3, font="helvetica 5", text=line5, bg="#3d3d3d", fg="white")
    outputlabel5.grid(row=4, column=1)


    #more frames for aesthetics:
    #first name:
    Textoutline1=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline1.grid(row=0, column=4)
    #second name:
    Textoutline2=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline2.grid(row=1, column=4)
    #phone number:
    Textoutline3=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline3.grid(row=2, column=4)
    #mobile number:
    Textoutline4=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline4.grid(row=3, column=4)
    #email adress
    Textoutline5=Frame(outlinewindow3, width=100, height=30, borderwidth=3, relief=SOLID, bg="#3d3d3d")
    Textoutline5.grid(row=4, column=4)

    #entry 6 (first name)
    L6=Label(outlinewindow3, text="First name:", bg="#3d3d3d", fg="white")
    L6.grid(row=0, column=4)
    E6=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E6.grid(row=0, column=5)

    #entry 7 (second name)
    L7=Label(outlinewindow3, text="Second name:", bg="#3d3d3d", fg="white")
    L7.grid(row=1, column=4)
    E7=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E7.grid(row=1, column=5)

    #entry 8 (Phone number)
    L8=Label(outlinewindow3, text="Phone number:", bg="#3d3d3d", fg="white")
    L8.grid(row=2, column=4)
    E8=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E8.grid(row=2, column=5)

    #entry 9 (Mobile number)
    L9=Label(outlinewindow3, text="Mobile number:", bg="#3d3d3d", fg="white")
    L9.grid(row=3, column=4)
    E9=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E9.grid(row=3, column=5)

    #entry 9 (Email adress)
    L10=Label(outlinewindow3, text="Email adress:", bg="#3d3d3d", fg="white")
    L10.grid(row=4, column=4)
    E10=Entry(outlinewindow3, bd=3, relief=SOLID, font="Helvetica 14", bg="#3d3d3d", fg="white")
    E10.grid(row=4, column=5)

    #Save contact button:
    commitchange=Button(outlinewindow3, height=9, width=9, bd=4, relief=SOLID, text="Save changes", bg="#3d3d3d", fg="white", command=retrieve_text)
    commitchange.grid(row=0, column=6, rowspan=100)#rowspan is set to arbitrarily huge number to maintain formatting, do not touch or it will destroy the format
    #exit button:
    exitbutton=Button(outlinewindow3, height=9, width=9, bd=4, relief=SOLID, text="Exit", command=outlinewindow3.destroy, bg="#3d3d3d", fg="white")
    exitbutton.grid(row=0, column=7, rowspan=100)#rowspan is set to arbtitrarily huge number to maintain formatting
    #old/new
    oldnew=Label(outlinewindow3, height=9, bd=5, relief=SOLID, text="<-old/new->", bg="#3d3d3d", fg="white")
    oldnew.grid(row=0, column=3, rowspan=100)

    outlinewindow3.mainloop()

if __name__ == "__main__":
    editfunctionality()