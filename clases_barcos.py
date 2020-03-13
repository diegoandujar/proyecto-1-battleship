
class submarino():
    cant = 4
    tamano = 1
    def __init__(self,direccion,lugar):
        self.lugar = lugar
        self.direccion = direccion
    def cant_tam(self):
        return self.cant, self.tamano

class buque_grande():
    cant = 1
    tamano = 3
    def __init__(self,direccion,lugar):
        self.lugar = lugar
        self.direccion = direccion
    def cant_tam(self):
        return self.cant, self.tamano

class buquesito():
    cant = 1
    tamano = 2
    def __init__(self,direccion,lugar):
        self.lugar = lugar
        self.direccion = direccion
    def cant_tam(self):
        return self.cant, self.tamano

