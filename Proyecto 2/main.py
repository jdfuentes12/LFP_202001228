
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from tkinter import filedialog

from Analizador import Automata

analizar_archivo = Automata()

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
        contenido2.add_command(label="Generar página web",command=self.generarPAgina)
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

    def generarPAgina(self):
        contenido = str(self.ingreso.get("1.0",END))
        analizar = open("entrada.txt","w",encoding="utf-8")
        analizar.write(contenido)
        analizar.close()
        print(contenido + "\n")
        
        analizar_archivo.analizador()
        
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

a = Interfaz()
