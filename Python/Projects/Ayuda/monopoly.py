import matplotlib.pyplot as plt
import random
import time

#Objeto con el que se veran y administrara cada encasillado y localizacion en el cuadro de juego
class Propiedad:
    nombre = ""
    precio_de_lista = 0
    precio_por_casa = 0
    precio_por_hotel = 0
    renta = 0
    renta_por_casa = 0
    renta_por_hotel = 0
    casas = 0
    hoteles = 0
    propietario = 0

    def __init__(self, nombre, precio_de_lista, precio_por_casa, precio_por_hotel, renta, renta_por_casa, renta_por_hotel):
        #Nombre de lugar
        self.nombre = nombre
        #Cuanto le cuesta al jugador comprar el lugar
        self.precio_de_lista = precio_de_lista
        #Cuanto cuesta anadirle una casa en este lugar
        self.precio_por_casa = precio_por_casa
        #Cuanto cuesta anadirle un hotel a este lugar
        self.precio_por_hotel = precio_por_hotel
        #Cuanto hay que pagar por caer en este lugar
        self.renta = renta
        #Cuanto hay que pagar adicional por cada casa que haya
        self.renta_por_casa = renta_por_casa
        #Cuanto hay que pagar adicional por cada hotel que haya
        self.renta_por_hotel = renta_por_hotel
        #Inicialmente no hay casas ni hoteles, ni propietario
        self.casas = 0
        self.hoteles = 0
        self.propietario = 0

    def renta_total(self):
        return self.renta + self.renta_por_casa * self.casas + self.renta_por_hotel * self.hoteles

    def comprar_propiedad(self, jugador):
        #Procurar que el jugador tenga suficiente dinero para comprar propiedad
        if jugador.dinero > self.precio_de_lista:
            jugador.dinero -= self.precio_de_lista  #Quitar dinero
            jugador.propiedades.append(self)        #Anadir propiedad a usuario
            self.propietario = jugador              #Poner jugador como propietario
            return "Compra exitosa!"
        return "No tienes suficiente dinero"

    def comprar_casa(self):
        if self.casas < 4 and self.hoteles != 1:    #Criterios para anadir una casa
            #Procurar tener el dinero necesario para comprar casa
            if self.propietario.dinero > self.precio_por_casa:
                self.casas += 1                     #Anadir casa
                self.propietario.dinero -= self.precio_por_casa #Quitar dinero
                return "Compra exitosa!"
            else:
                return "No tienes suficiente dinero"
        elif self.casas == 4 and self.hoteles == 0: #Criterios para anadir un hotel
            #Procurar tener el dinero necesario para comprar hotel
            if self.propietario.dinero > self.precio_por_hotel:
                self.casas = 0                      #Remover todas las casas
                self.hoteles = 1                    #Anadir hotel
                self.propietario.dinero -= self.precio_por_hotel #Quitar dinero
                return "Compra exitosa!"
            else:
                return "No tienes suficiente dinero"
        return "No tienes suficientes casas para comprar el hotel o ya tienes el maximo"


#Objeto con el que se rastreara la informacion de cada jugador (computadora y personas)
class Jugador:
    nombre = ""
    dinero = 0
    propiedades = []
    posicion = 0
    dado = 0
    vueltas = 0
    historial_dinero = [dinero]
    historial_propiedades = [[]]

    def __init__(self, nombre, dinero, propiedades):
        #Nombre con el que se hará referencia al jugador
        self.nombre = nombre
        #Cantidad de dinero de jugador
        self.dinero = dinero
        #Lista de localizaciones/propiedades del jugador
        self.propiedades = propiedades

        #Variables predeterminadas
        self.posicion = 0
        self.dado = 0
        self.vueltas = 0
        self.historial_dinero = [self.dinero]   #Comienza el juego con dinero
        self.historial_propiedades = [[]]       #Comienza el juego con 0 propiedades

    def imprimir_posicion(self, posiciones):
        posicion = posiciones[self.posicion]    #Buscar encasillado de tablero donde esta
        print("-----")                          #Division
        print("Posicion numero: " + str(self.posicion+1))
        print("Vuelta numero:   " + str(self.vueltas))
        print("Nombre:          " + posicion.nombre)
        print("Casas:           " + str(posicion.casas))
        print("Hoteles:         " + str(posicion.hoteles))
        print("Precio de lista: $" + str(posicion.precio_de_lista))
        print("Renta Total:     $" + str(posicion.renta_total()))
        #Si tiene propietario, imprimirlo tambien. Sino, no
        if posicion.propietario != 0:
            print("Pertenece a:     " + posicion.propietario.nombre)
        else:
            print("No pertenece a nadie")
        print("-----")                          #Division

    def imprimir_dinero(self):
        print("-----")                          #Division
        print("Dinero en cuenta: $" + str(self.dinero))
        print("-----")                          #Division

    def imprimir_propiedades(self, posiciones):
        #Procurar que hayan propiedades
        if len(self.propiedades) > 0:
            print("-----")                          #Division
            for propiedad in self.propiedades:
                #Indice de posicion de propiedad con relacion al tablero
                index = posiciones.index(propiedad)
                print("Nombre:                      " + propiedad.nombre)
                print("Posicion                     " + str(index+1))
                print("Casas:                       " + str(propiedad.casas))
                print("Hoteles:                     " + str(propiedad.hoteles))
                print("Precio de lista:             $" + str(propiedad.precio_de_lista))
                print("Precio por casa:             $" + str(propiedad.precio_por_casa))
                print("Precio por hotel:            $" + str(propiedad.precio_por_hotel))
                print("Renta:                       $" + str(propiedad.renta))
                print("Renta adicional por casa:    $" + str(propiedad.renta_por_casa))
                print("Renta adicional por hotel:   $" + str(propiedad.renta_por_hotel))
                print("-----")                          #Division
            print("**Total: " + str(len(self.propiedades)) + " propiedades")
        else:
            print("No tienes propiedades en estos momentos")


#Funcion con intencion de desplegar pequeno efecto de que se esta procesando
#informacion y esta cargando el programa
def cargando(mensaje, puntos=3, segundos=1):
    print(mensaje, end='\r')
    for i in range(int(puntos)):
        p = "." * (i+1)
        print(mensaje + " " + p, end='\r')
        time.sleep(segundos)
    print()


#Funcion para simular lanzamiento de dos dados
def tirar_dados():
    return random.randint(2,12)


#Funcion para adjudicar bono de 'Go' y anadir vuelta correspondiente
def pasar_go(jugador):
    print(jugador.nombre + " completo una vuelta!")
    jugador.vueltas += 1
    jugador.dinero += 200   #Bonificacion de $200


#Funcion para ocuparse de cobrarle la renta a un usuario cuando una propiedad
#tiene propietario o ofrecerle la propiedad a la venta cuando no lo tiene
def cobrar_o_vender_usuario(jugador, posiciones):
    global especiales           #Incluye aquellos lugares que no se cobran ni venden
    posicion = posiciones[jugador.posicion]

    #Salir si el lugar te pertenece o si es uno de aquellos lugares especiales
    if posicion in especiales or posicion in jugador.propiedades:
        return

    #Si no tiene propietario ...
    if posicion.propietario == 0:
        #Mantener loop hasta que el usuario conteste "s" o "n" donde se hace un break
        while True:
            print("Quisieras comprar " + posicion.nombre + " por $" + str(posicion.precio_de_lista) + "? (s/n)")
            entrada = input(" < ")
            if entrada == "s":
                print(posicion.comprar_propiedad(jugador))
                break
            elif entrada == "n":
                break
            else:
                print("Entra un dato valido!")
    else:                           #Ya tiene propietario, por lo que se cobra renta
        renta = posicion.renta_total()          #Computo de renta
        jugador.dinero -= renta                 #Quitar dinero
        posicion.propietario.dinero += renta    #Darselo al propietario
        print("Se le cobro $" + str(renta) + "de renta a " + jugador.nombre + " por caer en " + posicion.nombre)


#Funcion para ocuparse de cobrarle la renta a una computadora cuando una propiedad
#tiene propietario o ofrecerle la propiedad a la venta cuando no lo tiene.
#La diferencia clave es que esta no requiere entrada del usuario
def cobrar_o_vender_computadora(computadora, posiciones):
    global especiales           #Incluye aquellos lugares que no se cobran ni venden
    posicion = posiciones[computadora.posicion]

    #Salir si el lugar te pertenece o si es uno de aquellos lugares especiales
    if posicion in especiales or posicion in computadora.propiedades:
        return

    #Si no tiene propietario ...
    if posicion.propietario == 0:
        #Decidir si comprar casa o no con 50% probabilidad y si tiene el dinero
        comprar = random.randint(0,1)
        if comprar == 1 and computadora.dinero > posicion.precio_de_lista:
            print(posicion.comprar_propiedad(computadora))
            print(computadora.nombre + " compro " + posicion.nombre + " con renta de $" + str(posicion.renta_total()))
        else:
            print(computadora.nombre + " no compro " + posicion.nombre)
    else:                           #Ya tiene propietario, por lo que se cobra renta
        renta = posicion.renta_total()          #Computo de renta
        computadora.dinero -= renta                 #Quitar dinero
        posicion.propietario.dinero += renta    #Darselo al propietario
        print("Se le cobro a " + computadora.nombre + " renta de $" + str(renta) + " por caer en " + posicion.nombre)


#Funcion que se ocupara de manejar interface y acciones de una persona que juegue 
def turno_usuario(usuario, posiciones, oponente):
    print("Tu turno!")
    entrada = "0"
    #1.Recoger entrada de usuario y desplegar informacion
    while True:
        print("Que deseas hacer? Puedes")
        print("(1) Ver mi posicion")
        print("(2) Ver mi dinero")
        print("(3) Ver mis propiedades")
        print("(4) Ver posicion de oponente")
        print("(5) Ver dinero de oponente")
        print("(6) Ver propiedades de oponente")
        print("(7) Comprar casa/hotel")
        print("(8) Lanzar dado")

        entrada = input(" < ")

        if entrada == "1":
            usuario.imprimir_posicion(posiciones)
            print()
        elif entrada == "2":
            usuario.imprimir_dinero()
            print()
        elif entrada == "3":
            usuario.imprimir_propiedades(posiciones)
            print()
        elif entrada == "4":
            oponente.imprimir_posicion(posiciones)
            print()
        elif entrada == "5":
            oponente.imprimir_dinero()
            print()
        elif entrada == "6":
            oponente.imprimir_propiedades(posiciones)
            print()
        elif entrada == "7":
            #Procurar que hayan propiedades. Si no seguir a recoger entrada nuevamente
            if len(usuario.propiedades) < 1:
                print("No tienes propiedades en estos momentos")
                print()
                continue

            print("-----")                          #Division
            print("A cual propiedad le deseas anadir una casa?")
            #Imprimir propiedades
            for i in range(len(usuario.propiedades)):
                print("(" + str(i+1) + ") " + usuario.propiedades[i].nombre)
            p = input(" < ")    # Escoger propiedad
            try:
                p = int(p) - 1
                print(usuario.propiedades[p].comprar_casa())
                print("-----")                          #Division
            except:
                print("Entra un dato valido!")
                print("-----")                          #Division
                continue

        elif entrada == "8":
            break
        else:
            print("Entra un dato valido!")

    #2.Ejecutar tiro de dados y actualizar posicion
    usuario.dado = tirar_dados()
    print("Lanzaste un " + str(usuario.dado))
    if usuario.posicion + usuario.dado >= len(posiciones):
        usuario.posicion += usuario.dado
        pasar_go(usuario)                   #dio una vuelta completa
        usuario.posicion %= len(posiciones)
    else:
        usuario.posicion += usuario.dado
    print("Caiste en " + posiciones[usuario.posicion].nombre)
    print()

    #3.Cobrar renta u ofrecer propiedad para vender
    cobrar_o_vender_usuario(usuario, posiciones)


#Funcion que permitira que un jugador automaticamente haga decisiones de compra,
#venta sin necesiadad de que una persona la maneje
def turno_computadora(computadora, posiciones):
    print("Turno de computadora!")


    #1.Aleatoriamente decide si comrar una casa o no
    if len(computadora.propiedades) > 0:
        comprar = random.randint(0,1)
        if comprar == 1:
            p = random.randint(1,len(computadora.propiedades))-1
            print(computadora.propiedades[p].comprar_casa())

    #2.Ejecutar tiro de dados y actualizar posicion
    computadora.dado = tirar_dados()
    print("La computadora lanzo un " + str(computadora.dado))
    if computadora.posicion + computadora.dado >= len(posiciones):
        computadora.posicion += computadora.dado
        pasar_go(computadora)               #dio una vuelta completa
        computadora.posicion %= len(posiciones)
    else:
        computadora.posicion += computadora.dado
    print("Cayo en " + posiciones[computadora.posicion].nombre)
    print()

    #2.Cobrar renta u ofrecer propiedad para vender
    cobrar_o_vender_computadora(computadora, posiciones)


#Funcion que determinara ganador a partir de si algun jugador se quedo sin
#dinero o verificando aquel que tenga mayor cantidad de propiedades
def determinar_ganador(usuario, computadora):
    print("=== === === === FIN DE JUEGO === === === ===")
    if usuario.dinero < 0:
        print("Te quedaste con $" + str(usuario.dinero))
        print("No tienes dinero para pagar la renta, por lo que perdiste!")
        return
    elif computadora.dinero < 0:
        print("La computadora se quedo con $" + str(computadora.dinero))
        print("No tiene dinero para pagar la renta, por lo que perdio!")
        return

    print("Tus propiedades:")
    usuario.imprimir_propiedades(posiciones)
    print("=== ===")
    print("Propiedades de computadora:")
    computadora.imprimir_propiedades(posiciones)

    print()
    cargando("Procesando", 10, 0.25)
    print()

    if len(usuario.propiedades) > len(computadora.propiedades):
        print("Ganaste!!!")
    elif len(computadora.propiedades) > len(usuario.propiedades):
        print("La computadora gano")
    else:
        #Desempate depende de cantidad de dinero que tengan
        if usuario.dinero >= computadora.dinero:
            print("Ganaste!!")
        else:
            print("La computadora gano")


#Funcion que almacenara datos de computadora, usuario y posiciones en un
#documento CSV
def almacenar_resultados(usuario, computadora, posiciones, nombre_file):
    datos = []
    
    #Datos de usuario
    datos.append([])
    datos[-1].append(usuario.nombre)
    datos[-1].append(str(usuario.dinero))
    datos[-1].append(str(usuario.posicion))
    datos[-1].append(str(usuario.vueltas))
    propiedades = []
    for propiedad in usuario.propiedades:
        propiedades.append(propiedad.nombre)
    datos[-1].extend(propiedades[:])

    #Datos de computadora
    datos.append([])
    datos[-1].append(computadora.nombre)
    datos[-1].append(str(computadora.dinero))
    datos[-1].append(str(computadora.posicion))
    datos[-1].append(str(computadora.vueltas))
    propiedades = []
    for propiedad in computadora.propiedades:
        propiedades.append(propiedad.nombre)
    datos[-1].extend(propiedades[:])

    #Posiciones de tablero
    for posicion in posiciones:
        datos.append([])
        datos[-1].append(posicion.nombre)
        datos[-1].append(str(posicion.precio_de_lista))
        datos[-1].append(str(posicion.precio_por_casa))
        datos[-1].append(str(posicion.precio_por_hotel))
        datos[-1].append(str(posicion.renta))
        datos[-1].append(str(posicion.renta_por_casa))
        datos[-1].append(str(posicion.renta_por_hotel))
        datos[-1].append(str(posicion.casas))
        datos[-1].append(str(posicion.hoteles))
        if isinstance(posicion.propietario, Jugador):
            datos[-1].append(posicion.propietario.nombre)
        else:
            datos[-1].append("No tiene propietario")

    #https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    with open(nombre_file, 'w') as fp:
        for linea in datos:
            linea = ','.join(linea)
            fp.write(linea+'\n')


#Funcion que graficara datos de usuario y computadora. Especificamente su
#historial de dinero e historial de propiedades 
def graficar_resultados(usuario, computadora):
    #https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/subplot.html
    #https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html
    xu = list(range(len(usuario.historial_dinero)))
    xc = list(range(len(computadora.historial_dinero)))

    plt.subplot(2,1,1)
    plt.title('Dinero con Respecto a Turno')
    plt.plot(xu, usuario.historial_dinero, 'o-', label='Dinero Usuario')
    plt.plot(xc, computadora.historial_dinero, '.-', label='Dinero Computadora')
    plt.legend(loc='lower left')
    plt.ylabel('Dinero')
    plt.xlabel('Turno')

    xu = list(range(len(usuario.historial_propiedades)))
    xc = list(range(len(computadora.historial_propiedades)))
    yu = list([len(propiedades) for propiedades in usuario.historial_propiedades])
    yc = list([len(propiedades) for propiedades in computadora.historial_propiedades])

    plt.subplot(2,1,2)
    plt.title('Cantidad de Propiedades con Respecto a Turno')
    plt.plot(xu, yu, 'o-', label='Propiedades Usuario')
    plt.plot(xc, yc, '.-', label='Propiedades Computadora')
    plt.legend(loc='lower right')
    plt.ylabel('Cantidad de Propiedades')
    plt.xlabel('Turno')

    plt.show()
    

#0.Preparacion de tablero e informacion basica
maximo_vueltas = 10
#Informacion de: https://monopoly.fandom.com/wiki/Property
posiciones = [
        Propiedad("Go", 0, 0, 0, 0, 0, 0),
        Propiedad("Mediterranean Avenue", 60, 50, 50, 2, 15, 160),
        Propiedad("Baltic Avenue", 60, 50, 50, 4, 20, 320),
        Propiedad("Oriental Avenue", 100, 50, 50, 6, 30, 550),
        Propiedad("Vermont Avenue", 100, 50, 50, 6, 30, 550),
        Propiedad("Connecticut Avenue", 120, 50, 50, 8, 40, 600),
        Propiedad("Free Parking", 0, 0, 0, 0, 0, 0),
        Propiedad("States Avenue", 140, 100, 100, 10, 50, 750),
        Propiedad("Virginia Avenue", 160, 100, 100, 12, 60, 900),
        Propiedad("St. James Place", 180, 100, 100, 14, 70, 950),
        Propiedad("Tennesse Avenue", 180, 100, 100, 14, 70, 950),
        Propiedad("New York Avenue", 200, 100, 100, 16, 80, 1000),
        Propiedad("Free Parking", 0, 0, 0, 0, 0, 0),
        Propiedad("Kentucky Avenue", 220, 150, 150, 18, 90, 1050),
        Propiedad("Indiana Avenue", 220, 150, 150, 18, 90, 1050),
        Propiedad("Illinois Avenue", 240, 150, 150, 20, 100, 1100),
        Propiedad("Park Place", 350, 200, 200, 35, 175, 1500),
        Propiedad("Boardwalk", 400, 200, 200, 50, 200, 2000),
        ]
especiales = [posiciones[0], posiciones[6], posiciones[12]]
usuario = Jugador("1er jugador", 1500, [])
computadora = Jugador("Computadora", 1500, [])

#1.Introduccion
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Bienvenido al juego de Monopolio ... en Puerto Rico")
print("En esta version simplificada del juego gana aquel que")
print("que tenga mayor propiedades al final de " + str(maximo_vueltas))
print("vueltas o pierde aquel que se quede sin dinero antes de estas.")
print("[Mas información ...]")
print()

#2.Secuencia de inicio y determinar quien comienza
print("Para comenzar se arrojaran dados.")
print("Aquel que tenga mayor puntuación al arrojar el dados comienza el juego.")
print("En el caso de empate comienzas el juego tu.")
print()
_ = input("Presione 'Enter' para tirar dados y comenzar juego.")

usuario.dado = tirar_dados()
print("Lanzaste un " + str(usuario.dado))
computadora.dado = tirar_dados()
print("La computadora lanzo un " + str(computadora.dado))
cargando("", 4, 1)

usuario_proximo = True
if computadora.dado > usuario.dado:
    print("Comienza la computadora!")
    usuario_proximo = False
elif usuario.dado > computadora.dado:
    print("Comienzas tu!")
    usuario_proximo = True
print()

#3.Ciclo de juego
while usuario.vueltas < maximo_vueltas and computadora.vueltas < maximo_vueltas and usuario.dinero >= 0 and computadora.dinero >= 0:
    if usuario_proximo:
        turno_usuario(usuario, posiciones, computadora)
        cargando("", 3, 0.5)
        print()
        usuario.historial_dinero.append(usuario.dinero)
        #https://docs.python.org/3.8/library/copy.html
        usuario.historial_propiedades.append(usuario.propiedades[:])
        usuario_proximo = False
    else:
        turno_computadora(computadora, posiciones)
        cargando("", 5, 1)
        print()
        computadora.historial_dinero.append(computadora.dinero)
        #https://docs.python.org/3.8/library/copy.html
        computadora.historial_propiedades.append(computadora.propiedades[:])
        usuario_proximo = True


#4.Concluir juego y graficar resultados
determinar_ganador(usuario, computadora)
almacenar_resultados(usuario, computadora, posiciones, "resultados_monopolio.csv")
graficar_resultados(usuario, computadora)
print()
print("Gracias por jugar!!")
print()
