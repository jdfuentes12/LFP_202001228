from array import array
from http.cookiejar import LWPCookieJar
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog

global check
global radiobutton
global contenedor
global areaTexto
global boton
global clave
global etiqueta
global texto

global contenido
global propiedades

areaTexto = []
radiobutton = []
check = []
contenedor = []
boton = []
clave = []
etiqueta = []
texto = []
contenido = 0
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
        self.htmlEncabezado()
        self.css = open('estilo.css','w')
        contenido = archivo.readlines()
        lexema = ""
        for linea in contenido:
            self.fila += 1
            self.columna = 0
            validar = 0
            opcion = 0
            condicion = 0
            tmp = ''
            validar2 = False
            validar3 = False
            color = []
            for caracter in linea:
                #self.comentario(linea)
                self.columna += 1
                
                if self.comentario(linea) == True:
                    break

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
                            elif i == 'propiedades':
                                self.estado = 18
                            elif i == 'Colocacion':
                                self.estado = None
                
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
                            self.estado = 13
                            opcion = 0
                            lexema = ""
                        if lexema == 'Check':
                            self.estado = None
                            opcion = 0
                            lexema = ""
                        if lexema == 'RadioBoton':
                            self.estado = None
                            opcion = 0
                            lexema = ""
                        if lexema == 'AreaTexto':
                            self.estado = None
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
                    pass
                
                if self.estado == 11:
                    pass
                
                if self.estado == 12:
                    pass
                
                if self.estado == 13:
                    if caracter == "-":
                        self.estado = 13
                        validar += 1
                        if validar == 2:
                            self.estado = 14
                
                if self.estado == 14:
                    if caracter == ">":
                        self.estado = 15
                
                if self.estado == 15:
                    if caracter == "<":
                        self.estado = 16
                
                if self.estado == 16:
                    if caracter == "!":
                        self.estado = 17
                
                if self.estado == 17:
                    if caracter == "-":
                        self.estado = 17
                        validar += 1
                        if validar == 2:
                            self.estado = 3
                
                if self.estado == 18:
                    
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        for i in contenedor:
                            if lexema == i:
                                self.estado = 19
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                #contenedor
                if self.estado == 19:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema  == 'setAncho':
                            validar = True
                            lexema = ''
                            opcion = 0
                        
                        if validar == True:
                            if lexema != '':
                                self.setAncho(tmp,lexema)
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setAlto':
                            validar2 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar2 == True:
                            if lexema != '':
                                self.setAlto(tmp,lexema)
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setColorFondo':
                            validar3 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar3 == True:
                            if lexema != '':
                                color.append(lexema)
                                lexema = ''
                                if len(color) == 3:
                                    self.setColorFondo(tmp,color)
                                    lexema = ''
                                    self.estado = 18
                
            
    def setAncho(self,control,tamaño):
        
        self.css.write(control + '{\n')
        self.css.write('width: ' + tamaño + 'px;\n')
        self.css.write('}\n')
    
    def setAlto(self,control,tamaño):
        self.css.write(control + '{\n')
        self.css.write('height: ' + tamaño + 'px;\n')
        self.css.write('}\n')
    
    def setColorFondo(self,control,color):
        self.css.write(control + '{\n')
        self.css.write('background-color: rgb(' )
        
        for i in color:
            self.css.write(i + ',')
        self.css.write(');\n')
        
        self.css.write('}\n')
    
    def comentario(self,linea):

        cadena = linea.replace(" ","")
        contador = len(cadena)
        
        if cadena[0] == '/' and cadena[1] == '/':
            return True
        if cadena[0] == '/' and cadena[1] == '*' and cadena[contador-3] == '*' and cadena[contador-2] == '/':
            return True
        else:
            return False

    def htmlEncabezado(self):
        archivo = open('index.html','w')
        archivo.write('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" type="estilo.css" href="URL">
</head>
<body>
''')

a = Atuomatico()
a.analizador() 

#b = Interfaz()