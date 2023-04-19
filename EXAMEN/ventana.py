from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from clase import *

# Creamos una instancia de tipo controlador
controlador = controladorBD()

# Definimos las funciones para las operaciones de inserción, eliminación y consulta
def insertar():
    transporte = entrada_transporte.get()
    aduana = entrada_aduana.get()
    controlador.insertar(transporte, aduana)
    mensaje.config(text="Registro insertado correctamente")
        
def eliminar():
    id_expo = entrada_id_expo.get()
    controlador.eliminar(id_expo)
    mensaje.config(text="Registro eliminado correctamente")

def consulta_x_aduana():
    aduana = entrada_aduana_consulta.get()
    registros = controlador.consultaXAduana(aduana)
    resultado.config(text="")
    for registro in registros:
        resultado.config(text=resultado.cget("text") + f"{registro[0]} | {registro[1]} | {registro[2]}\n")
        

# Creamos la interfaz gráfica
ventana = tk.Tk()
ventana.title("Exportaciones")
ventana.geometry("400x300")

# Creamos los elementos de la interfaz gráfica
etiqueta_transporte = tk.Label(ventana, text="Transporte:")
entrada_transporte = tk.Entry(ventana)
etiqueta_aduana = tk.Label(ventana, text="Aduana:")
entrada_aduana = tk.Entry(ventana)
boton_insertar = tk.Button(ventana, text="Insertar", command=insertar)
etiqueta_id_expo = tk.Label(ventana, text="IDExpo:")
entrada_id_expo = tk.Entry(ventana)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar)
etiqueta_aduana_consulta = tk.Label(ventana, text="Aduana:")
entrada_aduana_consulta = tk.Entry(ventana)
boton_consulta = tk.Button(ventana, text="Consulta por Aduana", command=consulta_x_aduana)
mensaje = tk.Label(ventana, text="")
resultado = tk.Label(ventana, text="", justify="left")

# Alineamos los elementos en la interfaz gráfica
etiqueta_transporte.grid(column=0, row=0, padx=5, pady=5)
entrada_transporte.grid(column=1, row=0, padx=5, pady=5)
etiqueta_aduana.grid(column=0, row=1, padx=5, pady=5)
entrada_aduana.grid(column=1, row=1, padx=5, pady=5)
boton_insertar.grid(column=2, row=0, padx=5, pady=5)
etiqueta_id_expo.grid(column=0, row=2, padx=5, pady=5)
entrada_id_expo.grid(column=1, row=2, padx=5, pady=5)
boton_eliminar.grid(column=2, row=2, padx=5, pady=5)
etiqueta_aduana_consulta.grid(column=0, row=3, padx=5, pady=5)
entrada_aduana_consulta.grid(column=1, row=3, padx=5, pady=5)
boton_consulta.grid(column=2, row=3, padx=5, pady=5)
mensaje.grid(column=0, row=4, columnspan=3, padx=5, pady=5)
resultado.grid(column=0, row=5, columnspan=3, padx=5, pady=5)

# Ejecutamos la interfaz gráfica
ventana.mainloop()




 




