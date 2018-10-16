# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:26:36 2018

@author: Martin Quivira
"""

from bddServividrio import precioFI, c

class correderaPVC:
    
     def __init__(self, color, alto, ancho, rieles, hojas, vidrio):
         
         self.alto = alto*1000
         self.ancho = ancho*1000
         self.color = color
         self.rieles = rieles
         self.hojas = hojas
    
         self.marcoH = self.ancho+5
         self.marcoV = self.alto+5
         self.refMarcoH = self.ancho-100
         self.refMarcoV = self.alto-100
    
         self.hojaH = (self.ancho-78)/self.hojas+37
         self.hojaV = self.alto-85
         self.refHojaH = self.hojaH-100
         self.refHojaV = self.alto-100
    
         self.traslapo = self.hojaV-7
    
         self.junquilloH = self.hojaH-130
         self.junquilloV = self.hojaV-130
         
         self.vidrio = vidrio
         
         area = self.hojaH*self.hojaV/1000000
         
         perimetro = (self.alto + self.ancho)*2
          
         if perimetro%1 > 0:
          
            metrosL = perimetro - perimetro%1 + 1
             
         else:
              
            metrosL = perimetro
          
         self.tornillosAutoper = metrosL*2
         
         if area > 2 : self.carro = 'Carro grande'
             
         else: self.carro = 'Carro chico'   
         
                    
     def precioCorrederaPVC(self):
         
         # Busca precio por metro en catalogo y calcula el del item
         
         precios = []
         
         #Marco
         if self.rieles == 2: valorM = c.execute('''SELECT
            marcoDobleRiel FROM PVCcorredera WHERE color = ?''', self.color)
         
         else: valorM = c.execute('''SELECT
            marcoTripleRiel FROM PVCcorredera WHERE color = ? ''', self.color)
         
         precioMarcoH = self.marcoH*valorM/6*2
         precioMarcoV = self.marcoV*valorM/6*2
         
         precios.append(precioMarcoH, precioMarcoV)
         
         #Refuerzo Marco
         precioRM = c.execute('''SELECT
            precio FROM otros WHERE tipo = ?''', 'Refuerzo marco' )
         
         precioRefuerzoMarco = (self.refMarcoH + self.refMarcoV)*2*precioRM/6
         
         precios.append(precioRefuerzoMarco)
         
         #Hoja
         precioH = c.execute('''SELECT
            hoja FROM PVCcorredera WHERE color = ?''', self.color)
         
         precioHojaH = self.hojaH*precioH/6*2*self.hojas
         precioHojaV = self.hojaV*precioH/6*2*self.hojas
         
         precios.append(precioHojaH, precioHojaV)
         
         #Refuerzo hojas
         precioRH = c.execute('''SELECT
            precio FROM otros WHERE tipo = ? ''', 'Refuerzo hoja')
         
         precioRefHoja = (self.refHojaH + self.refHojaV)*2*self.hojas*precioRH/6
         
         precios.append(precioRefHoja)
         
         #Junquillo
         precioJunquillo = c.execute('''SELECT
            junquillo FROM PVCcorredera WHERE color = ?''', self.color)
         
         precioJ = (self.junquilloH + self.junquilloV)*2*self.hojas*precioJunquillo/6
         
         precios.append(precioJ)
         
         #Traslapo
         precioT = c.execute('''SELECT
            traslapo FROM PVCcorredera WHERE color = ?''', self.color)
         
         precioTraslapo = self.traslapo*self.hojas*precioT/6
         
         precios.append(precioTraslapo)
         
         #Manilla
         precioManilla = ('''SELECT
            manilla FROM PVCcorredera WHERE color = ?''', self.color)
         
         precios.append(precioManilla)
         
         #Carros
         precioC = c.execute('''SELECT
            precio FROM otros WHERE tipo = ?''', self.carro)
         
         precioCarros = precioC*2*self.hojas
         
         precios.append(precioCarros)
         
         #Vidrios
         precioV = c.execute('''SELECT
            precio FROM otros WHERE tipo = ?''', self.vidrio)
         
         precioVidrio = ((self.alto-139)*(self.ancho-139)/1000000)*precioV*self.hojas
         
         precios.append(precioVidrio)
         
         
         
         materiales = 0
         
         for i in range(len(precios)):
             
             materiales = materiales + precios(i)
         
         fYi = precioFI(self.alto, self.ancho)
         
         precio = (materiales + fYi)*1.5
         
         return precio
    
     def corteCorrederaPVC(self):
         
         largo = 595
         

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
              
         
    