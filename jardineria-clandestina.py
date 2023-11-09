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


msj_error = ""  # Variable que muestra un mensaje de error.

def menú_dificultad():
    """
    Función que muestra el menú de dificultad y valida que
    la entrada del jugador sea un número entre 1 y 4.
    """

    global msj_error

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

    print(msj_error)

    dificultad = input("\033[38;2;255;211;64m >> \033[0;m")

    if dificultad.isdigit():
        dificultad = int(dificultad)

        if 1 <= dificultad <= 4:
            if dificultad == 1:  # Fácil
                print("\033[2J\033[1;1f")
                print("\nFácil\n")

            elif dificultad == 2:  # Normal
                print("\033[2J\033[1;1f")
                print("\nNormal\n")

            elif dificultad == 3:  # Difícil
                print("\033[2J\033[1;1f")
                print("\nDíficil\n")

            elif dificultad == 4:  # Personalizado
                print("\033[2J\033[1;1f")
                print("\nPersonalizado\n")
                # Aquí se llama a la función para setear el tamaño nxm
                # de la matriz.

        else:
            print("\033[2J\033[1;1f")
            msj_error = "\033[38;2;255;0;0m \nOpción no válida.\n \033[0;m"
            menú_dificultad()

    else:
        print("\033[2J\033[1;1f")
        msj_error = "\033[38;2;255;0;0m \nEntrada no válida. Solo números entre 1 y 4.\n \033[0;m"
        menú_dificultad()



def menu_dificultad():
    """
    Menú para escoger la dificultad
    Modifica la variable "dificultad"
    """
    global dificultad
    print("Elija su dificultad:")
    print("1: Fácil")
    print("2: Medio")
    print("3: Dificil")
    print("4: Personalizado")
    dificultad = menu_dificultad_aux()
     

def menu_dificultad_aux():
    """
    Válida la opción elegida para la dificultad
    """
    n = input("Opción: ")
    if not n.isdigit():
        print("Sólo de números")
        return menu_dificultad_aux()
    
    if int(n) < 1 or int(n) > 4 :
        print("Solamente números entre 1 y 4")
        return menu_dificultad_aux()
    
    return int(n)


def crear_matriz_aux():
    """
    Escoge las dimensiones para 
    crear una matriz
    """
    global dificultad
    #Dificuldades default
    if dificultad == 1 :
        mapa_juego = crear_matriz(6)
    elif dificultad == 2:
        mapa_juego = crear_matriz(10)
    elif dificultad == 3:
        mapa_juego = crear_matriz(18)
    
    #Personalizadas
    elif dificultad == 4 :   
        #Validaciones     
        n = input("Inserte el número de celdas: ")
        if not n.isdigit():
            print("Solo de números")
            return crear_matriz_aux()
        if int(n) <= 0:
            print("Cantidad no válida")
            return crear_matriz_aux()
        #Crear matriz
        mapa_juego = crear_matriz(int(n))


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


def principal():
    bienvenida()
    menú_principal()
    menu_dificultad()
    crear_matriz_aux()
    mostrar_matriz()
    # desvincularla del menú incial, ya que necesito llamarla cuando
    # la opción elegida es 1.
    # Mostrar ciudad (matriz)


principal()
