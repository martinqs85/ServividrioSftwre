# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:05:25 2018

@author: Martin Quivira
"""

import tkinter as tk
from bddServividrio import c 

def catalogo():
    
    ventanaCatalogo = tk.Tk()
    ventanaCatalogo.geometry("500x500")
    ventanaCatalogo.title("Catalogo")
    
    optionList = ('PVC Corredera', 'PVC Fija', 'PVC Puerta', 'Otros')
    v = tk.StringVar()
    v.set(optionList[0])
    tabla = tk.OptionMenu(ventanaCatalogo, v, *optionList)
    tabla.grid(row = 1, column = 1)
    
    
        
    table = v.get()
    
    columnas = []
        
    if table == 'PVC Corredera':
        
       #Color
       text1 = tk.Label(text="Color")
       text1.grid(row = 2, column = 1)
       
       lbColor = tk.Listbox(ventanaCatalogo)
       for colour in c.execute('''SELECT color FROM PVCcorredera'''):
           
           lbColor.append(colour)
           
       lbColor.grid(row = 3, column = 1)    
       
       #Marco2
       text2 = tk.Label(text="Marco 2 rieles")
       text2.grid(row = 2, column = 2)
       
       lbMarco2r = tk.Listbox(ventanaCatalogo)
       for marco2riel in c.execute('''SELECT marcoDobleRiel FROM PVCcorredera'''):
           
           lbMarco2r.append(marco2riel)
       
       lbMarco2r.grid(row = 3, column = 2)
       
       #Marco3r
       text3 = tk.Label(text="Marco 3 rieles")
       text3.grid(row = 2, column = 3)
       
       lbMarco3r = tk.Listbox(ventanaCatalogo)
       
       for marco3riel in c.execute('''SELECT marcoTripleRiel FROM PVCcorredera'''):
           
           lbMarco3r.append(marco3riel) 
           
       lbMarco3r.grid(row = 3, column = 3)
           
          
           
    
    ventanaCatalogo.mainloop()

catalogo()

