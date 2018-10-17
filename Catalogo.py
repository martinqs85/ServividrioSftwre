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
        
    if table == 'PVC Corredera':
        
       #Color
       text1 = tk.Label(text="Color")
       text1.grid(row = 2, column = 1)
       
       lbColor = tk.Listbox(ventanaCatalogo)
       for colour in c.execute('''SELECT color FROM correderaPVC'''):
           
           lbColor.append(colour)
           
       lbColor.grid(row = 3, column = 1)    
       
       #Marco2
       text2 = tk.Label(text="Marco 2 rieles")
       text2.grid(row = 2, column = 2)
       
       lbMarco2r = tk.Listbox(ventanaCatalogo)
       for marco2riel in c.execute('''SELECT marcoDobleRiel FROM correderaPVC'''):
           
           lbMarco2r.append(marco2riel)
       
       lbMarco2r.grid(row = 3, column = 2)
       
       #Marco3r
       text3 = tk.Label(text="Marco 3 rieles")
       text3.grid(row = 2, column = 3)
       
       lbMarco3r = tk.Listbox(ventanaCatalogo)
       
       for marco3riel in c.execute('''SELECT marcoTripleRiel FROM correderaPVC'''):
           
           lbMarco3r.append(marco3riel) 
           
       lbMarco3r.grid(row = 3, column = 3)
       
       #Hoja
       text4 = tk.Label(text="Hoja")
       text4.grid(row = 2, column = 4)
       
       lbHoja = tk.Listbox(ventanaCatalogo)
       
       for hoja in c.execute('''SELECT hoja FROM correderaPVC'''):
           
           lbHoja.append(hoja) 
           
       lbHoja.grid(row = 3, column = 4)
          
       #Junquillo
       text5 = tk.Label(text="Junquillo")
       text5.grid(row = 2, column = 5)
       
       lbJunquillo = tk.Listbox(ventanaCatalogo)
       
       for junquillo in c.execute('''SELECT junquillo FROM correderaPVC'''):
           
           lbJunquillo.append(junquillo) 
           
       lbJunquillo.grid(row = 3, column = 5)
       
       #Traslapo
       text6 = tk.Label(text="Traslapo")
       text6.grid(row = 2, column = 6)
       
       lbTraslapo = tk.Listbox(ventanaCatalogo)
       
       for traslapo in c.execute('''SELECT traslapo FROM correderaPVC'''):
           
           lbTraslapo.append(traslapo) 
           
       lbTraslapo.grid(row = 3, column = 6)
       
       #Manilla
       text7 = tk.Label(text="Manilla")
       text7.grid(row = 2, column = 7)
       
       lbManilla = tk.Listbox(ventanaCatalogo)
       
       for manilla in c.execute('''SELECT manilla FROM correderaPVC'''):
           
           lbManilla.append(manilla) 
           
       lbManilla.grid(row = 3, column = 7)
    
    ventanaCatalogo.mainloop()

catalogo()
   


