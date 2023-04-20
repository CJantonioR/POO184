from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

class controladorBD:
            
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
                
        #Metodo para Insertar
    def insert(self, tra, adu,):
        #1. llamar a la conexion
        conx = self.conexionBD()

        #2. Revisar parametros vacios
        if(tra == "" or adu == ""):
            messagebox.showwarning("Aguas!!", "Revisa este show")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            datos = (tra, adu)
            qrInsert = "insert into TBPedimentos(Transporte, Aduana) values(?,?)"

            #4. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "Registro exitoso")


            
            #metodo para eliminar
    def delete(self, IDExpo):
            conx = self.conexionBD()
            cursor = conx.cursor()
            datos = (IDExpo,)
            qrDelete = "delete from TBPedimentos where IDExpo=?"
            #4.confirmacion de eliminar usuario
            confirmacion = messagebox.askquestion("Eliminar", "¿Estas seguro?")
            if confirmacion == "no":
                return  
            
            cursor.execute(qrDelete, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "Registro eliminado")
            
            #metodo ConsultaXAduana regresa todos los usuarios con la mima aduana
    def ConsultaXAduana(self, adu):
        conx = self.conexionBD()
        cursor = conx.cursor()
        datos = (adu,)
        qrSelect = "select * from TBPedimentos where Aduana=?"
        cursor.execute(qrSelect, datos)
        rsUsuario = cursor.fetchall()
        conx.close()
        return rsUsuario
    
        
        


            
            
       
        
        
            
        

        
       