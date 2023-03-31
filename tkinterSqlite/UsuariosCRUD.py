from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from controladorBD import *

# Creamos una instancia de tipo controlador
controlador = controladorBD()
#modificamos el codigo ya hace lo que el profe pide
# Procedemos a Guardar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())
    
#Funcion para buscar un Usuario
def ejecutaSelectU():
    
    rsUsuario = controlador.consultarUsuario(varBus.get())

    if rsUsuario:
        textBus.delete("1.0","end")
        # usuario_data = str(rsUsuario[0])
        # Extraemos solamente nombre y correo
        usuario_data = f"Nombre: {rsUsuario[0][1]}\nCorreo: {rsUsuario[0][2]}"
        textBus.insert(tk.INSERT, usuario_data) 
    
    else:
        messagebox.showinfo("Ojito", "Usuario no registrado en la BD")
        textBus.delete("1.0","end")
        return
    
# Función para Consultar Usuarios de la base de datos
# Función para Consultar Usuarios de la base de datos
def ejecutaSelectAll():
        # Desactivamos el botón para evitar doble clic
        btnConsulta.config(state="disabled")
        
        # Obtenemos todos los usuarios de la base de datos
        usuarios = controlador.selectAll()
        
        # Creamos una instancia del widget Treeview
        tree = ttk.Treeview(pestana3, columns=('Nombre', 'Correo', 'Contraseña'), show='headings')
        
        # Configuramos las columnas del Treeview
        tree.heading('Nombre', text='Nombre')
        tree.heading('Correo', text='Correo')
        tree.heading('Contraseña', text='Contraseña')
        
        # Agregamos los usuarios al Treeview
        for usuario in usuarios:
            tree.insert('', 'end', values=(usuario[1], usuario[2], usuario[3]))
        tree.pack()
        
        # Reactivamos el botón después de que se complete la consulta
        btnConsulta.config(state="normal")
    
              

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

#Pestaña 3: Consultar Usuarios
titulo3= Label(pestana3, text="Consultar Usuarios", fg="blue", font=("Modern",18))
titulo3.pack()
# Creamos los encabezados de las columnas
btnConsulta= Button(pestana3, text="Consultar", command=ejecutaSelectAll)
btnConsulta.pack()

#Pestaña 4: Actualizar Usuario



panel.add(pestana1, text="Formulario de usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="Consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuario")

ventana.mainloop()


