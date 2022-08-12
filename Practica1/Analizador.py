from Cursos import Cursos
from tkinter import messagebox

class Analizador():
    global cursos
    cursos = []
    
    print("esta en el modulo analizador")
    def AgregarCurso(codigo,nombre,requisito,semestre,opcional,creditos,estado):
        
        curso = Cursos(codigo,nombre,requisito,semestre,opcional,creditos,estado)
        cursos.append(curso)
        messagebox.showinfo("Informacion", "Archivo Cargado con Exito")
        self.ruta.delete("1.0","end")
        
        return cursos