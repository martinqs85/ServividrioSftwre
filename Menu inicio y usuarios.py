# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:44:44 2018

@author: Martin Quivira 
"""
import tkinter.messagebox
import tkinter as tk
from Catalogo import catalogo

usuarios = {'Pancho': 1345}

def inicio():

    global ventanaInicio
    global entryUsuarioI
    global entryContraseñaI
    
    ventanaInicio = tk.Tk()
    ventanaInicio.geometry("300x300")
    ventanaInicio.title("Servividrio")
    
    #Texto
    text1 = tk.Label(text="Bienvenido")
    text1.grid(row= 3, column=3, rowspan=1)
    
    text2 = tk.Label(text="Usuario:")
    text2.grid(row= 6, column=2, rowspan=1)
    
    text3 = tk.Label(text="Contraseña:")
    text3.grid(row= 9, column=2, rowspan=1)
    
    #Entrada de datos de usuario
    entryUsuarioI= tk.Entry(width=30) 
    entryUsuarioI.grid(row=6, column=3, rowspan=2)
    
    entryContraseñaI= tk.Entry(width=30, show='*')
    entryContraseñaI.grid(row=9, column=3, rowspan=2)
    
    #Botones
    boton1 = tk.Button(text="Entrar", command=iniciarSesion,width=20,height=2)
    boton1.grid(row=12, column=3)
    
    boton2 = tk.Button(text="Gestionar usuarios", command=registroUsuarios, width=20, height=2)
    boton2.grid(row=16, column=3)
    
    ventanaInicio.mainloop()
    
def iniciarSesion():    
    
    global ventanaInicio
    global entryUsuarioI
    global entryContraseñaI
    
    usuario = entryUsuarioI.get()
    contraseña = entryContraseñaI.get()
    
    if len(usuario)==0 or len(contraseña)==0:
        
       tk.messagebox.showinfo('Inicio de sesión', 'Hay campos en blanco')
       
    elif usuario in usuarios and contraseña == usuarios[usuario]:
        
       ventanaInicio.destroy()
       catalogo()
       
    else:
        
       tkinter.messagebox.showinfo('Inicio de sesión', 'Usuario o contraseña inválidos')

def registroUsuarios():
    
    global ventanaInicio
    global menuUsuarios
    global entryUsuario
    global entryContraseña
    global entryContraseña2
    
    ventanaInicio.destroy()
    
    menuUsuarios = tk.Tk()
    menuUsuarios.geometry("350x300")
    menuUsuarios.title("Usuarios")
    
    #Texto
    
    text0 = tk.Label(text="Ingrese sus datos")
    text0.grid(row=1, column=3, rowspan=2, columnspan=2)
    
    text1 = tk.Label(text="Usuario: ")
    text1.grid(row= 3, column=2, rowspan=2)
    
    text2 = tk.Label(text="Contraseña: ")
    text2.grid(row= 6, column=2, rowspan=2)
    
    text3 = tk.Label(text="Confirmar contraseña: ")
    text3.grid(row= 9, column=2, rowspan=2)
    
    #Entrada de datos de usuario
    entryUsuario= tk.Entry(width=30) 
    entryUsuario.grid(row=3, column=3, rowspan=2)
    
    entryContraseña= tk.Entry(width=30, show='*')
    entryContraseña.grid(row=6, column=3, rowspan=2)
    
    entryContraseña2= tk.Entry(width=30, show='*')
    entryContraseña2.grid(row=9, column=3, rowspan=2)
    
    #Botones
    boton1 = tk.Button(text="Registrar usuario", command=registrarUsuario, width=20, height=2)
    boton1.grid(columnspan=4, row=12)
    
    boton2 = tk.Button(text="Borrar usuario", command=borrarUsuario, width=20, height=2)
    boton2.grid(columnspan=4, row=15)
    
    boton3 = tk.Button(text="Volver", command=volver, width=20, height=2)
    boton3.grid(columnspan=4, row=18)
    
    
def borrarUsuario():
    
    global usuarios
    global entryUsuario
    global entryContraseña
    global entryContraseña2
    
    usuario = entryUsuario.get()
    contraseña = entryContraseña.get()
    contraseña2 = entryContraseña2.get()
    
    if len(usuario)==0 or len(contraseña)==0 or len(contraseña2)==0:
        
       tkinter.messagebox.showinfo('Registro', 'Hay campos en blanco')
    
    elif usuario not in usuarios:
        
       tkinter.messagebox.showinfo('Registro', 'No existe usuario con ese nombre')
        
    elif contraseña != contraseña2:
       
       tkinter.messagebox.showinfo('Registro', 'Las contraseñas no coinciden')
       
    else:
        
       del usuarios[usuario] 
       tkinter.messagebox.showinfo('Registro', 'Usuario borrado')


def registrarUsuario():    
    
    global usuarios
    global entryUsuario
    global entryContraseña
    global entryContraseña2
    
    usuario = entryUsuario.get()
    contraseña = entryContraseña.get()
    contraseña2 = entryContraseña2.get()
    
    if len(usuario)==0 or len(contraseña)==0 or len(contraseña2)==0:
        
       tkinter.messagebox.showinfo('Registro', 'Hay campos en blanco')
       
    elif usuario in usuarios:
        
       tkinter.messagebox.showinfo('Registro', 'Ya existe usuario con ese nombre')
        
    elif contraseña != contraseña2:
       
       tkinter.messagebox.showinfo('Registro', 'Las contraseñas no coinciden')
       
    else:
        
       usuarios[usuario] = contraseña
       tkinter.messagebox.showinfo('Registro', 'Usuario registrado')

def salir():
    
    global ventanaInicio
    ventanaInicio.destroy()
    
def volver():
    
    menuUsuarios.destroy()
    inicio()
    
inicio()