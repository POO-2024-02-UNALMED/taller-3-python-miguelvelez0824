class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setcontrol(self)

    def setTv(self, tv):
        self._tv = tv
    def getTv(self):
        return self._tv
    
    
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()


    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    

    def volumenUp(self):
        self._tv.volumenUp()
    def voluemnDown(self):
        self._tv.voluemnDown()
    
    
    def setCanal(self, canal):
        self._tv.setCanal(canal)
    def setVolumen(self, volumen):
        self._tv.setVolumen(volumen)