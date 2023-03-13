import tkinter as tk
from caja_popular import CajaPopular

class Interfaz:
    def __init__(self):
        self.caja_popular = CajaPopular()
    
    def iniciar(self):
        self.ventana = tk.Tk()
        self.crear_widgets()
        self.ventana.mainloop()
    
    def crear_widgets(self):
        # aquí se crearían los widgets de la interfaz
        pass
    
    def manejar_eventos(self, evento):
        # aquí se manejarían los eventos de la interfaz
        pass
