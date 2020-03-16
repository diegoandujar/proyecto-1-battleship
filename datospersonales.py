
from random import randint

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

tablero = []
lista_final = []
direccion = ("Vertical" , "Horizontal")
lista_al_lado = []

for x in range(10):
    tablero.append(["■"] * 10)

def tableros(tablero):
    """
    para crear el tablero
    """
    print("0 1 2 3 4 5 6 7 8 9")
    for r in tablero:
        
        print((" ").join(r))

def tiros():
    """
    Para pedir las cordenadas de los disparos en el tablero y colocar los barcos
    """
    global tiritos, puntos, tiros_repetidos, lista_final
    turn = 0
    puntos = 0 
    tiritos = 0
    tiros_repetidos = 0
    zona_de_tiros = []
    for x in lista_final:
        tablero[x[0]][x[1]]= "B"
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
        print("---¿Eres un Robot? lo que acabas de hacer es poco probable ....---\n")  
    elif tiritos>9 and tiritos<45:
        print("---Excelente Estrategia---\n")
    elif tiritos>44 and tiritos<70:
        print("---Buena Estrategia; pero hay que mejorar---\n")
    elif tiritos>70:
        print("---Considérese Perdedor, tiene que mejorar notablemente---\n")
          
    print("tiros efectuados: ",tiritos)
    print("tiros repetidos: ",tiros_repetidos)
    print("\n")
    print("se disparo en estos puntos",zona_de_tiros) 
    print("los puntos obtenidos: ",puntos)
    for x in zona_de_tiros:
        tablero[x[0]][x[1]] = "■"

def colocar_buquesito():
    """
    para colocar las coordenadas del buque pequeno en la lista de barcos
    """
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
    """
    para colocar las coordenadas del buque en la lista de barcos
    """
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
    """
    para colocar las coordenadas de los submarinos en la lista de barcos
    """
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
    """
    para ubicar los barcos en la lista de coordenadas
    """
    colocar_buquesito()
    colocar_buque_grande()
    colocar_submarinos()

def juego():
    """
    fun para correr el tablero, la ubicacion, y la fun para disparar
    """  
    tableros(tablero)
    ubicar_todo()
    #print(lista_final)
    tiros()


#########################################################

lista_de_jugadores = []
def datos_jugador():
    """
    para pedir los datos del jugador
    """
    global edad, dicc_datps_per, genero,datosssss, usuario_en_uso, usuarios, user

    usuarios = []
    datosssss = []
    usuario_en_uso =[]
    seguir = True
    user = input("Nombre de usuario: ")
    while seguir:
        with open ('database.txt','r') as fh:
            datos = fh.readlines()
            for x in datos:
                usuario = x[:-1].split(',')
                usuarios.append(usuario[0])
                datosssss.append(usuario)
            if user in usuarios:
                print("bienvenido de vuelta {}".format(x[0]))
                for x in datosssss:
                    if user == x[0]:
                        user = x[0]
                        nombre_completo = x[1]
                        edad = x[2]
                        genero = x[3]
                        datosssss.remove(x)
                        for y in x:
                            usuario_en_uso.append(y)
                print('{}, {}, {}, {}'.format(user,nombre_completo,edad,genero))

            else:
                while  len(user)>30 or " " in user:
                    if len(user)>30:
                        print("---No pueden ser mas de 30 caracteres---")
                        user = input("Ingrese su usuario nuevamente: ")
                    if " " in user:
                        print("---No se pueden espacios---")
                        user = input("Ingrese su usuario nuevamente: ") 
                # print(user)
                user = user.lower()
            
                nombre = input("\nNombre: ")
                vali_nombre = nombre.isalpha()
                while vali_nombre == False:
                    print("---Solo se pueden colocar letras---")
                    nombre = input("Nombre: ")
                    vali_nombre =  nombre.isalpha()
                nombre = nombre.title()
                apellido = input("Apellido: ")
                vali_apellido = apellido.isalpha()
                while vali_apellido == False: 
                    print("---Solo se pueden colocar letras---")
                    apellido = input("Apellido: ")
                    vali_apellido = apellido.isalpha()
                apellido = apellido.title()

                nombre_completo = nombre +" "+ apellido
                
                edad = input("\nColoque su edad: ")
                vali_edad = edad.isdigi()
                while vali_edad==False or int(edad)<5 or int(edad)>100:
                    print("---Solo pueden ser numeros enteros entre 5 y 100---") 
                    edad = input("Repita su edad: ")
                    vali_edad = edad.isdigit()
                edad = int(edad)
                genero = input("\nHombre --- M\nMujer --- F\n ")
                vali_genero = genero.isalpha()
                while vali_genero==False or genero!="F" and genero!="f" and genero!="M" and genero!="m":
                    print("---Solo pueden ser las letras M o F---")
                    genero = input("Hombre --- M\nMujer --- F ")
                    vali_genero = genero.isalpha()
                if genero=="M" or genero=="m":
                    genero = "Hombre"
                if genero=="F" or genero=="f":
                    genero = "Mujer"
                usuario_en_uso.append(user)
                usuario_en_uso.append(nombre_completo)
                usuario_en_uso.append(edad)
                usuario_en_uso.append(genero)
        break

def modificar():
    """
    para modificar los datos
    """
    user_buscar = input("ingrese el usuario que quiere modificar: ")       
    seguir = True
    no_modificar = []
    a_modificar = []
    usuarios2 = []
    while seguir:
        with open ('database.txt','r') as fh:
            datos = fh.readlines()
            for x in datos:
                usuario1 = x[:-1].split(',')
                usuarios2.append(usuario1[0])
                no_modificar.append(usuario1)
            if user_buscar in usuarios2:
                for x in no_modificar:
                    if user_buscar == x[0]:
                        for y in x:
                            a_modificar.append(y)
                        no_modificar.remove(x)
                seguir2 = True
                while seguir2:
                    que_desea = input("Que desea modificar:\nUser --->(1)\nNombre Comlpeto --->(2)\nEdad --->(3)\nGenero --->(else)\n---> ")
                    vali_que_desea = que_desea.isdigit()
                    while vali_que_desea == False:
                        print("---Solo pueden ser numeros---")
                        que_desea = input("Que desea modificar:\nUser --->(1)\nNombre Completo --->(2)\nEdad --->(3)\nGenero --->(else)\n---> ")
                        vali_que_desea = que_desea.isdigit()
                    if que_desea=='2':
                        nombre = input("Nombre: ")
                        vali_nombre = nombre.isalpha()
                        while vali_nombre == False:
                            print("---Solo se pueden colocar letras---")
                            nombre = input("Nombre: ")
                            vali_nombre =  nombre.isalpha()
                        nombre = nombre.title()
                        apellido = input("Apellido: ")
                        vali_apellido = apellido.isalpha()
                        while vali_apellido == False: 
                            print("---Solo se pueden colocar letras---")
                            apellido = input("Apellido: ")
                            vali_apellido = apellido.isalpha()
                        apellido = apellido.title()

                        nombre_completo = nombre +" "+ apellido
                        a_modificar[1] = nombre_completo
                    if que_desea=='1':
                        user = input("Nombre de usuario: ")
                        while  len(user)>10 or " " in user:
                            if len(user)>10:
                                print("---No pueden ser mas de 30 caracteres---")
                                user = input("Ingrese su usuario nuevamente: ")
                            if " " in user:
                                print("---No se pueden espacios---")
                                user = input("Ingrese su usuario nuevamente: ") 
                        a_modificar[0] = user
                    if que_desea=='3':
                        edad = input("Coloque su edad: ")
                        vali_edad = edad.isdigit()
                        while vali_edad==False or int(edad)<5 or int(edad)>100:
                            print("---Solo pueden ser numeros enteros entre 5 y 100---") 
                            edad = input("Repita su edad: ")
                            vali_edad = edad.isdigit()
                        a_modificar[2] = str(edad)
                        edad = int(edad)
                    if que_desea!='1' and que_desea!='2' and que_desea!='3':
                        genero = input("Hombre --- M\nMujer --- F\n ")
                        vali_genero = genero.isalpha()
                        while vali_genero==False or genero!="F" and genero!="f" and genero!="M" and genero!="m":
                            print("---Solo pueden ser las letras M o F---")
                            genero = input("Hombre --- M\nMujer --- F ")
                            vali_genero = genero.isalpha()
                        if genero=="M" or genero=="m":
                            genero = "Hombre"
                        if genero=="F" or genero=="f":
                            genero = "Mujer"
                        a_modificar[3] = genero
                    de_nuevo = input("desea modificar otra cosa:\nSi ---> (S)\nNo ---> (N)\n ")
                    while de_nuevo!="S" and de_nuevo!="s" and de_nuevo!="N" and de_nuevo!="n":
                        print("---Solo pueden ser las letras S o N---")
                        de_nuevo = input("desea modificar otra cosa:\nSi ---> (S)\nNo ---> (N)\n ")
                    if de_nuevo=="S" or de_nuevo=="s":
                        seguir2 = True
                    elif de_nuevo=="N" or de_nuevo=="n":
                        break
                with open ('database.txt','w') as fh:
                    fh.write('{},{},{},{},{},{}\n'.format(a_modificar[0],a_modificar[1],a_modificar[2],a_modificar[3],a_modificar[4],a_modificar[5]))
                for x in no_modificar:
                    with open ('database.txt','a') as fh:
                        fh.write('{},{},{},{},{},{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
                break
            elif user_buscar not in usuarios2:
                print("---Este user no existe---")
        break

def top_10():
    """
    para sacar el top 10
    """
    print("\n")
    top = []
    usuarios_top = []
    topo = []
    print ("-"*20,"TOP 10","-"*20)
    with open("database.txt", "r") as fh:
        datos = fh.readlines()
        for x in datos:
            y = x[:-1].split(",")
            top.append(y)
    for x in top:
        topo.append(int(x[5]))
    
    topo = sorted(topo,reverse= True) 
    for x in topo:
        usuarios_top.append(str(x))
    for y in usuarios_top:
        for x in top:
            if y == x[5]:
                user = x[0]
                puntos = x[5]
                tiros = x[4]
                print('{}.......................{}.......................{}\n'.format(user,puntos,tiros))
    print("\n")
    print("-"*48)

def promedios():
    """
    para sacar los promedios
    """
    tiros_prmedio = []
    todos= []
    cant_de_jugadores = 0
    m = []
    f = []
    lista5_18 = []
    lista19_45 = []
    lista46_60 = []
    lista61_100 = []
    carajitos = 0
    adulto =  0
    pure = 0 
    pure_de_pures = 0 
    edades = [] 
    with open ('database.txt','r') as fh:
        datos = fh.readlines()
        for x in datos:
            usuario = x[:-1].split(',')
            todos.append(usuario)
        for x in todos:
            tiros_prmedio.append(int(x[4]))
            cant_de_jugadores = cant_de_jugadores + 1
        print("Promedio de tiros efectuados para ganar: ",(sum(tiros_prmedio))/cant_de_jugadores)
        for x in todos:
            if x[3]=="Hombre":
                m.append(int(x[5]))
            if x[3]=="Mujer":
                f.append(int(x[5]))
        print("Tiros totales por hombres: ",sum(m))
        print("Tiros totales por mujeres: ",sum(f))
        for x in todos:
            x[2] = int(x[2])
            if x[2]<19:
                lista5_18.append(x[2])
                carajitos = carajitos + 1
            if x[2]<46 and x[2]>18:
                lista19_45.append(x[2])
                adulto = adulto + 1
            if x[2]<61 and x[2]>45:
                lista46_60.append(x[2])
                pure = pure + 1
            if x[2]<101 and x[2]>60:
                lista61_100.append(x[2])
                pure_de_pures = pure_de_pures + 1
        edades.append(carajitos)
        edades.append(adulto)
        edades.append(pure)
        edades.append(pure_de_pures)
        if max(edades)==edades[0]:
            print("Los jugadores que mas juegan se encuetran de 5 a 18")
        if max(edades)==edades[1]:
            print("Los jugadores que mas juegan se encuetran de 19 a 45")
        if max(edades)==edades[2]:
            print("Los jugadores que mas juegan se encuetran de 46 a 60")
        if max(edades)==edades[3]:
            print("Los jugadores que mas juegan se encuetran de 61 a 100")



        


def main():
    """
    Funcion donde se va a correr el juego
    """
    print("-"*50,"Bienvenido a Battleship","-"*50)
    menu = input("\nque deseas hacer\njugar ---> 1\nmodificar ---> 2\nPromedios ---> 3\nTop 10 ---> 4\n ")
    while menu!="1" and menu!="2" and menu!="3" and menu!="4":
        print("---Solo pueden ser los numeros 1, 2, 3 y 4---")
        menu = input("\nque deseas hacer\njugar ---> 1\nmodificar ---> 2\nPromedios ---> 3\nTop 10 ---> 4\n ")
    seguir = True
    while seguir:
        if menu=="1":
            datos_jugador()
            juego()
            print(usuario_en_uso)
            if user not in usuarios:
                usuario_en_uso.append(tiritos)
                usuario_en_uso.append(puntos)
            else:
                tiros_totales = int(usuario_en_uso[4]) + tiritos
                puntos_totales = int(usuario_en_uso[5]) + puntos 
                usuario_en_uso.pop(4)
                usuario_en_uso.pop(4)
                usuario_en_uso.append(tiros_totales)
                usuario_en_uso.append(puntos_totales)
            for x in usuario_en_uso:
                print(x)        
            
            with open ('database.txt','w') as fh:
                fh.write('{},{},{},{},{},{}\n'.format(usuario_en_uso[0],usuario_en_uso[1],usuario_en_uso[2],usuario_en_uso[3],usuario_en_uso[4],usuario_en_uso[5]))
            for x in datosssss:
                with open ('database.txt','a') as fh:
                    fh.write('{},{},{},{},{},{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
        if menu=="2":
            modificar()
        if menu=="3":
            promedios()
        if menu=="4":
            top_10()
        print("\n\n")
        otra_cosa = input("Quieres hacer algo mas:\nSi ---> (S)\nNo ---> (N)\n ")
        while otra_cosa!="s" and otra_cosa!="S" and otra_cosa!="N" and otra_cosa!="n":
            print("---Solo se permiten las letras S y N")
            otra_cosa = input("Quieres hacer algo mas:\nSi ---> (S)\nNo ---> (N)\n ")
        if otra_cosa=="S" or otra_cosa=="s":
            seguir = True
            menu = input("\nque deseas hacer\njugar ---> 1\nmodificar ---> 2\nPromedios ---> 3\nTop 10 ---> 4\n") 
        else:
            break
    print("-"*30,"Gracias por jugar","-"*30)
main()

#sirve plis


###########################################################

