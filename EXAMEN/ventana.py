from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from clase import *


# Creamos una instancia de tipo controlador
controlador = controladorBD()

# Procedemos a insertar usando el metodo del objeto controlador
def ejecutaInsert():
    controlador.insert(varTrans.get(), varAdu.get())
    varTrans.set("")
    varAdu.set("")
    return
    
    
# Funcion para eliminar
def ejecutaDelete():
    controlador.delete(varId.get())
    varId.set("")
    return
    
    #Funcion Consultar Por Aduana
def ejecutaSelectA():
    rsAduana = controlador.ConsultaXAduana(varBus.get())
    if rsAduana:
        textBus.delete("1.0","end")

        aduana_data = f"Transportista: {rsAduana[0][1]}\nAduana: {rsAduana[0][2]}"
        textBus.insert(tk.INSERT, aduana_data) 
    else:
        messagebox.showinfo("Ojito", "Aduana no registrada en la BD")
        textBus.delete("1.0","end")
        return



      
# Creamos la ventana principal
ventana = Tk()
ventana.title("ADUANA")
ventana.geometry("650x400")

# Creamos el Notebook
panel = ttk.Notebook(ventana, style='TNotebook')
panel.pack(fill="both", expand="yes")

# Creamos un estilo para el Notebook
estilo = ttk.Style()
estilo.configure('TNotebook', tabposition='n')

# Creamos las pestañas
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

# Agregamos las pestañas al Notebook
panel.add(pestana1, text="INSERTAR")
panel.add(pestana2, text="ELIMINAR")
panel.add(pestana3, text="ConsultaXAduana")


# Creamos los widgets para la pestaña 1 INSERTAR
# Creamos las variables para los campos de texto
varTrans = StringVar()
varAdu = StringVar()

# Creamos los campos de texto   
txtTrans = Entry(pestana1, textvariable=varTrans)
txtAdu = Entry(pestana1, textvariable=varAdu)

# Creamos los labels
lblTrans = Label(pestana1, text="Transportista")
lblAdu = Label(pestana1, text="Aduana")

# Creamos el boton
btnInsertar = Button(pestana1, text="Insertar", command=ejecutaInsert)

# Creamos el titulo
titulo1 = Label(pestana1, text="INSERTAR", font=("Arial", 20, "bold"))

# Posicionamos los widgets
titulo1.grid(row=0, column=0, columnspan=2, pady=10)
lblTrans.grid(row=1, column=0, pady=5, padx=5)
txtTrans.grid(row=1, column=1, pady=5, padx=5)
lblAdu.grid(row=2, column=0, pady=5, padx=5)
txtAdu.grid(row=2, column=1, pady=5, padx=5)
btnInsertar.grid(row=4, column=0, columnspan=2, pady=5, padx=5)

# Creamos los widgets para la pestaña 2 ELIMINAR
# Creamos las variables para los campos de texto
varId = StringVar()

# Creamos los campos de texto
txtId = Entry(pestana2, textvariable=varId)

# Creamos los labels
lblId = Label(pestana2, text="Id")

# Creamos el boton
btnEliminar = Button(pestana2, text="Eliminar", command=ejecutaDelete)

# Creamos el titulo
titulo2 = Label(pestana2, text="ELIMINAR", font=("Arial", 20, "bold"))

# Posicionamos los widgets
titulo2.grid(row=0, column=0, columnspan=2, pady=10)
lblId.grid(row=1, column=0, pady=5, padx=5)
txtId.grid(row=1, column=1, pady=5, padx=5)
btnEliminar.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

# Creamos los widgets para la pestaña 3 ConsiltaXAduana
# Creamos las variables para los campos de texto
varBus = StringVar()

# Creamos los campos de texto
txtBus = Entry(pestana3, textvariable=varBus)

# Creamos los labels
lblBus = Label(pestana3, text="Aduana")

# Creamos el boton
btnBus = Button(pestana3, text="Buscar", command=ejecutaSelectA)

# Creamos el titulo
titulo3 = Label(pestana3, text="CONSULTA X ADUANA", font=("Arial", 20, "bold"))

# Creamos el text
textBus = Text(pestana3, width=30, height=10)

# Posicionamos los widgets
titulo3.grid(row=0, column=0, columnspan=2, pady=10)
lblBus.grid(row=1, column=0, pady=5, padx=5)
txtBus.grid(row=1, column=1, pady=5, padx=5)
btnBus.grid(row=2, column=0, columnspan=2, pady=5, padx=5)
textBus.grid(row=3, column=0, columnspan=2, pady=5, padx=5)

# Iniciamos el mainloop        
ventana.mainloop()

