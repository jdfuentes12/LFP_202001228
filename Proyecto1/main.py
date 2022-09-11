from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

class Principal():
    
    def __init__(self):
        self.menu = Tk()
        self.menu.title("Analizador  Lexico")
        self.menu.resizable(0,0)
        self.menu.geometry("450x250+500+250")
        self.menu.configure(bg="#214457")
        self.container()

    def container(self):
        self.frame = Frame(height=200,width=400)
        self.frame.config(bg="#114e64")
        self.frame.pack(padx=20,pady=20)

        curso = Label(self.frame,bg="#007389" , text="Bienvenido al analizador de texto")
        curso.pack
        curso.place(x=20,y=10)
        curso.config(font=("Consolas",13))

        #Botonoes
        botonIniciar =  Button(self.frame,bg="#006f98",font=("Consolas",12),text="Iniciar",command=self.inicio)
        botonIniciar.place(x=175,y=75)

        botonSalir =  Button(self.frame,bg="#006f98",font=("Consolas",12),text="Salir",command=self.salir)
        botonSalir.place(x=183,y=125)
        
        self.frame.mainloop()
    
    def salir(self):
        self.menu.destroy()
        
    def inicio(self):
        self.menu.destroy()
        Intefaz()

class Intefaz():
        
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Analizador léxico")
        self.ventana.resizable(0,0)
        self.ventana.geometry("1200x700+150+50")
        self.ventana.configure(bg="#214457")
        
        #PRIMER BARRA
        barraMenu = Menu(self.ventana)
        contenido  = Menu(barraMenu)
        contenido.add_command(label="Abrir",command=self.abrir)
        contenido.add_command(label="Guardar")
        contenido.add_command(label="Guardar Como",command=self.guardarComo)
        contenido.add_command(label="Analizar")
        contenido.add_command(label="Errores")
        contenido.add_separator()
        contenido.add_command(label="Salir",command=self.salir)
        barraMenu.add_cascade(label="Archivo",menu=contenido)
        self.ventana.config(menu=barraMenu)
        
        #SEGUNDA BARRA
        
        contenido2  = Menu(barraMenu)
        contenido2.add_command(label="Manual de Usuario",command=self.manualUsuario)
        contenido2.add_command(label="Manual de Técnico")
        contenido2.add_command(label="Temas de  Ayuda")
        
        barraMenu.add_cascade(label="Ayuda",menu=contenido2)
        self.ventana.config(menu=barraMenu)
        
        self.contenido = Text(self.ventana, height = 40, width = 143)
        self.contenido.place(x=25,y=25)
        
        self.ventana.mainloop()
    
    def abrir(self):
        
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[('Archivos', '.txt'), # -> concatena -> *.data o *.lfp
                                                        ('All Files', '*')])
            # print(filename)
            with open(filename, encoding='utf-8') as infile:
                x = infile.read().strip()
                print(x)
                self.contenido.insert(1.0,x)
        except:
            messagebox.showerror("Error", "Archivo incorrecto")
            return
    
    def salir(self):
        self.ventana.destroy()
    
    def manualTecnico(self):
        pass

    def manualUsuario(self):
        wb.open_new(r'E:\Documentos\USAC\LFP\LFP_202001228\Proyecto1\MANUALES\Manual Usuario.pdf')

    def guardarComo(self):
        file = filedialog.asksaveasfile(filetypes=[
                                            ("txt file", ".txt"),
                                            ("Html file", ".html"),
                                            ("Documento",".doc"),
                                            ("Imagen jpg",".jpg"),
                                            ("Imagen png",".png"),
                                            ("Lectura (PDF)",".pdf"),
                                            ("All files",".*")],
                                        defaultextension=".txt")
        filetext = str(self.contenido.get(1.0,END))
        file.write(filetext)
        file.close()

    def guardar(self):
        pass
#a = Intefaz()
a = Principal()
