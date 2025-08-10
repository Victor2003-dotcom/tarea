import tkinter as tk
from math import sqrt
def suma():
    d1=float (e1.get())
    d2=float (e2.get())
    r=d1+d2
    etiqueta1 = tk.Label(ventana,  text=f"{r}",  font=("Arial",18), fg="white", bg= "green")
    etiqueta1.place(x=200,y=0)
def resta():
    d2=float (e1.get())
    d1=float (e2.get())
    r=d1-d2
    etiqueta1 = tk.Label(ventana,  text=f"{r}",  font=("Arial",18), fg="white", bg= "green")
    etiqueta1.place(x=500,y=0)
def multiplicacion():
    d2=float (e1.get())
    d1=float (e2.get())
    r=d2*d1
    etiqueta1 = tk.Label(ventana,  text=f"{r}",  font=("Arial",18), fg="white", bg= "green")
    etiqueta1.place(x=500,y=0)
def division():
    d2=float (e1.get())
    d1=float (e2.get())
    r=d2/d1
    etiqueta1 = tk.Label(ventana,  text=f"{r}",  font=("Arial",18), fg="white", bg= "green")
    etiqueta1.place(x=500,y=0)
ventana = tk.Tk()
ventana.title("mi primera pagina")
ventana.geometry("500x500")
ventana.configure(bg="red")# cambia color de fondo
b1= tk.Button(ventana, text="suma(+)", command=suma,bg= "green" )
b1.place(x=120,y=200)
e1= tk.Entry(ventana, width=25)
e1.place(x=100,y=100)
e2= tk.Entry(ventana, width=25)
e2.place(x=300,y=100)
b2= tk.Button(ventana, text="resta(-)", command=resta, bg= "green")
b2.place(x=200,y=200)
b3= tk.Button(ventana, text="multiplicacion(*)", command=multiplicacion, bg= "green")
b3.place(x=270,y=200)
b4= tk.Button(ventana, text="division(/)", command=division, bg= "green")
b4.place(x=400,y=200)
ventana.mainloop()

