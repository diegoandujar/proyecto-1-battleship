from random import randint

class barcos():
    def __init__(self,direccion,lugar):
        self.direccion = direccion
        self.lugar = lugar

class submarino(barcos):
    cant = 4
    tamano = 1
    caract = "los submarinos se pueden sumergir"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract

class buque_grande(barcos):
    cant = 1
    tamano = 3
    caract = "El buque pequeno se puede comunicar con tierra y otros miembros de la flota"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract

class buquesito(barcos):
    cant = 1
    tamano = 2
    caract = "El buque grande permite el aterrizaje de helicopteros para el transporte de tropas"
    def __init__(self,direccion,lugar):
        barcos.__init__(self,direccion,lugar)
    def cant_tam(self):
        return self.cant, self.tamano, self.caract


tablero = []
lista_final = []
direccion = ("Vertical" , "Horizontal")
lista_al_lado = []

for x in range(10):
    tablero.append(["■"] * 10)

def tableros(tablero):
    print("0 1 2 3 4 5 6 7 8 9")
    for r in tablero:
        
        print((" ").join(r))

def tiros():
    global tiritos, puntos, tiros_repetidos, lista_final
    turn = 0
    puntos = 0 
    tiritos = 0
    tiros_repetidos = 0
    zona_de_tiros = []
    # for x in lista_final:
    #     tablero[x[0]][x[1]]= "B"
    while len(lista_final)>0:
        turn = turn + 1 
        while True:
            try:
                row = int(input("Guess Row:"))
                if row>9 and row<0:
                    raise ValueError
                break
            except ValueError:
                print("---eso no es un numero---")
        while True:
            try:
                col = int(input("Guess Col:"))
                if col>9 and col<0:
                    raise ValueError 
                break
            except ValueError:
                print("---eso no es un numero")
        coordenadas = (row,col)
        while row>9 or row<0 or col>9 or col<0:
            print("---eso no se encuentra en el campo")
            while True:
                try:
                    row = int(input("Guess Row:"))
                    if row>9 and row<0:
                        raise ValueError
                    break
                except ValueError:
                    print("---eso no es un numero---")
            while True:
                try:
                    col = int(input("Guess col:"))
                    if row>9 and row<0:
                        raise ValueError
                    break
                except ValueError:
                    print("---eso no es un numero---")
            coordenadas = (row,col)
        
        while  coordenadas in zona_de_tiros:
            print("---no puedes repetir la zona de impacto---")
            while True:
                try:
                    row = int(input("Guess Row:"))
                    if row>9 and row<0:
                        raise ValueError
                    break
                except ValueError:
                    print("---eso no es un numero---")   
            while True: 
                try:
                    col = int(input("Guess Col:"))    
                    if col>9 and col<0:
                        raise ValueError
                    break
                except ValueError:
                    print("---eso no es un numero---")    
            tiros_repetidos = tiros_repetidos + 1
            coordenadas = (row,col)
        if tablero[row][col] == "X":
            puntos = puntos - 2

        elif coordenadas in lista_final:
            print("---Le has dado a un barco---")        
            lista_final.remove(coordenadas)
            tiritos = tiritos + 1
            tablero[row][col] = "F"
            puntos = puntos + 10 
        elif coordenadas not in lista_final:
            print("\nMission failed, we'll get it next time")
            tablero[row][col] = "X"
            tiritos = tiritos + 1
            puntos = puntos - 2 
        tableros(tablero)
        zona_de_tiros.append(coordenadas)
        print(turn)
    if tiritos==9:
        print("---Marico eres arrechisimo---\n")  
    elif tiritos>9 and tiritos<45:
        print("---coye, bien bro---\n")
    elif tiritos>44 and tiritos<70:
        print("---Mira bro, hay que mejorar---\n")
    elif tiritos>70:
        print("---papi, eres una mierda---\n")
          
    print("tiros efectuados: ",tiritos)
    print("tiros repetidos: ",tiros_repetidos)
    print("\n")
    print("se disparo en estos puntos",zona_de_tiros) 
    print("los puntos obtenidos: ",puntos)
    for x in zona_de_tiros:
        tablero[x[0]][x[1]]= "■"


def colocar_buquesito():
    global lista_buquesito
    lista_buquesito = []   
    tamano = buquesito.tamano
    cant = buquesito.cant 
    orientaciones = ("Vertical", "Horizontal")
    orientacion = orientaciones[(randint(0,1))]
    while cant >0:
        if orientacion=="Horizontal":
            coorde_fila = randint(0,10)
            coorde_col = randint(0,10)
        elif orientacion=="Vertical":
            coorde_col = randint(0,10)
            coorde_fila = randint(0,10)
        while (coorde_fila + tamano)>10 or (coorde_col + tamano)>10:
            coorde_col = randint(0,10)
            coorde_fila = randint(0,10)
        lugar = (coorde_fila,coorde_col)
        lista_buquesito.append(lugar)
        while len(lista_buquesito)<tamano:
            if orientacion=="Vertical":
                coorde_fila = coorde_fila + 1
                lugar = (coorde_fila,coorde_col)
            elif orientacion=="Horizontal":
                coorde_col = coorde_col + 1 
                lugar = (coorde_fila,coorde_col)
            lista_buquesito.append(lugar)
        cant = cant -1 
    # print(lista_buquesito)
    for x in lista_buquesito:
        lista_final.append(x)

def colocar_buque_grande():
    global lista_buquegrande
    for x in lista_final:
        pos_al_lado = (x[0]+1,x[1])
        pos_al_lado2 = (x[0]-1,x[1])
        pos_al_lado3 = (x[0],x[1]-1)
        pos_al_lado4 = (x[0],x[1]+1)
        lista_al_lado.append(pos_al_lado4)
        lista_al_lado.append(pos_al_lado3)
        lista_al_lado.append(pos_al_lado2)
        lista_al_lado.append(pos_al_lado)
    lista_buquegrande = []
    tamano = buque_grande.tamano
    cant = buque_grande.cant 
    orientaciones = ("Vertical", "Horizontal")
    orientacion = orientaciones[(randint(0,1))]
    seguir = True
    while seguir:
        while cant >0:
            if orientacion=="Horizontal":
                coorde_fila = randint(0,10)
                coorde_col = randint(0,10)
            elif orientacion=="Vertical":
                coorde_col = randint(0,10)
                coorde_fila = randint(0,10)
            while (coorde_fila + tamano)>10 or (coorde_col + tamano)>10:
                coorde_col = randint(0,10)
                coorde_fila = randint(0,10)
            lugar = (coorde_fila,coorde_col)
            lista_buquegrande.append(lugar)
            while len(lista_buquegrande)<tamano:
                if orientacion=="Vertical":
                    coorde_fila = coorde_fila + 1
                    lugar = (coorde_fila,coorde_col)
                elif orientacion=="Horizontal":
                    coorde_col = coorde_col + 1 
                    lugar = (coorde_fila,coorde_col)
                lista_buquegrande.append(lugar) 
            cant = cant-1 
        if lista_buquegrande[0] in lista_final or lista_buquegrande[1] in lista_final or lista_buquegrande[2] in lista_final:
            seguir = True
        elif lista_buquegrande[0] in lista_al_lado or lista_buquegrande[1] in lista_al_lado or lista_buquegrande[2] in lista_al_lado:
            seguir = True
        elif lista_buquegrande[0] not in lista_al_lado and lista_buquegrande[1] not in lista_al_lado and lista_buquegrande[2] not in lista_al_lado and lista_buquegrande[0] not in lista_final and lista_buquegrande[1] not in lista_final and lista_buquegrande[2] not in lista_final:
            seguir = False           
    # print(lista_buquegrande)
    for x in lista_buquegrande:
        lista_final.append(x)

def colocar_submarinos():
    global  lista_submarinos
    for x in lista_final:
        pos_al_lado = (x[0]+1,x[1])
        pos_al_lado2 = (x[0]-1,x[1])
        pos_al_lado3 = (x[0],x[1]-1)
        pos_al_lado4 = (x[0],x[1]+1)
        lista_al_lado.append(pos_al_lado4)
        lista_al_lado.append(pos_al_lado3)
        lista_al_lado.append(pos_al_lado2)
        lista_al_lado.append(pos_al_lado)
    lista_submarinos = []
    tamano = submarino.tamano
    cant = submarino.cant 
    orientaciones = ("Vertical", "Horizontal")
    orientacion = orientaciones[(randint(0,1))]
    seguir = True
    while seguir:
        while cant >0:
            if orientacion=="Horizontal":
                coorde_fila = randint(0,10)
                coorde_col = randint(0,10)
            elif orientacion=="Vertical":
                coorde_col = randint(0,10)
                coorde_fila = randint(0,10)
            while (coorde_fila + tamano)>10 or (coorde_col + tamano)>10:
                coorde_col = randint(0,10)
                coorde_fila = randint(0,10)
            lugar = (coorde_fila,coorde_col)
            lista_submarinos.append(lugar)
            while len(lista_submarinos)<tamano:
                if orientacion=="Vertical":
                    coorde_fila = coorde_fila + 1
                    lugar = (coorde_fila,coorde_col)
                elif orientacion=="Horizontal":
                    coorde_col = coorde_col + 1 
                    lugar = (coorde_fila,coorde_col)
                lista_submarinos.append(lugar) 
            cant = cant-1 
        for x in lista_submarinos:
            pos_al_lado = (x[0]+1,x[1])
            pos_al_lado2 = (x[0]-1,x[1])
            pos_al_lado3 = (x[0],x[1]-1)
            pos_al_lado4 = (x[0],x[1]+1)
            lista_al_lado.append(pos_al_lado4)
            lista_al_lado.append(pos_al_lado3)
            lista_al_lado.append(pos_al_lado2)
            lista_al_lado.append(pos_al_lado)                 
        if lista_submarinos[0] in lista_final or lista_submarinos[1] in lista_final or lista_submarinos[2] in lista_final or lista_submarinos[3] in lista_final:
            seguir = True
        elif lista_submarinos[0]==lista_submarinos[1] or lista_submarinos[0]==lista_submarinos[2] or lista_submarinos[0]==lista_submarinos[3] or lista_submarinos[1]==lista_submarinos[2] or lista_submarinos[1]==lista_submarinos[3] or lista_submarinos[2]==lista_submarinos[3]:
            seguir = True
        elif lista_submarinos[0] in lista_al_lado or lista_submarinos[1] in lista_al_lado or lista_submarinos[2] in lista_al_lado or lista_submarinos[3] in lista_al_lado:
            seguir = True
        elif lista_submarinos[0] not in lista_al_lado and lista_submarinos[1] not in lista_al_lado and lista_submarinos[2] not in lista_al_lado and lista_submarinos[3] not in lista_al_lado and lista_submarinos[0] not in lista_final and lista_submarinos[1] not in lista_final and lista_submarinos[2] not in lista_final and lista_submarinos[3] not in lista_final:
            seguir = False               
    # print(lista_submarinos)
    for x in lista_submarinos:
        lista_final.append(x)

    
def ubicar_todo():
    colocar_buquesito()
    colocar_buque_grande()
    colocar_submarinos()

def juego():  
    tableros(tablero)
    ubicar_todo()
    print(lista_final)
    tiros()

