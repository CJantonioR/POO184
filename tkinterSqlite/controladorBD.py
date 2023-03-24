from tkinter import *
from tkinter import messagebox
import sqlite3
import bcrypt 

class controladorBD:
    
    def __init__(self):
        pass
        
    #1. preparamos la conexion para usarla cuando sea necesario
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/reach/OneDrive/Documentos/POO184/tkinterSqlite/DBUsuarios.db")
            print("conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
      
    #Metodo para Insertar      
    def guardarUsuario(self, nom, cor, con):
        #1. llamar a la conexion
        conx = self.conexionBD()
        
        #2. Revisar parametros vacios
        if(nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Aguas!!", "Revisa este show")
            conx.close()
        else:
            #3. Preparamos los datos y el querySQL
            cursor = conx.cursor()
            conH= self.encriptarCon(con)
            datos = (nom, cor, conH)
            qrInsert = "insert into TBRegistrados(Nombre, Correo, Contraseñas) values(?,?,?)"
            
            #4. Ejecutamos la consulta y cerramos la conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Registro", "Registro exitoso")
            
    #Metodo para encryptar
    def encriptarCon(self, con):
        conPlana= con
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt()
        
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa
    
    
        
