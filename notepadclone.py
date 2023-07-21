from tkinter import *
from tkinter import messagebox as mg
from tkinter import filedialog as fd
r=Tk()
global maintext
#Function to adjust textbox size to always match the window size
def text_adjust(event):
    global textarea
    main_geometry=r.geometry()
    main_geometry=main_geometry.split('+')
    main_geometry=main_geometry[0]
    main_geometry=main_geometry.split('x')
    textarea.config(width=main_geometry[0],height=main_geometry[1])
def openfile():
    f=fd.askopenfile(mode='r',filetypes=[('Text File','.txt')])
    maintext=f.read()
    print(maintext)
menubar=Menu(r)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save")
filemenu.add_command(label="Save As")
filemenu.add_separator()
filemenu.add_command(label="Exit")
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Delete")
editmenu.add_separator()
editmenu.add_command(label="Find")
editmenu.add_command(label="Replace")
infomenu=Menu(menubar,tearoff=0)
infomenu.add_command(label="Source Code")
infomenu.add_command(label="About")
menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label="Edit",menu=editmenu)
menubar.add_cascade(label="Info",menu=infomenu)
r.config(menu=menubar)
r.bind('<Configure>',text_adjust)
textarea=Text(r,borderwidth=0)
textarea.pack()
r.title("Notepad Clone")
r.geometry('900x500')
r.mainloop()