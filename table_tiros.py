from random import randint
from clases_barcos import submarino
from clases_barcos import buquesito
from clases_barcos import buque_grande



tablero = []
direccion = ("Vertical" , "Horizontal")


for x in range(10):
    tablero.append(["■"] * 10)

def tableros(tablero):
    for r in tablero:
        print((" ").join(r))

# print("Let's play Battleship!")
tableros(tablero)
def tiros():
    seguir = True
    turn = 0
    tiritos = 0
    tiros_repetidos = 0
    zona_de_tiros = []
    while seguir:
        turn = turn + 1 
        row = int(input("Guess Row:")) - 1
        col = int(input("Guess Col:")) - 1
        coordenadas = (row,col)
        zona_de_tiros.append(coordenadas)
        
        while row>10 or row<0 or col>10 or col<0:
            print("\n---la sacasta del campo campeon---")
            row = int(input("Guess Row:")) - 1
            col = int(input("Guess Col:")) - 1
            tablero[row][col] = "X"
            coordenadas = (row,col)
            tiritos = tiritos + 1
        if tablero[row][col] == "X":
            while  coordenadas in zona_de_tiros:
                print("---la vas a volver a cagar papa---")
                row = int(input("Guess Row:")) - 1
                col = int(input("Guess Col:")) - 1
                tablero[row][col] = "X"             
                tiros_repetidos = tiros_repetidos + 1
                coordenadas = (row,col)
                
            tiritos = tiritos + 1
            zona_de_tiros.append(coordenadas)
        else:
            print("\nMission failed, we'll get it next time")
            tablero[row][col] = "X"
            tiritos = tiritos + 1
        tableros(tablero)
        print(turn)
        
        de_nuevo = int(input("si o no: "))
        if de_nuevo!=1:
            break
    print("tiros efectuados: ",tiritos)
    print(tiros_repetidos)
    print(zona_de_tiros)    
print("\n")


lista_final = []
def colocar_buquesito():
    global lista_lista
    lista_buquesito = []
    lista_lista = []
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
        for x in lista_buquesito:
            lista_final.append(x)
            lista_lista.append(x)
    
    print(lista_final)
    lista_buquesito.clear()
    print(lista_buquesito)
    print("epale")

          


def colocar_buque_grande():
    lista_buquegrande = []
    tamano = buque_grande.tamano
    cant = buque_grande.cant 
    orientaciones = ("Vertical", "Horizontal")
    orientacion = orientaciones[(randint(0,1))]
    while cant >0:
        posible_lugar = True
        while posible_lugar:
            aqui = "si"
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
            for x in lista_final:
                for y in lista_buquegrande:
                    if y==x:
                        aqui = "no"
                    elif y!=x:
                        aqui = "si"
            if aqui=="si":
                posible_lugar = False
            elif aqui=="no":
                posible_lugar = True
                    
        cant = cant - 1 
    print(lista_buquegrande)

    
    

def colocar_submarinos():
    lista_submarinos = []
    tamano = submarino.tamano
    cant = submarino.cant 
    orientaciones = ("Vertical", "Horizontal")
    orientacion = orientaciones[(randint(0,1))]
    while cant >0:
        posible_lugar = True
        while posible_lugar:
            aqui = "si"
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
            for x in lista_final:    
                for y in lista_submarinos:
                    if y == x:
                        aqui = "si"
                    elif y != x:
                        aqui = "no"
            if aqui=="no":
                posible_lugar = True 
            elif aqui=="si":
                posible_lugar = False
                    
        # for x in lista_submarinos:
        #     lista_final.append(x)
        cant = cant - 1 
    print(lista_submarinos)
    

def ubicar_todo():
    colocar_buquesito()
    colocar_buque_grande()
   
    
   
ubicar_todo()    