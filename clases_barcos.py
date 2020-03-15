
class barcos():
    """
    para darle direccion y posicion a los barcos
    """
    def __init__(self,direccion,lugar):
        self.direccion = direccion
        self.lugar = lugar

class submarino(barcos):
    """
    para darle la cantidad y tamano
    """
    cant = 4
    tamano = 1
    caract = "los submarinos se pueden sumergir"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract

class buque_grande(barcos):
    """
    para darle la cantidad y tamano
    """
    cant = 1
    tamano = 3
    caract = "El buque pequeno se puede comunicar con tierra y otros miembros de la flota"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract

class buquesito(barcos):
    """
    para darle la cantidad y tamano
    """
    cant = 1
    tamano = 2
    caract = "El buque grande permite el aterrizaje de helicopteros para el transporte de tropas"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract



