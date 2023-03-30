from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import *

# Creamos una instancia de tipo controlador
controlador = controladorBD()

# Procedemos a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
    
#Funcion para buscar un Usuario
def ejecutaSelectU():
    
    rsUsuario = controlador.consultarUsuario(varBus.get())

    if rsUsuario:
        textBus.delete("1.0","end")
        usuario_data=str(rsUsuario[0])
        textBus.insert(tk.INSERT,usuario_data)
        usuario = rsUsuario[0]
        varNom.set(usuario[1]) 
        varCor.set(usuario[2]) 
        varCon.set(usuario[3]) 
    else:
        messagebox.showinfo("ojito", "Usuario no registrado en la BD")

                       

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("500x300")

panel = ttk.Notebook(ventana)
panel.pack(fill="both", expand="yes")

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

# Pestaña1: Formulario de Usuario
titulo = Label(pestana1, text="Registro Usuarios", fg="blue", font=("Modern",18))
titulo.pack()

varNom = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ")
lblNom.pack()
txtNom = Entry(pestana1, textvariable=varNom)
txtNom.pack()

varCor = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ")
lblCor.pack()
txtCor = Entry(pestana1, textvariable=varCor)
txtCor.pack()

varCon = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ")
lblCon.pack()
txtCon = Entry(pestana1, textvariable=varCon)
txtCon.pack()

btnGuardas = Button(pestana1, text="Guardar usuario", command=ejecutaInsert)
btnGuardas.pack()

#Pestaña 2: Buscar Usuario
titulo2= Label(pestana2, text="Buscar Usuario", fg="blue", font=("Modern",18))
titulo2.pack()

varBus = tk.StringVar()
lblid = Label(pestana2, text="Identificador de Usuario: ")
lblid.pack()
txtid = Entry(pestana2,textvariable=varBus)
txtid.pack()
btnBusqueda= Button(pestana2, text="Buscar", command=ejecutaSelectU)
btnBusqueda.pack()

subBus= Label(pestana2, text="Registrado: ", fg="blue", font=("Modern", 15))
subBus.pack()
textBus= tk.Text(pestana2, height=5, width=52)
textBus.pack()

panel.add(pestana1, text="Formulario de usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuario")

ventana.mainloop()


