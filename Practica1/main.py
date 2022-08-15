import code
from mailbox import NoSuchMailboxError
from select import select
from tkinter import *
from tkinter import filedialog
from tkinter import ttk 
import tkinter as tk
from tkinter import font
from traceback import print_tb
from Cursos import Cursos
from tkinter import messagebox
from Analizador import Analizador

#C:\Users\jose2\OneDrive\Escritorio\archivo.lfp
#ruta del archivo  prueba :v

global cursos
global codigo
global nombre
global requisito
global semestre
global opcional
global creditos
global estado
cursos = []
codigo = []
nombre = []
requisito = []
semestre = []
opcional = []
creditos = []
estado = []

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

        botonConteo = Button(self.frame,bg="#447cb6", font=("Consolas",12),text="Conteo de Créditos",command=self.conteo)
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

    def conteo(self):
        self.menu.destroy()
        ConteoCreditos()

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

        self.ruta = Text(self.frame, height = 1, width = 50)
        self.ruta.place(x=100,y=50)

        seleccionar = Button(self.frame,bg="#42d35c",text="Seleccionar",font=("Consolas",12),command=self.leerTexto)
        seleccionar.pack
        seleccionar.place(x=150,y=100)

        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=300,y=100)
        

        self.frame.mainloop()

    def leerTexto(self):
        #obtner el resultado del  TEXT
        resultado = self.ruta.get("1.0","end").replace("\n","")
        
        cursos = self.Analizador(resultado)
        
        for curso in cursos:
            codigo = curso.getCodigo()
            nombre = curso.getNombre()
            requisito = curso.getRequisitos()
            semestre = curso.getSemestre()
            opcional = curso.getOpcional()
            creditos = curso.getCreditos()
            estado = curso.getEstado()
            print(codigo," ",nombre," ",requisito," ",semestre," ",opcional," ",creditos," ",estado)
        
    def Analizador(self, ruta):
        
        try:
            objeto = open(ruta,'r+',encoding='utf-8')
            lineas = objeto.readlines()
            objeto.close()
            
            for linea in lineas:
                data = linea.split(',')
                print(data)
                curso = Cursos(data[0],data[1],data[2],data[3],data[4],data[5],data[6].rsplit('\n'))
                cursos.append(curso)
                
            return cursos
        
        except:
            messagebox.showerror("Error", "El archivo ingresado no es valido \nIntente de nuevo  :)")
            self.ruta.delete("1.0","end")

    def regresar(self):
        self.cargar.destroy()
        Menu()
    
    print("esta en el modulo analizador")
    def AgregarCurso(codigo,nombre,requisito,semestre,opcional,creditos,estado):
        
        curso = Cursos(codigo,nombre,requisito,semestre,opcional,creditos,estado)
        cursos.append(curso)
        messagebox.showinfo("Informacion", "Archivo Cargado con Exito")        
        return cursos

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

        
        listar = Button(self.frame,bg="#447cb6",text="Listar Cursos",font=("Consolas",12),command=self.lista)
        listar.pack
        listar.place(x=150,y=50)

        agregar = Button(self.frame,bg="#447cb6",text="Agregar Cursos",font=("Consolas",12),command=self.agregar)
        agregar.pack
        agregar.place(x=150,y=100)

        editar = Button(self.frame,bg="#447cb6",text="Editar Cursos",font=("Consolas",12))
        editar.pack
        editar.place(x=150,y=150)
        
        eliminar = Button(self.frame,bg="#447cb6",text="Eliminar Cursos",font=("Consolas",12),command=self.eliminar)
        eliminar.pack
        eliminar.place(x=150,y=200)

        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=150,y=250)

        self.frame.mainloop()

    def lista(self):
        self.gestionar.destroy()
        ListaCursos()
    
    def agregar(Self):
        Self.gestionar.destroy()
        AgregarCurso()
        
    def eliminar(self):
        self.gestionar.destroy()
        EliminarCuro()
    
    def regresar(self):
        self.gestionar.destroy()
        Menu()

#todo el codigo de las ventanas de gestionar cursos 
#--------------------------------------INICIO DE GESTION DE CURSOS--------------------------------------------------
class ListaCursos():
    def __init__(self):
        self.lista = Tk()
        self.lista.title("Lista de Cursos")
        self.lista.resizable(1,1)
        self.lista.geometry("750x400")
        self.lista.configure(bg="#18b9e4")
        self.contenido()
        
    def contenido(self):
        self.frame = Frame(height=1000,width=1000)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)
        
        # define columns  
        columns = ('codigo','nombre','pre_requisitos','opcional','semestre','creditos','estado')
        
        tabla = ttk.Treeview(self.frame, columns=columns, show='headings')
        tabla.place(x=100,y=50)
        
        tabla.column('codigo',width=80,anchor=CENTER)
        tabla.column('nombre',width=120,anchor=CENTER)
        tabla.column('pre_requisitos',width=100,anchor=CENTER)
        tabla.column('opcional',width=80,anchor=CENTER)
        tabla.column('semestre',width=80,anchor=CENTER)
        tabla.column('creditos',width=80,anchor=CENTER)
        tabla.column('estado',width=80,anchor=CENTER)
        
        # define headings
        tabla.heading('codigo',text='Código')
        tabla.heading('nombre', text='Nombre')
        tabla.heading('pre_requisitos', text='Pre requisitos')
        tabla.heading('opcional', text='Opcional')
        tabla.heading('semestre', text='Semestre')
        tabla.heading('creditos', text='Créditos')
        tabla.heading('estado', text='Estado')
        
        tabla.grid(row=0, column=0, sticky='nsew')
        tabla.pack
        
        regresar = Button(self.lista,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack 
        regresar.place(x=300,y=300)
        
        #tabla.insert("",END,values=("100","prueba","0","2","0","5","0"))        
        for i in cursos:
            print(codigo," ",nombre," ",requisito," ",semestre," ",opcional," ",creditos," ",estado)
            #tabla.insert("",END,values=(codigo,nombre,requisito,semestre,opcional,creditos,estado))

        self.frame.mainloop()
    
    def regresar(self):
        self.lista.destroy()
        GestionarCurso()

class AgregarCurso():
    def __init__(self):
        print("agregar curso")
        self.agregarV = Tk()
        self.agregarV.title("Agregar Curso")
        self.agregarV.resizable(0,0)
        self.agregarV.geometry("430x500")
        self.agregarV.configure(bg="#18b9e4")
        self.container()
    
    def container(self):
    
        self.frame = Frame(height=500,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)
        
        c = Label(self.frame,bg="#42d35c",text="Código:",font=("Consolas",13))
        c.pack
        c.place(x=30,y=30)
        
        self.codigo = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.codigo.pack
        self.codigo.place(x=180,y=30)
        
        n = Label(self.frame,bg="#42d35c",text="Nombre:",font=("Consolas",13))
        n.pack
        n.place(x=30,y=80)
        
        self.nombre = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.nombre.pack
        self.nombre.place(x=180,y=80)
        
        p = Label(self.frame,bg="#42d35c",text="Pre Requisito:",font=("Consolas",13))
        p.pack
        p.place(x=30,y=130)
        
        self.requisito = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.requisito.pack
        self.requisito.place(x=180,y=130)
        
        s = Label(self.frame,bg="#42d35c",text="Semestre:",font=("Consolas",13))
        s.pack
        s.place(x=30,y=180)
        
        self.semestre = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.semestre.pack
        self.semestre.place(x=180,y=180)
        
        o = Label(self.frame,bg="#42d35c",text="Opcional:",font=("Consolas",13))
        o.pack
        o.place(x=30,y=230)
        
        self.opcional = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.opcional.pack
        self.opcional.place(x=180,y=230)
        
        cr = Label(self.frame,bg="#42d35c",text="Créditos:",font=("Consolas",13))
        cr.pack
        cr.place(x=30,y=280)
        
        self.creditos = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.creditos.pack
        self.creditos.place(x=180,y=280)
        
        e = Label(self.frame,bg="#42d35c",text="Estado:",font=("Consolas",13))
        e.pack
        e.place(x=30,y=330)
        
        self.estado = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.estado.pack
        self.estado.place(x=180,y=330)
        
        agregar = Button(self.frame,bg="#447cb6",text="Agregar",font=("Consolas",12),command=self.agregar)
        agregar.pack
        agregar.place(x=50,y=380)
        
        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=200,y=380)
        
        self.frame.mainloop()
    
    def agregar(self):
        
        codigo = self.codigo.get("1.0","end").replace("\n","")
        nombre = self.nombre.get("1.0","end").replace("\n","")
        requisito = self.requisito.get("1.0","end").replace("\n","")
        semestre = self.semestre.get("1.0","end").replace("\n","")
        opcional = self.opcional.get("1.0","end").replace("\n","")
        creditos = self.creditos.get("1.0","end").replace("\n","")
        estado = self.estado.get("1.0","end").replace("\n","")
        
        print(codigo," ",nombre," ",requisito," ",semestre," ",opcional," ",creditos," ",estado)
        
        cursos = self.agreCurso(codigo,nombre,requisito,semestre,opcional,creditos,estado)
        
        for curso in cursos:
            print(curso.getCodigo()," ",curso.getNombre())
        
        messagebox.showinfo("Información", "Curso Agregado con éxito.")
    
    def agreCurso(self,codigo,nombre,requisito,semestre,opcional,creditos,estado):
        curso = Cursos(codigo,nombre,requisito,semestre,opcional,creditos,estado)
        cursos.append(curso)
        return cursos
    
    def regresar(self):
        self.agregarV.destroy()
        GestionarCurso()

class EditarCurso():
    print("editar")

class EliminarCuro():
    def __init__(self):
        self.eliminar = Tk()
        self.eliminar.title("Eliminar Curso")
        self.eliminar.resizable(0,0)
        self.eliminar.geometry("650x300")
        self.eliminar.configure(bg="#18b9e4")
        self.container()

    def container(self):
        self.frame = Frame(height=400,width=600)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)

        textoR = Label(self.frame,bg="#42d35c" , text="Código de Curso:")
        textoR.pack
        textoR.place(x=20,y=45)
        textoR.config(font=("Consolas",13))

        self.ruta = Text(self.frame, height = 1, width = 25)
        self.ruta.place(x=200,y=50)

        eliminar = Button(self.frame,bg="#42d35c",text="Seleccionar",font=("Consolas",12))
        eliminar.pack
        eliminar.place(x=150,y=100)

        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=300,y=100)
        

        self.frame.mainloop()
        
    def regresar(self):
        self.eliminar.destroy()
        GestionarCurso()
#--------------------------------------Fin de Gestionar Cursos-------------------------------------------

class ConteoCreditos():

    def __init__(self):
        self.conteo = Tk()
        self.conteo.title("Conteo de Creditos")
        self.conteo.resizable(0,0)
        self.conteo.geometry("650x500")
        self.conteo.configure(bg="#18b9e4")
        self.container()
    
    def container(self):
        self.frame = Frame(height=550,width=650)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)


        aprobados = Label(self.frame,bg="#42d35c",text="Créditos Aprobados:",font=("Consolas",13))
        aprobados.pack
        aprobados.place(x=20,y=20)


        cursado = Label(self.frame,bg="#42d35c" , text="Créditos Cursando:",font=("Consolas",13))
        cursado.pack
        cursado.place(x=20,y=70)
        
        pendientes = Label(self.frame,bg="#42d35c",text="Créditos Pendientes", font=("Consolas",13))
        pendientes.pack
        pendientes.place(x=20,y=120)

        obligatorios = Label(self.frame,bg="#42d35c",text="Créditos Obligatorios hasta semestre N:",font=("Consolas",13))
        obligatorios.pack
        obligatorios.place(x=20,y=170)

        obligariosCreditos = Text(self.frame, height = 1, width = 10)
        obligariosCreditos.place(x=400,y=170)
        
        osemestre = Label(self.frame,bg="#42d35c",text="Semestre",font=("Consolas",13))
        osemestre.pack
        osemestre.place(x=50,y=220)

        csemestre=Label(self.frame,bg="#42d35c",text="Créditos del semestre:",font=("Consolas",13))
        csemestre.pack
        csemestre.place(x=20,y=270)

        cretidosSemestre = Text(self.frame,height=1,width=10)
        cretidosSemestre.place(x=250,y=270)

        csemestre = Label(self.frame,bg="#42d35c",text="Semestre",font=("Consolas",13))
        csemestre.pack
        csemestre.place(x=50,y=320)

        regresar = Button(self.frame,text="Regresa",bg="#447cb6",font=("Consolas",13),command=self.regresar)
        regresar.pack
        regresar.place(x=480,y=370)

        
        combo = ttk.Combobox(values=["1","2","3","4","5","6","7","8","9","10","11","12"])
        #codigo para realizar la accion despues de seleccionar una de las opcciones
        #combo.bind("<<ComboboxSelected>>", selection_changed)
        combo.place(x=200,y=250)
        
        combo1 = ttk.Combobox(values=["1","2","3","4","5","6","7","8","9","10","11","12"])
        #codigo para realizar la accion despues de seleccionar una de las opcciones
        #combo.bind("<<ComboboxSelected>>", selection_changed)
        combo1.place(x=200,y=350)

        
        self.frame.mainloop()

    def regresar(self):
        self.conteo.destroy()
        Menu()

class IngresarCurso():
    
    def __init__(self,codigo,nombre,requisito,semestre,opcional,creditos,estado):
        global cursos
        
        curso = Cursos(codigo,nombre,requisito,semestre,opcional,creditos,estado)
        cursos.append(curso)
        return cursos

a = Menu()
