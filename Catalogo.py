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
    tabla.grid()
    
    table = v.get()
    
    columnas = []
        
    if table == 'PVC Corredera':
        
       columnas = c.execute('''SELECT * FROM PVCcorredera''') 
       
       print(columnas)
       
    if table == 'PVC Fija':
        
       columnas = c.execute('''SELECT * FROM PVCfija''')   
    
    if table == 'PVC Corredera':
        
       columnas = c.execute('''SELECT * FROM PVCpuerta''')
       
    if table == 'PVC Corredera':
        
       columnas = c.execute('''SELECT * FROM otros''') 
       
    for columna in range(columnas):
        
        text = tk.Label(text=columnas(columna))
        text.grid()

    ventanaCatalogo.mainloop()

catalogo()

