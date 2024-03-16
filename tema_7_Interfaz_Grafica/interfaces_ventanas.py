#
#En este código, estamos utilizando la biblioteca Tkinter para crear interfaces gráficas de usuario (GUI) basadas en ventanas. 
#Tkinter es una biblioteca estándar de Python que nos permite crear interfaces gráficas de manera sencilla y rápida.
#Primero, importamos todo de Tkinter.
#Creamos una ventana utilizando Tk().
#
#Definimos características de la ventana, como tamaño y título, usando métodos como geometry() y title().
#Mostramos la ventana con el método mainloop().
#
from tkinter import *

window = Tk()
window.geometry("600x400+10+20")
window.title("Mi primera ventana")
window.mainloop()
#
#-----------------------------------------------------------
#Lo primero es crear una ventana para ello instaciamos el Tk()

window = Tk()

#Debemos definir las caracteristicas de la misma, por ejemplo el tamaño inicial
#tocamos el metodo geometry ponemos como un string el tamaño inicial

window.geometry("600x400+10+20")

#Podemos poner un titulo

window.title("Mi primera vetana")

#Las ventanas no se muestran hasta que invocamos al metodo mainloop()

window.mainloop()

#Creamos otra ventana

window = Tk()
window.geometry("600x400+10+20")
window.title("Botones")

#Dentro de tkinter tenemos objetos para cada tipo de control (botones, cajas de texto..)

btn = Button(window, text="Esto es un boton", fg="blue")

#No solo llega con crearlos sino que debemos posicionarlos
#La primera opcion es coordenadas de forma absoluta se cuentan desde la esquina superior izquierda

btn.place(x=60,y=100)
window.mainloop()

#Los botones emiten un evento que es click, que es basicamente cuando son pulsados
#nosotros para poder gestionarlo debemos hacer una operacion de bind, indicar que accion va hacer el boton
#la forma de incicar esas acciones son las funciones o metodos
#creamos una funion que queresmo que se ejecute cuando hagan click
#la funcion destinada al binding recibe automaticamente los datos del evento

def botonClick(event):
    print("Boton pulsado")
    print(event)

window = Tk()
window.geometry("600x400+10+20")
window.title("Botones")

#Dentro de tkinter tenemos objetos para cada tipo de control (botones, cajas de texto..)

btn = Button(window, text="Esto es un boton", fg="blue")
btn.place(x=60,y=100)

#Hacemos el binding que es asociar la funcion y el boton
#aqui admite dos parametros el primero tipo de vento (ver documentacion) y el segundo la fincion
#es un puntero a una funcion y aqui si se suelen usar as lambdas

btn.bind("<Button-1>", botonClick)
window.mainloop()

#Tenemos labels que sirven  para mostrar informacion
window = Tk()
window.geometry("600x400+10+20")
window.title("Labels")
#primer argumento el window
lbl = Label(window,text="Esto es una label", fg = "green", font=("Helvetica",18))
lbl.place(x= 60, y = 50)
window.mainloop()

#Tenemos cajas de texto, que sirven para introducir datos

window = Tk()
window.geometry("600x400+10+20")
window.title("Cajas de texto")

#Se usa la clase entry

txt = Entry(window, text="Ejemplo de texto")
txt.place(x= 10, y = 10)

txt_2 = Entry(window, text="Ejemplo de texto 2", bd=5)
txt_2.place(x= 10, y = 50)

txt_3 = Entry(window, text="Ejemplo de texto 3", bd=1)
txt_3.place(x= 10, y = 100)

window.mainloop()

def ponerValor(event):
    txt.insert(END,"mi primer texto")

def leerValor():
    valor = txt.get()
    print(valor)

#Combinamos caja de texto y botones

window = Tk()
window.geometry("600x400+10+20")
window.title("Cajas de texto, labels y botones")

#label

lbl = Label(window,text="Numero", fg = "black", font=("Helvetica",12))
lbl.place(x= 10, y = 10)

#Se usa la clase entry

txt = Entry(window)
txt.place(x= 100, y = 10)

#boton
btn = Button(window,text="Poner valor")
btn.bind("<Button-1>", ponerValor)

#se puede hacer el bind de otra forma que es con command
#la diferencia es que command no pasa el evento como argumento

btn_2 = Button(window,text="Leer valor", command=leerValor)

btn.place(x=10,y=50)
btn_2.place(x=100,y=50)

window.mainloop()

#Tenemos mas controles de formularios
from tkinter.ttk import Combobox
window = Tk()
window.geometry("600x400+10+20")
window.title("Resto de controles de formulario")

#vamos a crear listbox, radio buttons, checkbuttons
lb = Listbox(window, height=5, selectmode="multiple")

#Añadir valores 
data = ("1","2","3","4")
for num in data:
    lb.insert(END, num)

lb.place(x=10, y = 10)

#Combos cuadro desplegable
cb = Combobox(window, values = data)
cb.place(x=10, y = 100)

#Radio buttons
#la variable es donde se va a guardar el valor seleccionado
v0 = IntVar()
v0.set(1)
r1 = Radiobutton(window, text= "par", value = 1, variable= v0)
r2 = Radiobutton(window, text= "impar", value = 2, variable= v0)

r1.place(x= 10, y = 150)
r2.place(x= 100, y = 150)


#Checkbox
v1 = IntVar()
v2 = IntVar()

c1 = Checkbutton(window, text="Futbol", variable = v1)
c2 = Checkbutton(window, text="Rugby", variable = v2)

c1.place(x = 10, y = 200)
c2.place(x = 100, y = 200)

window.mainloop()