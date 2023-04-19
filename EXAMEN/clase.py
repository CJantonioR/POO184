import sqlite3

class controladorBD:
    
    def __init__(self):
        pass
        
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("BDExportaciones.db")
            print("conectado BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar")
                  
    def insertar(self, transporte, aduana):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("INSERT INTO TBPedimentos VALUES (NULL, ?, ?)", (transporte, aduana))
        conn.commit()
        conn.close()
        
      
        
    def eliminar(self, id_expo):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("DELETE FROM TBPedimentos WHERE IDExpo=?", (id_expo,))
        conn.commit()
        conn.close()
        
    def consultaXAduana(self, aduana):
        conn = sqlite3.connect('BDExportaciones.db')
        c = conn.cursor()
        c.execute("SELECT * FROM TBPedimentos WHERE Aduana=?", (aduana,))
        rows = c.fetchall()
        conn.close()
        return rows
