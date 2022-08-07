from tkinter import *
from tkinter import filedialog



class Menu():

    def __init__(self):
        self.menu = Tk()
        self.menu.title("Menu")
        self.menu.resizable(0,0)
        self.menu.geometry("650x400")
        self.menu.configure(bg="#18b9e4")
        self.container()

    def container(self):
        self.frame = Frame(height=500,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        curso = Label(self.frame,bg="#42d35c" , text="Nombre del curso: Lab. Lenguajer Formales de Programación")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Consolas",13))

        nombre = Label(self.frame,bg="#42d35c" , text="Nombre del estudiante: José Daniel Fuentes Orozco")
        nombre.pack
        nombre.place(x=20,y=40)
        nombre.config(font=("Consolas",13))

        carne = Label(self.frame,bg="#42d35c" , text="Carné del estudiante: 202001228")
        carne.pack
        carne.place(x=20,y=70)
        carne.config(font=("Consolas",13))

        #Botonoes
        botonCarga =  Button(self.frame,bg="#447cb6",font=("Consolas",12),text="Cargar Archivo",command=self.cargarA)
        botonCarga.place(x=225,y=140)

        botonGestionar = Button(self.frame,bg="#447cb6",font=("Consolas",12),text="Gestionar Cursos",command=self.gestionar)
        botonGestionar.place(x=215,y=185)

        botonConteo = Button(self.frame,bg="#447cb6", font=("Consolas",12),text="Conteo de Créditos")
        botonConteo.place(x=208,y=225)

        botonSalir = Button(self.frame,bg="#447cb6",font=("Consolas",12), text="Salir",command=self.menu.destroy)
        botonSalir.place(x=270,y=265)

        self.frame.mainloop()

    def cargarA(self):
        self.menu.destroy()
        CargarArchivo()

    def gestionar(self):
        self.menu.destroy()
        GestionarCurso()

class CargarArchivo():
    def __init__(self):
        self.cargar = Tk()
        self.cargar.title("Seleccionar Archivo")
        self.cargar.resizable(0,0)
        self.cargar.geometry("650x300")
        self.cargar.configure(bg="#18b9e4")
        self.container()

    def container(self):
        self.frame = Frame(height=400,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        textoR = Label(self.frame,bg="#42d35c" , text="Ruta:")
        textoR.pack
        textoR.place(x=20,y=45)
        textoR.config(font=("Consolas",13))

        ruta = Text(self.frame, height = 1, width = 50)
        ruta.place(x=100,y=50)

        seleccionar = Button(self.frame,bg="#42d35c",text="Seleccionar",font=("Consolas",12))
        seleccionar.pack
        seleccionar.place(x=150,y=100)

        regresar = Button(self.frame,bg="#42d35c",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=300,y=100)
        

        self.frame.mainloop()

    def regresar(self):
        self.cargar.destroy()
        Menu()

class GestionarCurso():

    def __init__(self):
        self.gestionar = Tk()
        self.gestionar.title("Gestionar Cursos")
        self.gestionar.resizable(0,0)
        self.gestionar.geometry("450x400")
        self.gestionar.configure(bg="#18b9e4")
        self.container()
    
    def container(self):
        self.frame = Frame(height=400,width=500)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        
        listar = Button(self.frame,bg="#42d35c",text="Listar Cursos",font=("Consolas",12))
        listar.pack
        listar.place(x=150,y=50)

        agregar = Button(self.frame,bg="#42d35c",text="Agregar Cursos",font=("Consolas",12))
        agregar.pack
        agregar.place(x=150,y=100)

        editar = Button(self.frame,bg="#42d35c",text="Editar Cursos",font=("Consolas",12))
        editar.pack
        editar.place(x=150,y=150)
        
        eliminar = Button(self.frame,bg="#42d35c",text="Eliminar Cursos",font=("Consolas",12))
        eliminar.pack
        eliminar.place(x=150,y=200)

        regresar = Button(self.frame,bg="#42d35c",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=150,y=250)

        self.frame.mainloop()

    def regresar(self):
        self.gestionar.destroy()
        Menu()

class ConteoCreditos():

    def __init__(self):
        self.conteo = Tk()
        self.conteo.title("Seleccionar Archivo")
        self.conteo.resizable(0,0)
        self.conteo.geometry("650x300")
        self.conteo.configure(bg="#18b9e4")
        self.container()
    
    def container(self):
        self.frame = Frame(height=400,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        textoR = Label(self.frame,bg="#42d35c" , text="Ruta:")
        textoR.pack
        textoR.place(x=20,y=45)
        textoR.config(font=("Consolas",13))

        ruta = Text(self.frame, height = 1, width = 50)
        ruta.place(x=100,y=50)

        seleccionar = Button(self.frame,bg="#42d35c",text="Seleccionar",font=("Consolas",12))
        seleccionar.pack
        seleccionar.place(x=150,y=100)

        regresar = Button(self.frame,bg="#42d35c",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=300,y=100)
        

        self.frame.mainloop()




a = Menu()