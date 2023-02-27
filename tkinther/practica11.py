from tkinter import *
from tkinter import messagebox

def mostrarMensajes():
    messagebox.showinfo("Mensaje", "presionaste el boton azul")

#1. Instaciamos el objeto ventana
ventana = Tk()
ventana.title("ejemplo de 3 frames")
ventana.geometry("600x400")

#2. Creamos los frames
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True, fill=BOTH)

seccion2 = Frame(ventana, bg="blue")
seccion2.pack(expand=True, fill=BOTH)

seccion3 = Frame(ventana, bg="green")
seccion3.pack(expand=True, fill=BOTH)

#3. Creamos los widgets
botonAzul = Button(seccion1, text="Boton Azul", bg="blue", fg="white", command=mostrarMensajes)
botonAzul.place(x=60, y=60)

botonNegro = Button(seccion2, text="Boton Negro", bg="black", fg="white")
botonNegro.grid(row=0, column=0)

botonAmarillo = Button(seccion2, text="Boton Amarillo", bg="yellow", fg="black")
botonAmarillo.grid(row=1, column=1)

botonVerde = Button(seccion3, text="Boton Verde", bg="green", fg="white")
botonVerde.config(width=20, height=5)
botonVerde.pack(side=LEFT, anchor=NW)

#llamamos al mainloop
ventana.mainloop()
