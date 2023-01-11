from cProfile import label
from logging import root
from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox
from turtle import hideturtle
from PIL import Image,ImageTk
import os
from stegano import lsb
from cryptography.fernet import Fernet
import filecmp

root=Tk()
root.title("Cipher Herold")
root.geometry("700x500+150+180")
root.resizable(False,True)
root.config(bg="#933dbc")

#===========functions==================
def showimg():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All files","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    
def hide():
    global secret
    global key
    message=txt1.get(1.0,END)
    key = Fernet.generate_key()
    f= Fernet(key)
    messagebox.askyesno("Encrypt","Are you sure?")
    secret = lsb.hide(str(filename),message)
    txt2.insert(END,f)
    with open('sec.key','wb') as g:
        g.write(key)
        g.close()

    
def show():
    messagebox.askquestion("decrypt","Enter the key?")
    key2=txt2.get(1.0,END)
    with open('sec1.key','wb') as k:
        k.write(key2)
        k.close()
    op=filecmp.cmp('sec.key','sec1.key')
    if op>0:    
     clear_message=lsb.reveal(filename)
     txt1.delete(1.0,END)
     txt1.insert(END, clear_message)
     messagebox.askyesno("Decrypt","Are you sure?")
    
def save():
    secret.save("hidden.png")
    txt1.delete(1.0,END)
    txt2.delete(1.0,END)
    messagebox.showinfo("Saved","Saved Successfully!")            

#====================Icon====================

image_icon=PhotoImage(file="sha1.png")
root.iconphoto(False,image_icon)

#===================Logo=======================

logo=PhotoImage(file="sasuke.png")
Label(root,image=logo,bg="#933dbc").place(x=8,y=0)
Label(root,text="Img Encypt & Decpt",bg="#933dbc",fg="white",font="Helvetica 25 bold").place(x=110,y=20)
Label(root,text="Project By- Hari Hara Sudhan (CTIS)",bg="#933dbc",fg="white",font="Helvetica 10 bold").place(x=120,y=70)

#================First frame==========================

f1=Frame(root,bd=3,bg="black",width=340,height=240,relief=SUNKEN)
f1.place(x=15,y=100)
lbl=Label(f1,bg="black")
lbl.place(x=40,y=20)

#=================Second frame======================

f2=Frame(root,bd=3,bg="white",width=340,height=240,relief=SUNKEN)
f2.place(x=350,y=100)
txt1=Text(f2,font="Akzidenz-Grotesk 18 ",bg="white",fg="black",relief=SUNKEN,wrap=WORD)
txt1.place(x=0,y=0,width=320,height=295)

scr1=Scrollbar(f2)
scr1.place(x=320,y=0,height=300)
scr1.configure(command=txt1.yview)
txt1.configure(yscrollcommand=scr1.set)

#=================Third frame======================

f3=Frame(root,bd=3,bg="#933dbc",width=330,height=110,relief=GROOVE)
f3.place(x=15,y=350)
Button(f3,text="Open Image",width=10,height=2,command=showimg,font="Helvetica 14 bold").place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,command=save,font="Helvetica 14 bold").place(x=180,y=30)
Label(f3,text="Pic,Img,Photo File..",bg="#933dbc",fg="white").place(x=20,y=5)

#=================Fourth frame======================


f4=Frame(root,bd=3,bg="#933dbc",width=330,height=110,relief=GROOVE)
f4.place(x=360,y=350)
Button(f4,text="Hide Data",width=10,height=2,command=hide,font="Helvetica 14 bold").place(x=20,y=30)
Button(f4,text="Show Data",width=10,height=2,command=show,font="Helvetica 14 bold").place(x=180,y=30)
Label(f4,text="Options available..",bg="#933dbc",fg="white").place(x=20,y=5)

#=================fifth frame=================
f5=Frame(root,bd=2,bg="#933dbc",width=600,height=40,relief=GROOVE)
f5.place(x=15,y=460)
txt2=Text(f5,font="Akzidenz-Grotesk",bg="white",fg="black",relief=SUNKEN,wrap=WORD)
txt2.place(x=60,y=3,height=30,width=500)
Label(f5,text="KEY:",bg="#933dbc",fg="white").place(x=20,y=5)

root.mainloop()