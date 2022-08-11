# EJEMPLO DE FUNCIONES Y CLASES

# FUNCION
# CLASES
# CLASES
class Alumno:
    grado = 1

    def __init__(self, clave, nombre, apellido, edad, correo):
        self.clave = clave
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
    
    def getClave(self):
        return self.clave
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido
    
    def getEdad(self):
        return self.edad

    def getCorreo(self):
        return self.correo
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

    def setEdad(self, edad):
        self.edad = edad
    
    def setCorreo(self, correo):
        self.correo = correo
    

class Analizador:

    def Lectura(ruta):
        objeto = open(ruta,'r+')
        lineas = objeto.readlines()
        objeto.close()
        alumnos = []
        for linea in lineas:
            data = linea.split(',') # Devuelve una lista
            alumno = Alumno(data[0], data[1], data[2], data[3], data[4].rstrip('\n'))
            alumnos.append(alumno)
        return alumnos

alumnos = Analizador.Lectura('carpeta/clase3.txt')
if alumnos!= []:
    a2 = Analizador.Lectura('carpeta/clase3.txt')
    for a in a2:
        alumnos.append(a)

for alumno in alumnos:
    print(alumno.getNombre(),' ', alumno.getApellido(), ' ', alumno.getCorreo())