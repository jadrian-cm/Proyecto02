#!usr/bin/python3

# Integrantes:

# Pseudoesquema:
# Menú Inicial: Iniciar juego, instrucciones y solarpunk y jardinería clandestina
# Menú Dificultad: Fácil, medio, díficil y personalizado
# Mostrar matriz, que sería la ciudad
# Menú para las acciones: Planta, Semilla y Ciclovía
# Actualizar matriz
# Programar la municipalidad:
# - Establecer estados
# - Crear función que verifique el estado de la matriz
# Crear función para verificar game over
# Preguntar si se quiere jugar de nuevo

#Semillas: [nombre, turnos para crecer, turnos vivas]
semillas_facil = [ ["cosmos", 2], ["zinias", 3], ["salvias", 2], ["kiri", 3], ["herbaceas", 2] ]
semillas_medio = [ ["cerezo", 4], ["tomate", 3], ["rosas", 3], ["tulipanes", 4], ["mamón chino", 4]]
semillas_dificil = [ ["girasoles", 4, 9], ["papas", 5, 15], ["vinca", 5, 15], ["lirio", 5,15], ["dedalera", 6, 25] ]
semillas = []

dificultad = 0 #Nivel de dificultad
mapa_juego = [] #Mapa que se va a usar


def bienvenida():
    """
    Imprime el banner de bienvenida y el menú inicial.
    """

    print("\033[38;2;255;211;64m ┌──────────────────────────────────────┐ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  SOLARPUNK Y JARDINERÍA CLANDESTINA  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  ───────── MENÚ PRINCIPAL ─────────  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  [1] Iniciar juego                   │ \033[0;m")
    print("\033[38;2;255;211;64m │  [2] Instrucciones                   │ \033[0;m")
    print("\033[38;2;255;211;64m │  [3] Sobre jardinería clandestina    │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m └──────────────────────────────────────┘ \033[0;m")
    print()


def menú_principal():
    """
    Función que solicita al jugador que elija una opción
    y valida que la entrada sea un número entre 1 y 3.
    """

    opción = input("\033[38;2;255;211;64m >> \033[0;m")

    if opción.isdigit():
        opción = int(opción)

        if 1 <= opción <= 3:
            # print("\033[2J\033[1;1f")

            if opción == 1:  # Iniciar juego
                print("\033[2J\033[1;1f")
                menú_dificultad()

            elif opción == 2:  # Intrucciones
                print("\033[2J\033[1;1f")
                print("\nIntrucciones\n")

            elif opción == 3:  # Solarpunk y jardinería clandestina
                print("\033[2J\033[1;1f")
                print("\nSolarpunk y jardinería clandestina\n")

        else:
            print("\033[38;2;255;0;0m Opción no válida.\n \033[0;m")
            menú_principal()

    else:
        print("\033[38;2;255;0;0m Entrada no válida. Solo números entre 1 y 3.\n \033[0;m")
        menú_principal()


def menú_dificultad():
    """
    Función que muestra el menú de dificultad y valida que
    la entrada del jugador sea un número entre 1 y 4.
    
    Menú para escoger la dificultad
    Modifica la variable "dificultad"
    """

    global dificultad

    print("\033[38;2;255;211;64m ┌──────────────────────────────────────┐ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  SOLARPUNK Y JARDINERÍA CLANDESTINA  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  ───── DIFICULTADES DEL JUEGO ─────  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  [1] Fácil                           │ \033[0;m")
    print("\033[38;2;255;211;64m │  [2] Normal                          │ \033[0;m")
    print("\033[38;2;255;211;64m │  [3] Díficil                         │ \033[0;m")
    print("\033[38;2;255;211;64m │  [4] Personalizado                   │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m └──────────────────────────────────────┘ \033[0;m")
    print()

    dificultad = menu_dificultad_aux()
    
    dificultad = int(dificultad)

    if 1 <= dificultad <= 4:
        if dificultad == 1:  # Fácil
            print("\033[2J\033[1;1f")
            print("\nFácil\n")
            crear_matriz_aux()
            mostrar_matriz()

        elif dificultad == 2:  # Normal
            print("\033[2J\033[1;1f")
            print("\nNormal\n")
            mostrar_matriz()

        elif dificultad == 3:  # Difícil
            print("\033[2J\033[1;1f")
            print("\nDíficil\n")
            mostrar_matriz()

        elif dificultad == 4:  # Personalizado
            print("\033[2J\033[1;1f")
            print("\nPersonalizado\n")
            mostrar_matriz()
            # Aquí se llama a la función para setear el tamaño nxm
            # de la matriz.
     

def menu_dificultad_aux():
    """
    Valida la opción elegida para la dificultad
    """
    
    n = input("\033[38;2;255;211;64m >> \033[0;m")
    
    if not n.isdigit():
        # print("\033[2J\033[1;1f")
        print("\033[38;2;255;0;0m Entrada no válida. Solo números entre 1 y 4.\n \033[0;m")
        return menu_dificultad_aux()
    
    if int(n) < 1 or int(n) > 4 :
        print("\033[38;2;255;0;0m Solamente números entre 1 y 4.\n \033[0;m")
        return menu_dificultad_aux()
    
    return int(n)


def crear_matriz_aux():
    """
    Escoge las dimensiones para crear una matriz.
    """

    global dificultad
    global mapa_juego
    global semillas
    
    # Dificuldades default
    if dificultad == 1 :
        mapa_juego = crear_matriz(6)
        semillas = semillas_facil
    
    elif dificultad == 2:
        mapa_juego = crear_matriz(10)
        semillas = semillas_medio
    
    elif dificultad == 3:
        mapa_juego = crear_matriz(18)
        semillas = semillas_dificil

    # Personalizadas
    elif dificultad == 4 :   
        # Validaciones     
        n = input("Inserte el número de celdas: ")
        
        if not n.isdigit():
            print("Solo de números")
            return crear_matriz_aux()
        
        if int(n) <= 0:
            print("Cantidad no válida")
            return crear_matriz_aux()
        
        # Crear matriz
        mapa_juego = crear_matriz(int(n))
        semillas = semillas_medio


def crear_matriz(n):
    """
    Crea una matriz con las dimensiones
    del parametro de entrada
    """
    
    global mapa_juego
    
    for i in range(n):
        fila = []
        
        for j in range(n):
            fila.append("☆")
        mapa_juego.append(fila)
   
    return mapa_juego


def mostrar_matriz():
    """
    Muestra los datos del tablero
    """
    
    global mapa_juego
    
    for columna in mapa_juego :
        print(columna)


<<<<<<< HEAD
def menu_acciones():
    """
    Menu que le permite al usuario escoger 
    su accion en el turno de juego
    """
    print("1: Sembrar una semmilla")
    print("2: Sembrar una planta")
    print("3: Crear una ciclovía")
    
    opcion = input("Opción: ")
    
    if not validar_opción(opcion, 1, 3) :
        return menu_acciones


def solicitar_coordenadas(opcion):
    """
    Menu que solicita al jugador el espacio donde
    quiere efectuar la accion previamente seleccionada
    """
    global mapa_juego
    
    print("Inserte las coordenadas")
    x = input("Espacio horizontal: ")
    y = input("Espacio vertical: ")
    
    if not validar_opción(x, 0, len(mapa_juego)-1) or not validar_opción(y, 0, len(mapa_juego)-1):
        return solicitar_coordenadas(opcion)


def validar_opción(opcion, n1, n2):
    """
    Función para validar datos
    """
    
    if not opcion.isdigit():
        print("Solo de números")
        return False
    
    if int(opcion) < n1 or int(opcion) > n2 :
        print("Solo de números entre " + str(n1) + " y " + str(n2) )
        return False
    
    return True


def menu_sembrar_semilla():
    """
    Menu de la opción sembrar semillas
    """
    global semillas
    print("¿Qué semilla desea plantar?")
    print("No----------Nombre----------Carga----------Tiempo viva")
    print()
    print()
    print("0-----------"+ str(semillas[0][0]) + "------------" + str(semillas[0][1]) + "-----------------" + str(semillas[0][2]) )
    print()    
    print("1-----------"+ str(semillas[1][0]) + "-----------" + str(semillas[1][1]) + "-----------------" + str(semillas[1][2]) )
    print()    
    print("2-----------"+ str(semillas[2][0]) + "-------------" + str(semillas[2][1]) + "-----------------" + str(semillas[2][2]) )
    print()    
    print("3-----------"+ str(semillas[3][0]) + "---------" + str(semillas[3][1]) + "-----------------" + str(semillas[3][2]) )
    print()    
    print("4-----------"+ str(semillas[4][0]) + "-------------" + str(semillas[4][1]) + "-----------------" + str(semillas[4][2]) )
    print()
    print()
    
    opcion = input("Número de planta: ")
    if not validar_opción( opcion, 0, 4 ) :
        return menu_sembrar_semilla()

    opcion = semillas[ int(opcion) ]
    print(opcion)
=======
def estado_matriz():
    """
    Función que verifica qué contiene cada casilla de la
    matriz, para decidir la cómo actuará la municipalidad.
    """

    global mapa_juego




    return None
>>>>>>> d5810b9d33524ebc15900a5c6c924e6ed0892fc5


def principal():
    global dificultad

    bienvenida()
    menú_principal()
<<<<<<< HEAD
    menu_dificultad()
    crear_matriz_aux()
    mostrar_matriz()
    # desvincularla del menú incial, ya que necesito llamarla cuando
    # la opción elegida es 1.
    # Mostrar ciudad (matriz)
=======
    # Aquí debería ir la función menú_dificultad, pero no sé cómo
    # desvincularla del menú incial, ya que necesito llamarla cuando
    # la opción elegida es 1.
    # Mostrar ciudad (matriz)
    mostrar_matriz()
>>>>>>> d5810b9d33524ebc15900a5c6c924e6ed0892fc5




