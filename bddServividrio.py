# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 17:35:41 2018

@author: Martin Quivira
"""

import sqlite3

conn = sqlite3.connect('BDDServividrio.db', timeout=10)
c = conn.cursor()

""" 
c.execute('''CREATE TABLE pedido
          (nombreCliente, telefono, correo, cotizacion, estado)''')

c.execute('''CREATE TABLE correderaPVC
          (color, marcoDobleRiel, marcoTripleRiel, hoja, junquillo, traslapo, manilla)''')

c.execute('''CREATE TABLE PVCfija
          (color, marco)''')

c.execute('''CREATE TABLE PVCpuerta
          (color, marco)''')

# Incluye: insumos genericos de fabricacion y instalacion, vidrios, costos de fabricacion y instalacion

c.execute('''CREATE TABLE otros
          (tipo, precio)''') 

c.execute('''CREATE TABLE usuarios
          (nombre, contraseña)''') 

c.execute('''INSERT INTO usuarios VALUES
          ('Martin', 1111),
          ('Pancho', 0000)''') 

c.execute('''INSERT INTO otros VALUES
         ('Costo fabricación', 15000), 
         ('Costo instalación', 10000),
         ('Termopanel', 26000),
         ('Vidrio simple', 8000),
         ('Carro grande', 992),
         ('Carro chico', 6296)''') 

c.execute("INSERT INTO correderaPVC VALUES ('Blanco', 15642, 26325,17789, 4267, 5137, 1200)")

"""

class fijaPVC:

     def __init__(self, color, alto, ancho):
          
         self.alto = alto*1000
         self.ancho = ancho*1000
          
         self.marcoH = self.ancho+5
         self.marcoV = self.alto+5
          
         self.refMH = self.ancho-100
         self.refMV = self.alto-100
          
         perimetro = (self.alto + self.ancho)*2
          
         if perimetro%1 > 0:
          
            metrosL = perimetro - perimetro%1 + 1
             
         else:
              
            metrosL = perimetro
          
         self.tornillosAutoper = metrosL*2
          
         self.vidrioH = self.ancho-106
         self.vidiroV = self.alto-106
         
     def precioFijaPVC(self):
         
         materiales = 1
         
         precioFyI = precioFI(self.alto, self.ancho)
         
         precio = (materiales + precioFyI)*1.5
         
         return precio
     
          
def precioFI(alto, ancho):         
    # precioFinal = (materiales + fabricacion + instalacion)*1.5
    # Fabricacion = 15.000 aprox por metro cuadrado
    # Instalacion = 10.000 aprox por metro cuadrado
    cf = 'Costo fabricación' 
    ci = 'Costo instalación' 
              
    fabricacion = c.execute('''SELECT precio FROM otros WHERE tipo = ? ''', cf)
    instalacion = c.execute('''SELECT precio FROM otros WHERE tipo = ? ''', ci)
         
    precio = (fabricacion + instalacion)*(alto*ancho/1000000)
         
    return precio        
 
         