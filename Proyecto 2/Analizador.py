global check
global radioButton
global contenedor
global areaTexto
global boton
global clave
global etiqueta
global texto

global contenido
global propiedades

areaTexto = []
radioButton = []
check = []
contenedor = []
boton = []
clave = []
etiqueta = []
texto = []
contenido = 0
propiedades = []

class Automata:

    def __init__(self):
        self.columna = 0
        self.fila = 0
        self.estado = 0

    def analizador(self):
        archivo = open("entrada.txt","r",encoding="utf-8")
        contenido = archivo.readlines()
        archivo.close()
        self.htmlEncabezado()
        self.css = open('estilo.css','w')
        
        tmp2 = ''
        tmp3 = ''
        for linea in contenido:
            lexema = ""
            self.fila += 1
            self.columna = 0
            validar = 0
            opcion = 0
            tmp = ''
            validar1 = False
            validar2 = False
            validar3 = False
            validar4 = False
            validar5 = False
            validar6 = False
            color = []
            colocacion = []
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
                                self.estado = 18
                
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
                            self.estado = 10
                            opcion = 0
                            lexema = ""
                        if lexema == 'RadioBoton':
                            self.estado = 11
                            opcion = 0
                            lexema = ""
                        if lexema == 'AreaTexto':
                            self.estado = 12
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
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        check.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 11:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        radioButton.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
                if self.estado == 12:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        areaTexto.append(lexema)
                        lexema = ""
                        opcion = 0
                        self.estado = 4
                
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
                    elif caracter == ';':
                        break
                    elif opcion == 1:
                        #print('propiedades')
                        for i in contenedor:
                            if lexema == i:
                                self.estado = 19
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in boton:
                            if lexema == i:
                                self.estado = 20
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in clave:
                            if lexema == i:
                                self.estado = 21
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in texto:
                            if lexema == i:
                                self.estado = 22
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in etiqueta:
                            if lexema == i:
                                self.estado = 23
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in check:
                            if lexema == i:
                                self.estado = 24
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in radioButton:
                            if lexema == i:
                                self.estado = 25
                                opcion = 0
                                lexema = ""
                                tmp = i
                        
                        for i in areaTexto:
                            if lexema == i:
                                self.estado = 26
                                opcion = 0
                                lexema = ""
                                tmp = i

                        if lexema == 'propiedades':
                            self.estado = 27
                        
                        if lexema == 'Colocacion':
                            self.estado = 29

                        if lexema == 'this':
                            self.estado = 18
                            break
                
                #contenedor -> add por agregar :b
                if self.estado == 19:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema  == 'setAncho':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
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

                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                        
                #boton  -> solo falta el add
                if self.estado == 20:
                    if caracter.isalpha() or caracter.isnumeric() or caracter == " ":
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema  == 'setAncho':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
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
                        
                        if lexema == 'setTexto':
                            validar4 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar4 == True:
                            if lexema != '':
                                self.tmp = self.setTextoBotton(tmp,lexema)
                                lexema = ''
                                self.estado = 18

                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                
                #clave -> solo falta el add
                if self.estado == 21:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif caracter == '"':
                        contador = len(linea)
                        if linea[contador-4]== '"' and linea[contador-5]== '"' :
                            self.estado = 18
                            break
                    elif opcion == 1:
                        
                        if lexema == 'setTexto':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
                            if lexema != '':
                                tmp2 = lexema
                                lexema = ''
                                self.estado = 18

                        if lexema == 'setAlineacion':
                            validar2 = True
                            lexema = ''
                            opcion = 0
                            
                        if validar2 == True:
                            if lexema != '':
                                self.setAlineacionContraseña(tmp,tmp2,lexema)
                                tmp2 = ''
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                        
                #texto -> solo falta el add
                if self.estado == 22:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        
                        if lexema == 'setTexto':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
                            if lexema != '':
                                tmp2 = lexema
                                lexema = ''
                                self.estado = 18

                        if lexema == 'setAlineacion':
                            validar2 = True
                            lexema = ''
                            opcion = 0
                            
                        if validar2 == True:
                            if lexema != '':
                                self.setAlineacionTexto(tmp,tmp2,lexema)
                                tmp2 = ''
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                
                #etiqueta -> solo falta el add
                if self.estado == 23:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema  == 'setAncho':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
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
                        
                        if lexema == 'setTexto':
                            validar3 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar3 == True:
                            if lexema != '':
                                self.tmp = self.setTexto(tmp,lexema)
                                lexema = ''
                                self.estado = 18

                        if lexema == 'setColorLetra':
                            validar4 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar4 == True:
                            if lexema != '':
                                color.append(lexema)
                                lexema = ''
                                if len(color) == 3:
                                    self.setColorLetra(tmp,color)
                                    lexema = ''
                                    self.estado = 18
                        
                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                        
                #check -> solo falta el add
                if self.estado == 24:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        
                        if lexema == 'setMarcada':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
                            if lexema != '':
                                tmp2 = lexema
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setTexto':
                            validar2 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar2 == True:
                            if lexema != '':
                                self.tmp = self.setMarcada(tmp,tmp2,lexema)
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break
                        
                #radioButton -> solo falta el add 
                if self.estado == 25:
                    if caracter.isalpha() or caracter.isnumeric():
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        
                        if lexema  == 'setMarcada':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                            
                        if validar1 == True:
                            if lexema != '':
                                tmp2 = lexema
                                lexema = ''
                                self.estado = 18
                                
                        if lexema == 'setGrupo':
                            validar2 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar2 == True:
                            if lexema != '':
                                tmp3 = lexema
                                lexema = ''
                                self.estado = 18
                        
                        if lexema == 'setTexto':
                            validar3 = True
                            lexema = ''
                            opcion = 0
                            
                        if validar3 == True:
                            if lexema != '':
                                self.radioButton(tmp,tmp3,tmp2,lexema)
                                lexema = ''
                                self.estado = 18
                                tmp2 = ''
                                tmp3 = ''

                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''
                
                #areaTexto -> solo falta el add
                if self.estado == 26:
                    if caracter.isalpha() or caracter.isnumeric() or caracter == ' ':
                        lexema += caracter
                        opcion = 1
                    elif opcion == 1:
                        if lexema == 'setTexto':
                            validar1 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar1 == True:
                            if lexema != '':
                                self.tmp = self.setTextoArea(tmp,lexema)
                                lexema = ''
                                self.estado = 18
                                
                        if lexema == 'setPosicion':
                            validar6 = True
                            lexema = ''
                            opcion = 0
                        
                        if validar6 == True:
                            if lexema != '':
                                colocacion.append(lexema)
                                if len(colocacion) == 2:
                                    self.setposicion(tmp,colocacion)
                                    lexema = ''
                                    self.estado = 18
                                lexema = ''

                        if lexema == 'add':
                            self.estado = 18
                            break

                if self.estado == 27:
                    if caracter == "-":
                        self.estado = 27
                        validar += 1
                        if validar == 2:
                            self.estado = 28
                
                if self.estado == 28:
                    if caracter == ">":
                        self.estado = 1

                if self.estado == 29:
                    if caracter == "-":
                        self.estado = 29
                        validar += 1
                        if validar == 2:
                            self.estado = 30
                
                if self.estado == 30:
                    if caracter == ">":
                        continue
                        #self.cerrarhtml()


    def setposicion(self,id,xy):
        self.css.write(id+"{\n")
        self.css.write("position: absolute;\n")
        self.css.write("left:"+xy[0]+"px; \ntop:"+ xy[1]+"px; \n")
        self.css.write("}\n")

    def textoBotton(self,id,texto):
        redactar = '''<input type="submit" id="'''+id+'''" value="'''+texto+'''" style="text-align: Alineacion"/> '''
        print(redactar)
        self.html.write(redactar+"\n")

    def radioButton(self,id,nombre,estado,texto):
        redactar = '''<input type="radio" id="''' + id + '''" name="''' + nombre + '''" checked="'''+estado+'''" value="email">
        <label for="''' + id + '''">''' + texto + '''</label> '''
        print(redactar)
        self.html.write(redactar+"\n")

    def setMarcada(self,id, valor,texto):
        redactar  = '''<label><input type="checkbox" id="'''+id+'''" value="second_checkbox" checked="'''+valor+'''" >'''+texto+'''</label> \n'''
        print(redactar)
        self.html.write(redactar+"\n")

    def setTextoArea(self,id, texto):
        redactar = ''' <TExtarea id="''' + id + '''">''' + texto + '''</TExtarea> '''
        print(redactar)
        self.html.write(redactar+"\n")

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

    def setTexto(self,control,texto):
        redactar = '''<label id="''' + control + '''">''' + texto + '''</label>'''
        print(redactar)
        self.html.write(redactar+"\n")

    def setTextoBotton(self,id,texto):
        redactar = '''<input type="button" id="'''+id+'''" value="'''+texto+'''">'''
        print(redactar)
        self.html.write(redactar+"\n")

    def setColorLetra(self,control,color):
        self.css.write(control + '{\n')
        self.css.write('color: rgb(' )
        for i in color:
            self.css.write(i + ',')
        self.css.write(');\n')
        self.css.write('}\n')

    def add(self, div, contenido):
        self.html.write(
            '''<div id="''' + div + '''">\n'''
            '\t' +  contenido + '\n')
        self.tmp = ''

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
        self.html = open('index.html','w')
        self.html.write(
'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resultado</title>
    <link rel="stylesheet" href="/estilo.css">
</head>
<body>
''')

    def setAlineacionContraseña(self,control, texto, alineacion):
        redactar = '''<input type = "password" id="''' + control + '''"  value="''' + texto +'''" style="text-align: '''+ alineacion +'''" />'''
        print(redactar)
        self.html.write(redactar+"\n")

    def setAlineacionTexto(self,id,texto,alineacion):
        redactar = '''<input type = "text" id="''' + id + '''"  value="''' + texto +'''" style="text-align: '''+ alineacion +'''" />'''
        print(redactar)
        self.html.write(redactar+"\n")

    def cerrarhtml(self):
        self.html.write(
'''
</body>
</html>
''')
        self.html.close()

#a = Automata()
#a.analizador()