class Control:
    def __init__(self):
        self._tv = None
    
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
    
    def volumenDown(self):
        self._tv.volumenDown()
    
    def setCanal(self, newCanal):
        self._tv.setCanal(newCanal)
    
    def setVolumen(self, newVolumen):
        self._tv.setVolumen(newVolumen)
    
    def enlazar(self, tvHost):
        self._tv = tvHost
        tvHost.setControl(self)
    
    def getTv(self):
        return self._tv
    
    def setTv(self, newTV):
        self._tv = newTV