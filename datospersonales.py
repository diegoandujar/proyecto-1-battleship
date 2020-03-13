from usuario import usuario


lista_de_jugadores = []

def datos_jugador():
    global edad, dicc_datps_per, genero
    user = input("Nombre de usuario: ")
    while  len(user)>10 or " " in user:
        if len(user)>10:
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
    vali_edad = edad.isdigit()
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
    seguir = True
    while seguir:
        seguro = input("\nDesea hacer un ultimo cambio a sus datos personales:\nSi --->(S)\nNo --->(N)\n---> ")
        vali_seguro = seguro.isalpha()
        while vali_seguro == False:
            print("---Solo pueden ser letras---")
            seguro = input("Si --->(S)\nNo-->(else)\n---> ")
            vali_seguro = seguro.isalpha()
        if seguro == "s" or seguro == "S":
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
            if que_desea=='1':
                user = input("Nombre de usuario: ")
                while  len(user)>10 or " " in user:
                    if len(user)>10:
                        print("---No pueden ser mas de 30 caracteres---")
                        user = input("Ingrese su usuario nuevamente: ")
                    if " " in user:
                        print("---No se pueden espacios---")
                        user = input("Ingrese su usuario nuevamente: ") 
            if que_desea=='3':
                edad = input("Coloque su edad: ")
                vali_edad = edad.isdigit()
                while vali_edad==False or int(edad)<5 or int(edad)>100:
                    print("---Solo pueden ser numeros enteros entre 5 y 100---") 
                    edad = input("Repita su edad: ")
                    vali_edad = edad.isdigit()
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
        if seguro!="s" and seguro!="S":
            break
        
    dicc_datps_per = {
        "Nombre": nombre_completo,
        "user": user,
        "edad": edad,
        "genero": genero
    }
    print(dicc_datps_per)
    # print(edad)
    # print("\n",lista5_18,"\n",lista19_45,"\n",lista46_60,"\n",lista61_100)

    # print("\n",10*"-","\nUser: ",user,"\nEdad: ",edad,"\nGenero: ",genero,"\n",10*"-")
# def juego():
#     tablero = {A=[1,2,3,4,5,6,7,8,9,10,11],B=[1,2,3,4,5,6,7,8,3,10,11],B=[1,2,3,4,5,6,7,8,3,10,11],B=[1,2,3,4,5,6,7,8,3,10,11]}

def nuevos_usuarios():
  global lista5_18, lista19_45, lista46_60, lista61_100,jugadores, jugadoras
  jugadoras = 0
  jugadores = 0
  jugadores_tatales = []
  lista5_18 = []
  lista19_45 = []
  lista46_60 = []
  lista61_100 = []
  seguir = True
  while seguir:
    datos_jugador()
    if genero=="Hombre":
        jugadores = jugadores + 1
    else:
        jugadoras = jugadoras + 1  
    jugadores_tatales.append(dicc_datps_per)
    if edad>=5 and edad<=18:
        lista5_18.append(dicc_datps_per)
    elif edad>18 and edad<=45:
        lista19_45.append(dicc_datps_per)
    elif edad>45 and edad<=60:
        lista46_60.append(dicc_datps_per)
    elif edad>60 and edad<=100:
        lista61_100.append(dicc_datps_per)
    mas_jugadores = input("quieres meter mas jugadores:\nSi ---> (S)\nNo ---> (N)\n ---> ")
    vali_mas_jugadores = mas_jugadores.isalpha()
    while vali_mas_jugadores == False or mas_jugadores!="S" and mas_jugadores!="s" and mas_jugadores!="n" and mas_jugadores!="N":
      print("---Solo se puede colocar S o N---")
      mas_jugadores = input("quieres meter mas jugadores:\nSi ---> (S)\nNo ---> (N)\n ---> ")
      vali_mas_jugadores = mas_jugadores.isalpha()
    if mas_jugadores!="s" and mas_jugadores!="S":
      break
nuevos_usuarios()
print("\n",lista5_18,"\n",lista19_45,"\n",lista46_60,"\n",lista61_100,"\njugadores: ",jugadores,"\njugadoras: ",jugadoras)