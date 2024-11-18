class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self.canal = 1
        self._precio = 500
        self.estado = estado
        self.volumen = 1
        self._control = None
        TV.numTV += 1

    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca


    def setCanal(self, canal):
        if self.estado == True:
            if canal >= 1 and canal <= 120:
                self.canal = canal
    def getCanal(self):
        return self.canal
    
    def canalUp(self):
        if self.estado == True:
            if self.canal < 120:
                self.canal += 1
    def canalDown(self):
        if self.estado == True:
            if self.canal > 1:
                self.canal -= 1
    
    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio
    

    def setVolumen(self, volumen):
        if self.estado == True:
            if volumen >= 0 and volumen <=7:
                self.volumen = volumen
    def getVolumen(self):
        return self.volumen
    def volumenUp(self):
        if self.estado == True:
            if self.volumen < 7:
                self.volumen += 1
    def volumenDown(self):
        if self.estado == True:
            if self.volumen > 1:
                self.volumen -= 1
        

    def setControl(self, control):
        self._control = control
    def getControl(self):
        return self._control
    
    @classmethod
    def setNumTV(cls, NumTV):
        cls.numTV = NumTV
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    

    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False
    def getEstado(self):
        return self.estado