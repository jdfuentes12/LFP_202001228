from array import array
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog
global contenedor
global boton
global clave
global etiqueta
global texto
contenedor = []
boton = []
clave = []
etiqueta = []
texto = []
global contenido
contenido = 0
global propiedades
propiedades = []



class Interfaz:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Analizador léxico")
        self.ventana.resizable(0,0)
        self.ventana.geometry("1200x700+150+50")
        self.ventana.configure(bg="#214457")
        
        #ARCHIVO
        barraMenu = Menu(self.ventana)
        contenido  = Menu(barraMenu)
        contenido.add_command(label="Nuevo",command=self.nuevo)
        contenido.add_command(label="Abrir",command=self.abrir)
        contenido.add_command(label="Guardar")
        contenido.add_command(label="Guardar como")
        contenido.add_separator()
        contenido.add_command(label="Salir")
        barraMenu.add_cascade(label="Archivo",menu=contenido)
        self.ventana.config(menu=barraMenu)
        
        #GENERADOR DE PAGINA
        contenido2  = Menu(barraMenu)
        contenido2.add_command(label="Generar página web",command=self.generarPagina)
        barraMenu.add_cascade(label="Análizador",menu=contenido2)
        self.ventana.config(menu=barraMenu)
        
        
        #TOKENS
        contenido3 = Menu(barraMenu)
        contenido3.add_command(label="Tokens")
        barraMenu.add_cascade(label="Tokens",menu=contenido3)
        self.ventana.config(menu=barraMenu)
        
        #ERRORES
        contenido4 = Menu(barraMenu)
        contenido4.add_command(label="Errores")
        barraMenu.add_cascade(label="Errores",menu=contenido4)
        self.ventana.config(menu=barraMenu)
        
        self.ingreso = Text(self.ventana, height = 40, width = 143)
        self.ingreso.place(x=25,y=25)
        
        self.ventana.mainloop()

    def nuevo(self):
        x = ""
        Tk().withdraw()
        print("este es el contenido: ",self.ingreso.get("1.0",END))
        temp = self.ingreso.get("1.0",END)
        
        if temp == "\n":
            try:
                filename = askopenfilename(title='Selecciona un archivo',
                                                filetypes=[ # -> concatena -> *.data o *.lfp
                                                            ('GPW', '.gpw')])
                #print(filename)
                with open(filename, encoding='utf-8') as infile:
                    x = infile.read().strip()
                    
                    examinar = x
                    self.ingreso.insert(1.0,x)
            except:
                messagebox.showerror("Error", "Archivo incorrecto")
                return
        
        
        if temp != "":
            #messagebox.showinfo("Nuevo\n","¿Desea guardar los cambios?")
            print("guardar")
            file = filedialog.asksaveasfile(filetypes=[("GPW", ".gpw")],
                                            defaultextension=".gpw")
            filetext = (self.ingreso.get(1.0,END)) 
            print(filetext)
            file.write(filetext)
            file.close() 
            self.limpiar()

    def limpiar(self):
        self.ingreso.delete('1.0','end')

    def abrir(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[ # -> concatena -> *.data o *.lfp
                                                        ('GPW', '.gpw')])
            # print(filename)
            with open(filename, encoding='utf-8') as infile:
                x = infile.read().strip()
                self.ingreso.insert(1.0,x)
        except:
            messagebox.showerror("Error", "Archivo incorrecto")

class Atuomatico:
    def __init__(self):
        self.columna = 0
        self.fila = 0
        self.estado = 0
        
    def analizador(self):
        archivo = open("entrada.gpw","r")
        contenido = archivo.readlines()
        lexema = ""
        for linea in contenido:
            self.fila += 1
            self.columna = 0
            validar = 0
            opcion = 0
            for caracter in linea:
                self.columna += 1
                if caracter == "\t":
                    continue
                
                if self.estado == 0:
                    if caracter == "<":
                        self.estado = 1
                
                if self.estado == 1:
                    if caracter == "!":
                        self.estado = 2
                
                if self.estado == 2:
                    if caracter == "-":
                        self.estado = 2
                        validar += 1
                        if validar == 2:
                            self.estado = 3
                
                if self.estado == 3:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        propiedades.append(lexema)
                        lexema = ""
                        for i in propiedades:
                            if i == 'Controles':
                                self.estado = 4
                                opcion = 0
                                print(self.estado)
                            elif i == 'propiedades':
                                self.estado = 5
                            elif i == 'Colocacion':
                                self.estado = 6
                
                if self.estado == 4:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema == 'Contenedor':
                            self.estado = 5
                            opcion = 0
                            lexema = ""
                        if lexema == 'Boton':
                            self.estado = 6
                            opcion = 0
                            lexema = ""
                        if lexema == 'Clave':
                            self.estado = 7
                            opcion = 0
                            lexema = ""
                        if lexema == 'Texto':
                            self.estado = 8
                            opcion = 0
                            lexema = ""
                        if lexema == 'Etiqueta':
                            self.estado = 9
                            opcion = 0
                            lexema = ""
                        if lexema == 'Controles':
                            self.estado = 10
                            opcion = 0
                            lexema = ""
                
                if self.estado == 5:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        contenedor.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 6:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        boton.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 7:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        clave.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 8:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        texto.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 9:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        etiqueta.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 10:
                    if caracter == "-":
                        self.estado = 10
                        validar += 1
                        if validar == 2:
                            self.estado = 11
                
                if self.estado == 11:
                    if caracter == ">":
                        self.estado = 1
                
a = Atuomatico()
a.analizador() 

#b = Interfaz()