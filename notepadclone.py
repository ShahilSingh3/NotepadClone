from tkinter import *
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
#Function to open the file and replace textbox text
def openfile():
    global filename
    f=fd.askopenfile(mode='r+',filetypes=[('Text File','.txt')],initialdir='/')
    if f != None:
        maintext=f.read()
        textarea.delete(1.0,END)
        textarea.insert(1.0,maintext)
        filename=f.name
        f.close()
#Function to save the text to a file
def savefile():
    maintext=textarea.get(1.0,END)
    try:
        filename
        f=open(filename,'w')
        f.write(maintext)
        f.close()
    except:
        try:
            file_name=fd.asksaveasfilename(defaultextension='.txt',filetypes=[('Text File','.txt'),('HTML','.html'),('All Files','.*')])
            f=open(file_name,'w')
            f.write(maintext)
            f.close()
        except:
            pass
def saveasfile():
    maintext=textarea.get(1.0,END)
    filename=fd.asksaveasfilename(defaultextension='.txt',filetypes=[('Text File','.txt'),('HTML','.html'),('All Files','.*')])
    f=open('w',filename)
    f.write(maintext)
    f.close()
def customquit():
    # maintext=textarea.get(1.0,END)
    try:
        pass
    #     filename
    #     f=open('r',filename)
    #     filetext=f.read()
    #     f.close()
    #     if(filetext==maintext):
    #         r.destroy()
    #     else:
    #         confirm_save=Tk()
    #         height=str(round(confirm_save.winfo_screenheight()/2-200))
    #         width=str(round(confirm_save.winfo_screenwidth()/2-450))
    #         confirm_save.geometry("700x200+"+width+"+"+height)
    #         confirm_save.mainloop()
    except:
        pass
menubar=Menu(r)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open",command=openfile)
filemenu.add_command(label="Save",command=savefile)
filemenu.add_command(label="Save As",command=saveasfile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=customquit)
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