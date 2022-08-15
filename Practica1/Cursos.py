class Cursos():
    
    def __init__(self,codigo,nombre,requisitos,semestre,opcional,creditos,estado):
        self.codigo = codigo
        self.nombre = nombre
        self.requisitos = requisitos
        self.semestre = semestre
        self.opcional = opcional
        self.creditos = creditos
        self.estado = estado
        
    
    #get de la clase
    def getCodigo(self):
        return self.codigo
    
    def getNombre(self):
        return self.nombre
    
    def getRequisitos(self):
        return self.requisitos
    
    def getSemestre(self):
        return self.semestre
    
    def getOpcional(self):
        return self.opcional
    
    def getCreditos(self):
        return self.creditos
    
    def getEstado(self):
        return self.estado[0]
    
    #set de la clase
    def setCodigo(self,codigo):
        self.codigo = codigo
    
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def setRequisitos(self,requisitos):
        self.requisitos = requisitos

    def setSemestre(self,semestre):
        self.semestre = semestre
        
    def setOpcional(self,opcional):
        self.opcional = opcional
        
    def setCreditos(self,creditos):
        self.creditos = creditos
    
    def setEstado(self,estado):
        self.estado = estado