# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 01:35:33 2018

@author: Martin Quivira
"""

from tkinter import *
from tkinter import ttk
from Catalogo import catalogo
import subprocess 

def create_window():
    cw = Tk()
def open_window():
    subprocess.Popen("Sprint1-1.pyw", shell="true")


    raiz=Tk()
    raiz.title("Pedidos")
    raiz.geometry("350x300")
    raiz.config(bg="gray")
    raiz.resizable(False, False)

    frame=Frame()
    frame.pack()
    frame.config(bg="gray")
    frame.config(width="350",height="450")
    frame.config(bd=15)
    frame.config(cursor="hand2")
    titulo1= Label(frame, text= "Haga su pedido",fg="white",font=("Calibri",18),bg="gray").place(relx=0.5, rely=0.03, anchor=CENTER)
    labelname = Label(frame, text= "Nombre", fg="white",bg="gray").place(relx=0.005, rely=0.15)
    nombretb = Entry(frame, width = "35").place(relx=0.22,rely=0.15)

    labeldir = Label(frame, text= "Dirección", fg="white",bg="gray").place(relx=0.005, rely=0.25)
    dirtb = Entry(frame,width = "35").place(relx=0.22,rely=0.25)

    labelmail = Label(frame, text= "Correo", fg="white",bg="gray").place(relx=0.005, rely=0.35)
    mailtb = Entry(frame,width = "35").place(relx=0.22,rely=0.35)

    labelopt = Label(frame, text= "Producto", fg="white",bg="gray").place(relx=0.005, rely=0.45)
    option = ttk.Combobox(frame, width="32").place(relx=0.22,rely=0.45)

    labelCant = Label(frame, text= "Cantidad", fg="white",bg="gray").place(relx=0.005, rely=0.55)
    cantidadtb = Entry(frame,width = "10").place(relx=0.22,rely=0.55)

    labeldetalle = Label(frame, text= "Detalle", fg="white",bg="gray").place(relx=0.005, rely=0.65)
    detalletb = Entry(frame,width = "32").place(relx=0.22,rely=0.65)



    boton=Button(raiz,text="Cotizar").place(relx=0.25,rely=0.8)
    boton2=Button(raiz,text="Abrir Catálogo",command=catalogo()).place(relx=0.5,rely=0.8)


    raiz.mainloop()

open_window()


