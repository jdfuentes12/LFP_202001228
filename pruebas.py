from msilib.schema import Class
from tkinter import *


class Menu():

    def __init__(self):
        #print("estoy aca")
        self.ventana = Tk()
        self.ventana.title("Menu")
        self.ventana.resizable(0,0)
        self.ventana.geometry("650x350")
        self.ventana.configure(bg="#1c1672")
        #print("estoy aca-")

        '''curso = Label(self.ventana, text="Nombre del curso: Lab. Lenguajer Formales de Programación")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Arial Rounded MT Bold",13))
        
        self.frame = Frame(height=500,width=350)
        nombre = Label(self.ventana, text="Nombre del estudiante: José Daniel Fuentes Orozco")
        nombre.pack
        nombre.place(x=20,y=40)
        nombre.config(font=("Arial Rounded MT Bold",13))

        carne = Label(self.ventana, text="Carné del estudiante: 202001228",font=("Arial Rounded MT Bold",13))
        carne.pack
        carne.place(x=20,y=70)
        carne.config(font=("Arial Rounded MT Bold",13))

        botonCarga =  Button(self.ventana,text="Cargar Archivo")
        botonCarga.place(x=280,y=150)

        botonGestionar = Button(self.ventana,text="Gestionar Cursos")
        botonGestionar.place(x=275,y=190)

        botonConteo = Button(self.ventana, text="Conteo de Créditos")
        botonConteo.place(x=270,y=230)

        botonSalir = Button(self.ventana, text="Salir")
        botonSalir.place(x=310,y=270)'''

        self.botones()

        
        self.ventana.mainloop()



#FALTA EVALUAR PARA QUE LLAME AL FRAME
#-------------------------------------------------------------------------
    def botones(self):
        self.frame = Frame

        curso = Label(self.frame, text="Nombre del curso: Lab. Lenguajer Formales de Programación")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Arial Rounded MT Bold",13))

        nombre = Label(self.frame, text="Nombre del estudiante: José Daniel Fuentes Orozco")
        nombre.pack
        nombre.place(x=20,y=40)
        nombre.config(font=("Arial Rounded MT Bold",13))

        carne = Label(self.frame, text="Carné del estudiante: 202001228",font=("Arial Rounded MT Bold",13))
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

        self.ventana.mainloop()

'''    def container(self):
        self.frame = Frame(height=550,width=350)
        self.frame.config("#ff19ff")
        self.frame.pack(padx=25,pady=25)



        curso = Label(self.frame, text="Nombre del curso: Lab. Lenguajer Formales de Programación")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Arial Rounded MT Bold",13))

        nombre = Label(self.frame, text="Nombre del estudiante: José Daniel Fuentes Orozco")
        nombre.pack
        nombre.place(x=20,y=40)
        nombre.config(font=("Arial Rounded MT Bold",13))

        carne = Label(self.frame, text="Carné del estudiante: 202001228",font=("Arial Rounded MT Bold",13)).place(x=20,y=70)
        carne.pack
        carne.place(x=20,y=70)
        carne.config(font=("Arial Rounded MT Bold",13))
        self.frame.mainloop()
'''

class GestionarCurso():
    def __init__(self):
        self.ventana = Tk()





#llama a la funcion de menú
Menu()