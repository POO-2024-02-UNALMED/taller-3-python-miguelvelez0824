class Marca:
    def __init__(self, name):
        self._nombre = name
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    