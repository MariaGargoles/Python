#En este código, creamos una ventana con un formulario simple utilizando el sistema de grid de Tkinter.
#
#Primero, creamos una instancia de la ventana principal (Tk()) y configuramos sus propiedades, como el título, el tamaño y el color de fondo.
#Luego, cargamos una imagen y la mostramos en un widget de Label en la primera columna y abarcando cuatro filas.
#Después, creamos etiquetas y cuadros de entrada para ingresar información como nombre, estudios, teléfono y dirección. 
#Utilizamos el método grid() para posicionar estos elementos en filas y columnas específicas dentro de la ventana.
#Finalmente, iniciamos el bucle principal de eventos con window.mainloop() para mantener la ventana abierta y receptiva a las interacciones del usuario.
#

from tkinter import *
#IMPORTANT PARA ESTE EJEMPLO USAMOS EL IMPORT * PERO NO ES NADA RECOMENDABLE !!!
from tkinter.ttk import Combobox

window = Tk()
window.title("Ejemplo de formulario con grid")
window.geometry("500x300")
window.maxsize(500,300)
window.config(bg="lightgrey")

imagen = PhotoImage(file="gatito.gif")
porcion = imagen.subsample(1,1)
img = Label(window, image=porcion)
img.grid(row=0, column=0, rowspan = 4)

lbl_nombre = Label(window, text="Nombre").grid(row=0, column=1)
txt_nombre = Entry(window, bd=3)
txt_nombre.grid(row=0, column=2)

lbl_estudios = Label(window, text="Estudios").grid(row=1, column=1)
data = ("ESO","Bachiller", "FP")
cb_estudios = Combobox(window, values = data)
cb_estudios.grid(row=1, column=2)

lbl_telefono = Label(window, text="Telefono").grid(row=2, column=1)
txt_telefono = Entry(window, bd=3)
txt_telefono.grid(row=2, column=2)

lbl_direccion = Label(window, text="Direccion").grid(row=3, column=1)
txt_direccion = Entry(window, bd=3)
txt_direccion.grid(row=3, column=2)

window.mainloop()
