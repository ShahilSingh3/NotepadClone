from tkinter import *
r=Tk()
#Function to adjust textbox size to always match the window size
def text_adjust(event):
    global textarea
    main_geometry=r.geometry()
    main_geometry=main_geometry.split('+')
    main_geometry=main_geometry[0]
    main_geometry=main_geometry.split('x')
    textarea.config(width=main_geometry[0],height=main_geometry[1])
filemenu=Button(r,text="File",borderwidth=0,width=6)
filemenu.place(x=1,anchor=NW)
editmenu=Button(r,text="Edit",borderwidth=0,width=6)
editmenu.place(x=51,y=12,anchor=W)
viewmenu=Button(r,text='View',borderwidth=0,width=6)
viewmenu.place(x=101,y=12,anchor=W)
r.bind('<Configure>',text_adjust)
textarea=Text(r,borderwidth=0)
textarea.place(x=0,y=24)
r.geometry('900x500')
r.mainloop()