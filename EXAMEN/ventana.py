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
        cursor.execute("INSERT INTO TBPedimentos (Transporte, Aduana) VALUES (?, ?)", (transporte, aduana))
        conexion.commit()
        mensaje.config(text="Registro insertado correctamente")
        
    def eliminar():
        id_expo = entrada_id_expo.get()
        cursor.execute("DELETE FROM TBPedimentos WHERE IDExpo=?", (id_expo,))
        conexion.commit()
        mensaje.config(text="Registro eliminado correctamente")

    def consulta_x_aduana():
        aduana = entrada_aduana_consulta.get()
        cursor.execute("SELECT * FROM TBPedimentos WHERE Aduana=?", (aduana,))
        registros = cursor.fetchall()
        resultado.config(text="")
        for registro in registros:
            resultado.config(text=resultado.cget("text") + f"{registro[0]} | {registro[1]} | {registro[2]}\n")
            
            def __init__(self, IDExpo, Transporte, Aduana):
        self.IDExpo = IDExpo
        self.Transporte = Transporte
        self.Aduana = Aduana


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

root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()
 




