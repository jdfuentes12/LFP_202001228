from texto import Texto
from numero import Numero 
from aritmeticas import Aritmeticas 
from operador import Operador 
from errores import Errores
from estilo import Estilo
from funcion import Funcion

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import webbrowser as wb

tokens = (
    'RESTILO',
    'ROPERACIONES',
    'RTIPO',
    'RTEXTO',
    'RTIPO2',
    'RTEXTO2',
    'RFUNCION',
    'RTITULO',
    'RDESCRIPCION',
    'RCONTENIDO',
    'ROPERACION',
    'RCOLOR',
    'RTAMANIO',
    'RNUMERO',
    'RSUMA',
    'RRESTA',
    'RMULTIPLICACION',
    'RDIVISION',
    'RINVERSO',
    'RPOTENCIA',
    'RRAIZ',
    'RSENO',
    'RCOSENO',
    'RTANGENTE',
    'RESCRIBIR',
    'LLAA',
    'LLAC',
    'IGUAL',
    'DIV',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CORA',
    'CORC',
    'RAZUL',
    'RVERDE',
    'RROJO',
    'RNEGRO',
    'RBLANCO',
    'RGRIS',
    'RCELESTE',
    'RCAFE',
)


t_RESTILO = r'Estilo'
t_RTIPO2  = r'TIPO'
t_RTEXTO2  = r'TEXTO'
t_RTIPO       = r'Tipo'
t_RTEXTO        = r'Texto'
t_RFUNCION      = r'Funcion'
t_RTITULO       = r'Titulo'
t_RDESCRIPCION  = r'Descripcion'
t_RCONTENIDO    = r'Contenido'
t_ROPERACION     = r'Operacion'
t_ROPERACIONES = r'Operaciones'
t_RCOLOR        = r'Color'
t_RTAMANIO      = r'Tamanio'
t_RSUMA       = r'SUMA'
t_RRESTA       = r'RESTA'
t_RMULTIPLICACION = r'MULTIPLICACION'
t_RDIVISION = r'DIVISION'
t_RINVERSO = r'INVERSO'
t_RPOTENCIA = r'POTENCIA'
t_RRAIZ = r'RAIZ'
t_RSENO = r'SENO'
t_RCOSENO = r'COSENO'
t_RTANGENTE = r'TANGENTE'
t_RESCRIBIR = r'ESCRIBIR'
t_RNUMERO     = r'Numero'
t_LLAA        = r'<'
t_LLAC        = r'>'
t_IGUAL       = r'='
t_DIV         = r'/'
t_CORA        = r'\['
t_CORC        = r'\]'
t_RAZUL       = r'AZUL'
t_RVERDE      = r'VERDE'
t_RROJO       = r'ROJO'
t_RNEGRO      = r'NEGRO'
t_RBLANCO = r'BLANCO'
t_RGRIS = r'GRIS'
t_RCELESTE = r'CELESTE'
t_RCAFE = r'CAFE'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'(\".*?\")'
    t.value = t.value[1:-1] #Se remueven las comillas de la entrada
    t.value = t.value.replace('\\t','\t')
    t.value = t.value.replace('\\n','\n')
    t.value = t.value.replace('\\"','\"')
    t.value = t.value.replace("\\'","\'")
    t.value = t.value.replace('\\\\','\\')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ignore = " \t"

def t_error(t):
    # print("Error Lexico, no se reconoce: '%s'" % t.value[0])
    error = Errores(t.value[0],'Error Lexico', find_column(input,t),t.lineno)
    errores_.append(error)
    t.lexer.skip(1)

import re
import ply.lex as lex
lexer = lex.lex()

def p_init(t):
    'init : instrucciones'
    t[0] = t[1]
    return t[0]

def p_instrucciones_lista(t):
    '''instrucciones    : instrucciones instruccion
                        |   instruccion'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruccion(t):
    '''instruccion  : INSTIPO
                    | INSTEXTO
                    | INSTFUNCION
                    | INSTESTILO'''
    t[0] = t[1]

def p_instruccionTipo(t):
    'INSTIPO    :   LLAA RTIPO LLAC instrucciones_2 LLAA DIV RTIPO LLAC'
    t[0] = t[4]

def p_instruccionTexto(t):
    'INSTEXTO   :   LLAA RTEXTO LLAC CADENA LLAA DIV RTEXTO LLAC'
    t[0] = Texto(t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccionFuncion(t):
    'INSTFUNCION    :   LLAA RFUNCION IGUAL RESCRIBIR LLAC instrucciones_2 LLAA DIV RFUNCION LLAC'
    t[0] = Funcion(t[6][0], t[6][1], t[6][2], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccionEstilo(t):
    'INSTESTILO     :   LLAA RESTILO LLAC instrucciones_2 LLAA DIV RESTILO LLAC'
    t[0] = t[4]

def p_instrucciones_2_lista(t):
    'instrucciones_2 : instrucciones_2 instruccion_2'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_2_instruccion(t):
    'instrucciones_2 :  instruccion_2'
    t[0] = [t[1]]

def p_instruccion_2(t):
    'instruccion_2  :  LLAA ROPERACION IGUAL tipo LLAC instrucciones_2 LLAA DIV ROPERACION LLAC'
    if len(t[6]) == 2:
        t[0] = Aritmeticas(t[6][0], t[6][1], t[4], t.lineno(1), find_column(input,t.slice[1]))
    else:
        t[0] = Aritmeticas(t[6][0], None, t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_decimal(t):
    'instruccion_2 : LLAA RNUMERO LLAC DECIMAL LLAA DIV RNUMERO LLAC '
    t[0] = Numero(float(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_entero(t):
    'instruccion_2 : LLAA RNUMERO LLAC ENTERO LLAA DIV RNUMERO LLAC '
    t[0] = Numero(int(t[4]), t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_texto(t):
    'instruccion_2 : CADENA'
    t[0] = Numero(t[4], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_titulo(t):
    'instruccion_2 : LLAA RTITULO LLAC ROPERACIONES LLAA DIV RTITULO LLAC'
    t[0] = t[4]

def p_instruccion_2_descripcion(t):
    'instruccion_2 : LLAA RDESCRIPCION LLAC CORA RTEXTO2 CORC LLAA DIV RDESCRIPCION LLAC'
    t[0] = t[5]

def p_instruccion_2_contenido(t):
    'instruccion_2 : LLAA RCONTENIDO LLAC CORA RTIPO2 CORC LLAA DIV RCONTENIDO LLAC'
    t[0] = t[5]

def p_instruccion_2_titulo_2(t):
    'instruccion_2 : LLAA RTITULO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_descripcion_2(t):
    'instruccion_2 : LLAA RDESCRIPCION RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_instruccion_2_contenido_2(t):
    'instruccion_2 : LLAA RCONTENIDO RCOLOR IGUAL COLOR RTAMANIO IGUAL ENTERO DIV LLAC'
    t[0] = Estilo(t[2], t[5], t[8], t.lineno(1), find_column(input,t.slice[1]))

def p_color(t):
    '''COLOR    : RAZUL 
                | RVERDE 
                | RROJO 
                | RNEGRO 
                | RBLANCO 
                | RGRIS 
                | RCELESTE 
                | RCAFE'''
    t[0] = t[1]

def p_tipo(t):
    '''tipo :   RSUMA
            |   RRESTA
            |   RMULTIPLICACION
            |   RDIVISION
            |   RINVERSO
            |   RRAIZ
            |   RPOTENCIA
            |   RSENO
            |   RCOSENO
            |   RTANGENTE
    '''
    if t[1] == 'SUMA':
        t[0] = Operador.SUMA
    elif t[1] == 'RESTA':
        t[0] = Operador.RESTA
    elif t[1] == 'MULTIPLICACION':
        t[0] = Operador.MULTIPLICACION
    elif t[1] == 'DIVISION':
        t[0] = Operador.DIVISION
    elif t[1] == 'INVERSO':
        t[0] = Operador.INVERSO
    elif t[1] == 'RAIZ':
        t[0] = Operador.RAIZ
    elif t[1] == 'POTENCIA':
        t[0] = Operador.POTENCIA
    elif t[1] == 'SENO':
        t[0] = Operador.SENO
    elif t[1] == 'COSENO':
        t[0] = Operador.COSENO
    elif t[1] == 'TANGENTE':
        t[0] = Operador.TANGENTE

def p_error(t):
    print("Error de sintaxis en '%s'" % t.value," Linea:", t.lineno, " Columna:",find_column(input,t))

def find_column(inp, tk):
    try:
        line_start = inp.rfind('\n',0,tk.lexpos) + 1
        return (tk.lexpos - line_start) + 1
    except:
        return 0

import ply.yacc as yacc
parser = yacc.yacc()

def parse(input):
    lexer.lineno = 1
    return parser.parse(input)

def analizador():
    from generador import Generador
    genAux = Generador()
    generador = genAux.getInstance()
    global input
    global texto
    texto = ""
    global errores_
    errores_ = []
    global titulo
    titulo =  ""
    
    input = examinar
    variable = parse(input)

    getER = True
    getEr = False 

    global operaciones
    operaciones = []
    
    if variable:
        for var in variable:
            if isinstance(var, list):
                for var_ in var:  
                    if var_.ejecutar(getER) == var_.ejecutar(getEr):
                        print(var_.ejecutar(getEr))
                    if var_.ejecutar(getER) != var_.ejecutar(getEr):
                        operacion = var_.ejecutar(getER)," = ",var_.ejecutar(getEr)
                        operaciones.append(operacion)
            elif isinstance(var, Texto):
                texto = var.ejecutar(getER) 
            elif isinstance(var, Funcion):
                print(var.ejecutar(getER))
                titulo = var.ejcutar2(getER)
    
    for operacion in operaciones:
        print(operacion[0],operacion[1],operacion[2])
    
    global filas
    filas = []
    global columnas
    columnas = []
    global lexemas
    lexemas = []
    global tipos
    tipos = []
    
    for var in errores_:
        print(var.toString())
        
        fila = var.returFila()
        filas.append(fila)
        
        columna = var.returColumna()
        columnas.append(columna)
        
        tipo = var.returTipo()
        tipos.append(tipo)
        
        lexema = var.returLexema()
        lexemas.append(lexema)
    
    operacionesReporte()
    erroresReporte()
    wb.open_new(r'E:\Documentos\USAC\LFP\LFP_202001228\Proyecto1\Operaciones.html')

def erroresReporte():
    archivo = open("Errores.html", "w")
    archivo.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Errores Encontrados</title>
    </head>''')
    archivo.write('''<body>''')
    archivo.write('''<h1>Reporte de errorres</h1>''')
    archivo.write('''<br>''')
    archivo.write('''<table border = "1">''')
    archivo.write(''' 
    <tr>
    <td>No.</td>
    <td>Lexema</td>
    <td>Tipo</td>
    <td>Columna</td>
    <td>Fila</td>
    </tr>''')
    
    contador = 1
    contador2 = 0
    for error in errores_:
        archivo.write('''<tr>''')
        archivo.write('''<td>'''+ str(contador) +'''</td>''')
        archivo.write('''<td>'''+ str(lexemas[contador2]) +'''</td>''')
        archivo.write('''<td>'''+ str(tipos[contador2]) +'''</td>''')
        archivo.write('''<td>'''+ str(columnas[contador2]) +'''</td>''')
        archivo.write('''<td>'''+ str(filas[contador2]) +'''</td>''')
        archivo.write('''</tr>''')
        contador += 1
        contador2 += 1
    archivo.write()
    archivo.write('''</body>''')
    
    archivo.close('''</table>''')

def operacionesReporte():
    archivo = open("Operaciones.html", "w")

    archivo.write('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Operaciones Realizadas</title>
    </head>''')
    archivo.write('''<body>''')
    archivo.write('''<h1>''')
    archivo.write(str(titulo))
    archivo.write('''</h1>''')
    archivo.write('''<br>''')
    archivo.write('''<table border = "1">''')
    archivo.write(''' <tr>
    <td>Operacion 1</td>
    <td>Resultado</td>
    </tr>''')
    
    for operacion in operaciones:
        archivo.write('''<tr>''')
        archivo.write( '''<td>''' + str(operacion[0])+ '''</td>''')
        archivo.write( '''<td>''' + str(operacion[2])+ '''</td>''')
        archivo.write('''<tr>''')
    archivo.write('''</table>''')
    archivo.write('''</body>''')
    archivo.close()

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
        contenido.add_command(label="Guardar",command=self.guardar)
        contenido.add_command(label="Guardar Como",command=self.guardarComo)
        contenido.add_command(label="Analizar",command=self.analisis)
        contenido.add_command(label="Errores",command=self.error)
        contenido.add_separator()
        contenido.add_command(label="Salir",command=self.salir)
        barraMenu.add_cascade(label="Archivo",menu=contenido)
        self.ventana.config(menu=barraMenu)
        
        #SEGUNDA BARRA
        contenido2  = Menu(barraMenu)
        contenido2.add_command(label="Manual de Usuario",command=self.manualUsuario)
        contenido2.add_command(label="Manual de Técnico",command=self.manualTecnico)
        contenido2.add_command(label="Temas de  Ayuda")
        
        barraMenu.add_cascade(label="Ayuda",menu=contenido2)
        self.ventana.config(menu=barraMenu)
        
        self.ingreso = Text(self.ventana, height = 40, width = 143)
        self.ingreso.place(x=25,y=25)
        
        self.ventana.mainloop()

    def abrir(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo',
                                            filetypes=[ # -> concatena -> *.data o *.lfp
                                                        ('All Files', '*')])
            # print(filename)
            with open(filename, encoding='utf-8') as infile:
                x = infile.read().strip()
                
                examinar = x
                self.ingreso.insert(1.0,x)
        except:
            messagebox.showerror("Error", "Archivo incorrecto")
            return

    def salir(self):
        self.ventana.destroy()

    def manualTecnico(self):
        wb.open_new(r'E:\Documentos\USAC\LFP\LFP_202001228\Proyecto1\MANUEALES\Manual Técnico.pdf')

    def manualUsuario(self):
        wb.open_new(r'E:\Documentos\USAC\LFP\LFP_202001228\Proyecto1\MANUEALES\Manual Usuario.pdf')

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
        filetext = str(examinar.get(1.0,END))
        file.write(filetext)
        file.close()

    def guardar(self):
        file = filedialog.asksaveasfile(filetypes=[("txt file", ".txt")],
                                        defaultextension=".txt")
        filetext = str(examinar.get(1.0,END))
        file.write(filetext)
        file.close() 

    def analisis(self):
        global examinar
        examinar = self.ingreso.get(1.0,END)
        analizador()
    
    def error(self):
        wb.open_new(r'E:\Documentos\USAC\LFP\LFP_202001228\Proyecto1\Errores.html')

a = Principal()