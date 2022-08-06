from tkinter import *
from tkinter import filedialog

#r = Menu()


class Menu():

    def __init__(self):
        self.menu = Tk()
        self.menu.title("Menu")
        
        self.menu.geometry("650x450")
        self.menu.configure(bg="#18b9e4")
        self.container()
        #self.menu.mainloop()

    def centrar(self,r,ancho,alto):
        altura_p = r.winfo_screenheight()
        ancho_p = r.winfo_screenwigth()
        x = (ancho_p // 2) - (ancho // 2)
        y = (altura_p // 2) - (alto // 2)
        r.geometry(f"+{x}+{y}")

    def container(self):
        self.frame = Frame(height=550,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        curso = Label(self.frame, text="Nombre del curso: Lab. Lenguajer Formales de Programación")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Arial Rounded MT Bold",13))

        nombre = Label(self.frame, text="Nombre del estudiante: José Daniel Fuentes Orozco")
        nombre.pack
        nombre.place(x=20,y=40)
        nombre.config(font=("Arial Rounded MT Bold",13))

        carne = Label(self.frame, text="Carné del estudiante: 202001228")
        carne.pack
        carne.place(x=20,y=70)
        carne.config(font=("Arial Rounded MT Bold",13))

        botonCarga =  Button(self.frame,text="Cargar Archivo")
        botonCarga.place(x=280,y=150)

        botonGestionar = Button(self.frame,text="Gestionar Cursos")
        botonGestionar.place(x=275,y=190)

        botonConteo = Button(self.frame, text="Conteo de Créditos")
        botonConteo.place(x=270,y=230)

        botonSalir = Button(self.frame, text="Salir")
        botonSalir.place(x=310,y=270)

        self.frame.mainloop()


a = Menu()