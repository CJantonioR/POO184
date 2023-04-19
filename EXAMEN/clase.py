from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3
import bcrypt 
          
class controladorBD:
    
# Creamos la conexión a la base de datos
conexion = sqlite3.connect('BDExportaciones.db')

# Creamos la tabla
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS TBPedimentos 
                (IDExpo INTEGER PRIMARY KEY AUTOINCREMENT, 
                Transporte VARCHAR(30), 
                Aduana VARCHAR(30))''')
conexion.commit()


 def __init__(self):
        pass
        
    #1. preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/reach/OneDrive/Documentos/POO184/EXAMEN/BDExportaciones.db")
            print("conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
                  
    def insertar(self):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("INSERT INTO TBPedimentos (IDExpo, Transporte, Aduana) VALUES (?, ?, ?)", 
                  (self.IDExpo, self.Transporte, self.Aduana))
        conn.commit()
        conn.close()
        
    def eliminar(self):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("DELETE FROM TBPedimentos WHERE IDExpo=?", (self.IDExpo,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def consultaXAduana(aduana):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("SELECT * FROM TBPedimentos WHERE Aduana=?", (aduana,))
        rows = c.fetchall()
        conn.close()
        return rows