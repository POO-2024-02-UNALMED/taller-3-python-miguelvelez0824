class TV:
    numTV = 0
    def __init__(self, marca, estado):
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._control = None
        self._marca = marca
        self._estado = estado
        TV.numTV = TV.numTV + 1
    
    def getMarca(self):
        return self._marca
    
    def setMarca(self, newMarca):
        self._marca = newMarca
    
    def getCanal(self):
        return self._canal
    
    def setCanal(self, newCanal):
        if newCanal >= 1 and newCanal <= 120 and self._estado == True:
            self._canal = newCanal
    
    def getPrecio(self):
        return self._precio 
    
    def setPrecio(self, newPrecio):
        self._precio = newPrecio 
    
    def getVolumen(self):
        return self._volumen 
    
    def setVolumen(self, newVolumen):
        if newVolumen >= 0 and newVolumen <= 7 and self._estado == True:
            self._volumen = newVolumen 
    
    def getControl(self):
        return self._control
    
    def setControl(self, newControl):
        self._control = newControl 
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    @classmethod
    def setNumTV(cls, newNumTV):
        cls.numTV = newNumTV 
    
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False 
    
    def getEstado(self):
        return self._estado 
    
    def canalUp(self):
        if self._canal < 120 and self._estado == True:
            self._canal = self._canal + 1
    
    def canalDown(self):
        if self._canal > 1 and self._estado == True:
            self._canal = self._canal - 1
    
    def volumenUp(self):
        if self._volumen < 7 and self._estado == True:
            self._volumen = self._volumen + 1
    
    def volumenDown(self):
        if self._estado == True and self._volumen > 0:
            self._volumen = self._volumen - 1