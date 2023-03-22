from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana= Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Pestaña1: Formuario de Usuario2
titulo= Label( pestana1, text="Registro Usuarios", fg="blue", font=("Moder",18)).pack()
              
varNom=tk.StringVar()
lblNom=Label(pestana1, text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCor=tk.StringVar()
lblCor=Label(pestana1, text="Correo: ").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon=tk.StringVar()
lblCon=Label(pestana1, text="Contraseña: ").pack()
txtCon=Entry(pestana1,textvariable=varCor).pack()

btnGuardas=Button(pestana1, text="Guardad usuario").pack()
          


panel.add(pestana1, text="Formulario de usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3,text="Consultar Usuarios")
panel.add(pestana4,text="Actualizar Usuario")



ventana.mainloop()

