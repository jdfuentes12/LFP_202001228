from tkinter import *
from tkinter import ttk
from Cursos import Cursos
from tkinter import messagebox

#C:\Users\jose2\OneDrive\Escritorio\archivo.lfp

global cursos
cursos = []


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
            opcional = curso.getOpcional()
            semestre = curso.getSemestre()
            creditos = curso.getCreditos()
            estado = curso.getEstado()
            print(codigo,"\t",nombre,"\t",requisito,"\t",opcional,"\t",semestre,"\t",creditos,"\t",estado)
        
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
    def AgregarCurso(codigo,nombre,requisito,opcional,semestre,creditos,estado):
        
        curso = Cursos(codigo,nombre,requisito,opcional,semestre,creditos,estado)
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

        editar = Button(self.frame,bg="#447cb6",text="Editar Cursos",font=("Consolas",12),command=self.editar)
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
    
    def editar(self):
        self.gestionar.destroy()
        EditarCurso()
#todo el codigo de las ventanas de gestionar cursos 
#--------------------------------------INICIO DE GESTION DE CURSOS--------------------------------------------------
class ListaCursos():
    def __init__(self):
        self.lista = Tk()
        self.lista.title("Lista de Cursos")
        self.lista.resizable(1,1)
        self.lista.geometry("800x400")
        self.lista.configure(bg="#18b9e4")
        self.contenido()
        
    def contenido(self):
        self.frame = Frame(height=850,width=800)
        self.frame.config(bg="#00e4ce")
        self.frame.pack(padx=25,pady=25)
        
        # define columns  
        columns = ['codigo','nombre','pre_requisitos','opcional','semestre','creditos','estado']
        
        tabla = ttk.Treeview(self.frame, columns=columns, show='headings')
        #tabla.place(x=100,y=50)
        
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
        
        visual_drag = ttk.Treeview(self.frame,columns=columns,show='headings')
        
        for cols in columns:
            tabla.heading(cols,text=cols)
            visual_drag.heading(cols,text=cols)
        
        curso = 0
        
        for i in cursos:
            tabla.insert('','end',iid='line%i'% i,
                        values=(curso.getCodigo(),curso.getNombre(),curso.getRequisitos(),curso.getSemestre(),curso.getOpcional(),curso.getCreditos(),curso.getEstado()))
            visual_drag.insert('','end',idd='line%i' % i,
                        values=(curso.getCodigo(),curso.getNombre(),curso.getRequisitos(),curso.getSemestre(),curso.getOpcional(),curso.getCreditos(),curso.getEstado()))
            curso = curso + 1
        tabla.grid()
        
        regresar = Button(self.lista,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack 
        regresar.place(x=300,y=300)
        
        tabla.insert("",END,values=("100","prueba","0","2","0","5","0"))        
        

        self.frame.mainloop()
    
    def regresar(self):
        self.lista.destroy()
        GestionarCurso()

class AgregarCurso():
    def __init__(self):
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
        
        s = Label(self.frame,bg="#42d35c",text="Opcional:",font=("Consolas",13))
        s.pack
        s.place(x=30,y=180)
        
        self.opcional = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.opcional.pack
        self.opcional.place(x=180,y=180)
        
        o = Label(self.frame,bg="#42d35c",text="Semetre:",font=("Consolas",13))
        o.pack
        o.place(x=30,y=230)
        
        self.semestre = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.semestre.pack
        self.semestre.place(x=180,y=230)
        
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
        
        codigoA = self.codigo.get("1.0","end").replace("\n","")
        nombreA = self.nombre.get("1.0","end").replace("\n","")
        requisitoA = self.requisito.get("1.0","end").replace("\n","")
        semestreA = self.semestre.get("1.0","end").replace("\n","")
        opcionalA = self.opcional.get("1.0","end").replace("\n","")
        creditosA = self.creditos.get("1.0","end").replace("\n","")
        estadoA = self.estado.get("1.0","end").replace("\n","")
        
        print(codigoA," ",nombreA," ",requisitoA," ",semestreA," ",opcionalA," ",creditosA," ",estadoA)
        
        cursos = self.agreCurso(codigoA,nombreA,requisitoA,semestreA,opcionalA,creditosA,estadoA)
        
        analizador = 0
        
        for curso in cursos:
            if (analizador == 0):
                if (codigoA == curso.getCodigo()):
                    analizador = 1
                    print("CURSO YA EXISTENTE")
                    messagebox.showwarning("Advertencia", "Curso ya existente en la base de datos.\nIntente nuevamente")
            print(curso.getCodigo()," ",curso.getNombre())
        
        if (analizador == 0):
            cursos = self.agreCurso(codigoA,nombreA,requisitoA,semestreA,opcionalA,creditosA,estadoA)
            for curso in cursos:
                print(curso.getCodigo()," ",curso.getNombre())
                
            self.codigo.delete("1.0","end")
            self.nombre.delete("1.0","end")
            self.requisito.delete("1.0","end")
            self.semestre.delete("1.0","end")
            self.opcional.delete("1.0","end")
            self.creditos.delete("1.0","end")
            self.estado.delete("1.0","end")
            messagebox.showinfo("Información", "Curso Agregado con éxito.")
        
    def agreCurso(self,codigo,nombre,requisito,opcional,semestre,creditos,estado):
        curso = Cursos(codigo,nombre,requisito,opcional,semestre,creditos,estado)
        cursos.append(curso)
        return cursos
    
    def regresar(self):
        self.agregarV.destroy()
        GestionarCurso()

class EditarCurso():
    def __init__(self):
        self.eliminar = Tk()
        self.eliminar.title("Eliminar Curso")
        self.eliminar.resizable(0,0)
        self.eliminar.geometry("500x550")
        self.eliminar.configure(bg="#18b9e4")
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
        
        editar = Button(self.frame,bg="#447cb6",text="Editar",font=("Consolas",12))
        editar.pack
        editar.place(x=50,y=380)
        
        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=200,y=380)
        
        self.frame.mainloop()
        
    def editar(self):
        contenido = self.codigo.get("1.0","end").replace("\n","")
        
        codigoE = self.codigo.get("1.0","end").replace("\n","")
        nombreE = self.nombre.get("1.0","end").replace("\n","")
        requisitoE = self.requisito.get("1.0","end").replace("\n","")
        semestreE = self.semestre.get("1.0","end").replace("\n","")
        opcionalE = self.opcional.get("1.0","end").replace("\n","")
        creditosE = self.creditos.get("1.0","end").replace("\n","")
        estadoE = self.estado.get("1.0","end").replace("\n","")
        
        self.evaluacion = 0
        
        for curso in cursos:
            if(self.evaluacion == 0):
                if(contenido == curso.getCodigo()):
                    self.evaluacion = 1
                    curso.getCodigo 
                    messagebox.showinfo("Información","El curso seleccionado es valido")
        
        if (self.evaluacion == 0):
            messagebox.showerror("Error", "Curso no encontrado en la base de datos")
    
    def editar(self):
        print("EDITANDO CURSO")
        codigoE = self.codigo.get("1.0","end").replace("\n","")
        nombreE = self.nombre.get("1.0","end").replace("\n","")
        requisitoE = self.requisito.get("1.0","end").replace("\n","")
        semestreE = self.semestre.get("1.0","end").replace("\n","")
        opcionalE = self.opcional.get("1.0","end").replace("\n","")
        creditosE = self.creditos.get("1.0","end").replace("\n","")
        estadoE = self.estado.get("1.0","end").replace("\n","")
    

    def regresar(self):
        self.eliminar.destroy()
        GestionarCurso()

class Edicion():
    def __init__(self):
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
        
        s = Label(self.frame,bg="#42d35c",text="Opcional:",font=("Consolas",13))
        s.pack
        s.place(x=30,y=180)
        
        self.opcional = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.opcional.pack
        self.opcional.place(x=180,y=180)
        
        o = Label(self.frame,bg="#42d35c",text="Semetre:",font=("Consolas",13))
        o.pack
        o.place(x=30,y=230)
        
        self.semestre = Text(self.frame,height=1,width=20,font=("Consolas",13))
        self.semestre.pack
        self.semestre.place(x=180,y=230)
        
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
        
        codigoA = self.codigo.get("1.0","end").replace("\n","")
        nombreA = self.nombre.get("1.0","end").replace("\n","")
        requisitoA = self.requisito.get("1.0","end").replace("\n","")
        semestreA = self.semestre.get("1.0","end").replace("\n","")
        opcionalA = self.opcional.get("1.0","end").replace("\n","")
        creditosA = self.creditos.get("1.0","end").replace("\n","")
        estadoA = self.estado.get("1.0","end").replace("\n","")
        
        print(codigoA," ",nombreA," ",requisitoA," ",semestreA," ",opcionalA," ",creditosA," ",estadoA)
        
        cursos = self.agreCurso(codigoA,nombreA,requisitoA,semestreA,opcionalA,creditosA,estadoA)
        
        analizador = 0
        
        for curso in cursos:
            if (analizador == 0):
                if (codigoA == curso.getCodigo()):
                    analizador = 1
                    print("CURSO YA EXISTENTE")
                    messagebox.showwarning("Advertencia", "Curso ya existente en la base de datos.\nIntente nuevamente")
            print(curso.getCodigo()," ",curso.getNombre())
        
        if (analizador == 0):
            cursos = self.agreCurso(codigoA,nombreA,requisitoA,semestreA,opcionalA,creditosA,estadoA)
            for curso in cursos:
                print(curso.getCodigo()," ",curso.getNombre())
                
            self.codigo.delete("1.0","end")
            self.nombre.delete("1.0","end")
            self.requisito.delete("1.0","end")
            self.semestre.delete("1.0","end")
            self.opcional.delete("1.0","end")
            self.creditos.delete("1.0","end")
            self.estado.delete("1.0","end")
            messagebox.showinfo("Información", "Curso Agregado con éxito.")
        
    def agreCurso(self,codigo,nombre,requisito,opcional,semestre,creditos,estado):
        curso = Cursos(codigo,nombre,requisito,opcional,semestre,creditos,estado)
        cursos.append(curso)
        return cursos
    
    def regresar(self):
        self.agregarV.destroy()
        GestionarCurso()

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

        eliminar = Button(self.frame,bg="#42d35c",text="Seleccionar",font=("Consolas",12),command=self.eliminarCurso)
        eliminar.pack
        eliminar.place(x=150,y=100)

        regresar = Button(self.frame,bg="#447cb6",text="Regresar",font=("Consolas",12),command=self.regresar)
        regresar.pack
        regresar.place(x=300,y=100)
        

        self.frame.mainloop()
        
    def eliminarCurso(self):
        print("ELIMINAR CURSO")
        cursoEliminar = self.ruta.get("1.0","end").replace("\n","")
        print(cursoEliminar)
        
        evaluacion = 0
        contador = 0
        for curso in cursos:
            if(evaluacion == 0):
                
                if (cursoEliminar == curso.getCodigo()):
                    print(curso.getNombre())
                    evaluacion = 1
                    eliminadoC = curso.getNombre()
                    messagebox.showinfo("Información",("Curso", eliminadoC," fue eliminado con éxito."))
                    cursos.pop(contador)
                    
                    for curso in cursos:
                        codigo = curso.getCodigo()
                        nombre = curso.getNombre()
                        requisito = curso.getRequisitos()
                        opcional = curso.getOpcional()
                        semestre = curso.getSemestre()
                        creditos = curso.getCreditos()
                        estado = curso.getEstado()
                        print(codigo,"\t",nombre,"\t",requisito,"\t",opcional,"\t",semestre,"\t",creditos,"\t",estado)
                    break
            contador = contador + 1

        if (evaluacion == 0 ):
            print("EL CURSO NO ESTA EN LA BASE DE DATOS")
            messagebox.showinfo("Error", "Curso no encontrado en la base de datos")
        
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

        self.aprobadosLabel = Label(self.frame,bg="#2e77d9",font=("Consolas",13))
        self.aprobadosLabel.pack
        self.aprobadosLabel.place(x=220,y=20)
        
        cursado = Label(self.frame,bg="#42d35c" , text="Créditos Cursando:",font=("Consolas",13))
        cursado.pack
        cursado.place(x=20,y=70)
        
        self.cursandoLabel = Label(self.frame,bg="#2e77d9",font=("Consolas",13))
        self.cursandoLabel.pack
        self.cursandoLabel.place(x=220,y=70)
        
        pendientes = Label(self.frame,bg="#42d35c",text="Créditos Pendientes", font=("Consolas",13))
        pendientes.pack
        pendientes.place(x=20,y=120)
        
        self.pendientesLabel = Label(self.frame,bg="#2e77d9",font=("Consolas",13))
        self.pendientesLabel.pack
        self.pendientesLabel.place(x=220,y=120)

        obligatorios = Label(self.frame,bg="#42d35c",text="Créditos Obligatorios hasta semestre N:",font=("Consolas",13))
        obligatorios.pack
        obligatorios.place(x=20,y=170)
        
        self.obligatirios = Label(self.frame,bg="#2e77d9",text="Esperando...",font=("Consolas",13))
        self.obligatirios.pack
        self.obligatirios.place(x=400,y=170)
        
        
        osemestre = Label(self.frame,bg="#42d35c",text="Semestre",font=("Consolas",13))
        osemestre.pack
        osemestre.place(x=50,y=220)

        csemestre=Label(self.frame,bg="#42d35c",text="Créditos del semestre:",font=("Consolas",13))
        csemestre.pack
        csemestre.place(x=20,y=270)
        
        self.creditosSemestre = Label(self.frame,bg="#2e77d9",text="Esperando...",font=("Consolas",13))
        self.creditosSemestre.pack
        self.creditosSemestre.place(x=250,y=270)
        
        csemestre = Label(self.frame,bg="#42d35c",text="Semestre",font=("Consolas",13))
        csemestre.pack
        csemestre.place(x=50,y=320)

        regresar = Button(self.frame,text="Regresa",bg="#447cb6",font=("Consolas",13),command=self.regresar)
        regresar.pack
        regresar.place(x=500,y=365)
        
        self.combo = ttk.Combobox(self.frame,values=["1","2","3","4","5","6","7","8","9","10","11","12"])
        self.combo.place(x=200,y=220)
        
        self.conteoO = Button(self.frame,text="Conteo",bg="#23a0b5",font=("Consolas",13),command=self.conteoObligatorios)
        self.conteoO.pack
        self.conteoO.place(x=375,y=215)
        
        self.combo1 = ttk.Combobox(self.frame,values=["1","2","3","4","5","6","7","8","9","10","11","12"])
        self.combo1.place(x=200,y=320)
        
        self.conteoS = Button(self.frame,text="Conteo S",bg="#23a0b5",font=("Consolas",13),command=self.conteoSemestre)
        self.conteoS.pack
        self.conteoS.place(x=375,y=315)
        
        
        conteoAprobados = 0
        conteoCursando = 0
        conteoPendiente = 0
        print("hola")
        
        for curso in cursos:
            estado = int(curso.getEstado())
            if (estado == 0):
                conteoAprobados = conteoAprobados + 1
            elif (estado == 1):
                conteoCursando = conteoCursando + 1
        
        for curso in cursos:
            if curso.getOpcional() == "1":
                estado = curso.getEstado()
                if estado == "-1":
                    conteoPendiente = conteoPendiente + 1
        
        print(conteoAprobados," ",conteoCursando," ",conteoPendiente)
        
        self.aprobadosLabel['text'] = conteoAprobados
        self.cursandoLabel['text'] = conteoCursando
        self.pendientesLabel['text'] = conteoPendiente
        
        self.frame.mainloop()

    def regresar(self):
        self.conteo.destroy()
        Menu()
    
    def conteoObligatorios(self):
        try:
            seleccionado = self.combo.get()
            contarCreditos = 0
            limite = int(seleccionado)
            if seleccionado != "":
                for curso in cursos:
                    if curso.getOpcional() == "1":
                        if (int(curso.getSemestre()) <= limite):
                            contarCreditos = int(curso.getCreditos()) + contarCreditos
            else:
                messagebox.showerror("Error", "Seleccione un semestre a evaluar.\nO valor ingresado no obtenido en la base de datos.")
                
            
            self.obligatirios['text'] = contarCreditos
        except:
            messagebox.showerror("Error", "Ningun valor seleccionado")
    
    def conteoSemestre(self):
        try:
            seleccionado = self.combo1.get()
            print("usted selecciono ",seleccionado)
            contadorAprobados = 0
            contadorCursando = 0
            contadorPendiente = 0
            
            for curso in cursos:
                if curso.getOpcional() == "0":
                    contadorAprobados = int(curso.getCreditos()) + contadorAprobados
                elif curso.getOpcional() == "1":
                    contadorCursando = contadorCursando + int(curso.getCreditos())
                elif curso.getOpcional() == "-1":
                    contadorPendiente = contadorPendiente + int(curso.getCreditos())
            
            self.aprobadosLabel['text'] = contadorAprobados
            self.cursandoLabel['text'] = contadorCursando
            self.pendientesLabel['text'] = contadorPendiente
            
        except:
            messagebox.showerror("Error", "Ningun valor seleccionado")

a = Menu()