#!usr/bin/python3

# Integrantes:
# Bryan Fernández Sánchez, 2023131084
# José Carballo Martínez, 2019046749

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
# Algunos uft8icons de plantas: 🌰, 🌱, 🌷, 🌹, 🌺, 🌻, 🌼, 🥀

import random

# Semillas: [nombre, turnos para crecer, turnos vivas]
semillas_facil = [
    ["cosmos", 2],
    ["zinias", 3],
    ["salvias", 2],
    ["kiri", 3],
    ["herbaceas", 2],
]
semillas_medio = [
    ["cerezo", 4],
    ["tomate", 3],
    ["rosas", 3],
    ["tulipanes", 4],
    ["mamón chino", 4],
]
semillas_dificil = [
    ["girasoles", 4, 9],
    ["papas", 5, 15],
    ["vinca", 5, 15],
    ["lirio", 5, 15],
    ["dedalera", 6, 25],
]
semillas = []

# Falta la lista de las plantas

dificultad = 0  # Nivel de dificultad
mapa_juego = []  # Matriz que representa la ciudad


def bienvenida():
    """
    Función que imprime el banner de bienvenida y el
    menú inicial.
    """

    print("\033[38;2;255;211;64m" + "┌──────────────────────────────────────┐" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  SOLARPUNK Y JARDINERÍA CLANDESTINA  │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  ───────── MENÚ PRINCIPAL ─────────  │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [1] Iniciar juego                   │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [2] Instrucciones                   │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [3] Sobre jardinería clandestina    │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "└──────────────────────────────────────┘" + "\033[0;m")
    print()


def menú_principal():
    """
    Función que solicita al jugador que elija una opción
    y valida que la entrada sea un número entre 1 y 3.
    """

    opción = input("\033[38;2;255;211;64m" + ">>> " + "\033[0;m")

    if not validar_opción(opción, 1, 3):
        return menú_principal()
    
    else:
        if int(opción) == 1:  # Iniciar juego
            print("\033[2J\033[1;1f")

        elif int(opción) == 2:  # Intrucciones
            print("\033[2J\033[1;1f")
            print("\nInstrucciones\n")  
            # Aquí se debe agregar el archivo de instrucciones
            # Agregar opción para volver al menú principal

        elif int(opción) == 3:  # Solarpunk y jardinería clandestina
            print("\033[2J\033[1;1f")
            print("\nSolarpunk y jardinería clandestina\n")
            # Aquí debe ir el archivo sobre jardinería clandestina
            # Agregar opción para volver al menú principal


def menú_dificultad():
    """
    Función que muestra el menú de dificultad y valida
    que la entrada del jugador sea un número entre 1 y 4.
    """

    global dificultad

    print("\033[38;2;255;211;64m" + "┌──────────────────────────────────────┐" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  SOLARPUNK Y JARDINERÍA CLANDESTINA  │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  ───── DIFICULTADES DEL JUEGO ─────  │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [1] Fácil                           │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [2] Normal                          │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [3] Díficil                         │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│  [4] Personalizado                   │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "│                                      │" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "└──────────────────────────────────────┘" + "\033[0;m")
    print()

    dificultad = menú_dificultad_aux()

    # dificultad = int(dificultad)

    # if 1 <= dificultad <= 4:
    #     if dificultad == 1:  # Fácil
    #         print("\033[2J\033[1;1f")
    #         return mostrar_matriz()

    #     elif dificultad == 2:  # Normal
    #         print("\033[2J\033[1;1f")
    #         return mostrar_matriz()

    #     elif dificultad == 3:  # Difícil
    #         print("\033[2J\033[1;1f")
    #         return mostrar_matriz()

    #     elif dificultad == 4:  # Personalizado
    #         print("\033[2J\033[1;1f")
    #         return mostrar_matriz()
    #         # Aquí se llama a la función para setear el tamaño nxm
    #         # de la matriz.

    return dificultad


def menú_dificultad_aux():
    """
    Función que valida la opción elegida para la dificultad.
    """

    opción = input("\033[38;2;255;211;64m" + ">>> " + "\033[0;m")
    
    print()

    if not validar_opción(opción, 1, 4):
        return menú_dificultad_aux()

    return int(opción)


def crear_matriz_aux():
    """
    Función que permite escoger las dimensiones para
    crear una matriz.
    """

    global dificultad
    global mapa_juego
    global semillas

    # Dificuldades default
    if dificultad == 1:
        print("\033[2J\033[1;1f")
        mapa_juego = crear_matriz(6, 6)
        semillas = semillas_facil

    elif dificultad == 2:
        print("\033[2J\033[1;1f")
        mapa_juego = crear_matriz(10, 10)
        semillas = semillas_medio

    elif dificultad == 3:
        print("\033[2J\033[1;1f")
        mapa_juego = crear_matriz(18, 18)
        semillas = semillas_dificil

    # Personalizadas
    elif dificultad == 4:
        # Validaciones
        filas = input("\033[38;2;255;211;64m" + "Número de filas: " + "\033[0;m")
        columnas = input("\033[38;2;255;211;64m" + "Número de columnas: " + "\033[0;m")

        if (not validar_opción(filas, 3, 20) or
            not validar_opción(columnas, 3, 20)):
            return crear_matriz_aux()
        
        # Crear matriz
        print("\033[2J\033[1;1f")
        mapa_juego = crear_matriz(int(filas), int(columnas))
        semillas = semillas_medio


def crear_matriz(filas, columnas):
    """
    Función que crea una matriz con las dimensiones del
    parámetro de entrada.
    """

    global mapa_juego

    for _ in range(filas):
        fila = []

        for _ in range(columnas):
           fila.append("🟫")
        
        mapa_juego.append(fila)

    # mapa_juego = [["🟫" for _ in range(columnas)] for _ in range(filas)]

    return mapa_juego


def mostrar_matriz():
    """
    Función que muestra los datos del tablero.
    """

    global mapa_juego

    for fila in mapa_juego:
        for elemento in fila:
            print(elemento, end="")
        print()  # Salto de línea después de cada fila.

    print()


def menú_acciones():
    """
    Función que muestra el menú que le permite al usuario
    escoger una acción en el turno de juego.
    """

    print("\033[38;2;255;211;64m" + "[1] Sembrar una semilla" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "[2] Sembrar una planta" + "\033[0;m")
    print("\033[38;2;255;211;64m" + "[3] Crear una ciclovía" + "\033[0;m")
    print()

    opción = input("\033[38;2;255;211;64m" + ">>> " + "\033[0;m")

    if not validar_opción(opción, 1, 3):
        return menú_acciones()
    
    return opción


def solicitar_coordenadas():
    """
    Función que muestra el menú que solicita al jugador
    el espacio donde quiere efectuar la acción previamente
    seleccionada.
    """

    global mapa_juego

    print()
    print("\033[38;2;255;211;64m" + "Inserte las coordenadas" + "\033[0;m")

    x = input("\033[38;2;255;211;64m" + "Coordenada x: " + "\033[0;m")
    y = input("\033[38;2;255;211;64m" + "Coordenada y: " + "\033[0;m")

    if (not validar_opción(x, 0, len(mapa_juego) - 1) or
        not validar_opción(y, 0, len(mapa_juego) - 1)):
        return solicitar_coordenadas()


def validar_opción(opción, num1, num2):
    """
    Función que valida datos.
    """

    if not opción.isdigit():
        print("\033[38;2;255;0;0m" + "Solo puede ingresar números.\n" + "\033[0;m")
        return False

    if int(opción) < num1 or int(opción) > num2:
        print(
            "\033[38;2;255;0;0m" + "Solo números entre " +
            str(num1) + " y " + str(num2) + ".\n" + "\033[0;m"
        )
        return False

    return True


def menú_sembrar_semilla():
    """
    Función que muestra el menú de la opción sembrar
    semillas.
    """

    global semillas

    print()
    print("\033[38;2;255;211;64m" + "¿Qué semilla desea plantar?\n" + "\033[0;m")
    print(
        "\033[38;2;255;211;64m" +
        "No----------Nombre----------Carga----------Tiempo viva" +
        "\033[0;m"
    )
    print()
    print(
        "\033[38;2;255;211;64m" +
        "0-----------" + str(semillas[0][0]) +
        "------------" + str(semillas[0][1]) +
        "-----------------" + str(semillas[0][2]) +
        "\033[0;m"
    )
    print()
    print(
        "\033[38;2;255;211;64m" +
        "1-----------" + str(semillas[1][0]) +
        "------------" + str(semillas[1][1]) +
        "-----------------" + str(semillas[1][2]) +
        "\033[0;m"
    )
    print()
    print(
        "\033[38;2;255;211;64m" +
        "2-----------" + str(semillas[2][0]) +
        "------------" + str(semillas[2][1]) +
        "-----------------" + str(semillas[2][2]) +
        "\033[0;m"
    )
    print()
    print(
        "\033[38;2;255;211;64m" +
        "3-----------" + str(semillas[3][0]) +
        "------------" + str(semillas[3][1]) +
        "-----------------" + str(semillas[3][2]) +
        "\033[0;m"
    )
    print()
    print(
        "\033[38;2;255;211;64m" +
        "4-----------" + str(semillas[4][0]) +
        "------------" + str(semillas[4][1]) +
        "-----------------" + str(semillas[4][2]) +
        "\033[0;m"
    )
    print()
    print()

    opción = input("\033[38;2;255;211;64m" + "Número de planta: " + "\033[0;m")

    if not validar_opción(opción, 0, 4):
        return menú_sembrar_semilla()

    opción = semillas[int(opción)]

    return opción


def modificar_matriz():
    """
    ...
    """

    return None

# Luego mostrar la matriz actualizada y el menú de acciones

# Estados a programar:
#  + Si en la posición mapa_juego[i][j] hay una semilla:
#     - La municipalidad puede construir
#  + Si en la posición mapa_juego[i][j] hay una planta:
#     - La municipalidad puede arrancarla y construir
#  + Si en la posición mapa_juego[i][j] hay una ciclovía:
#     - La municipalidad puede destruirla y en otro turno construir


# def verificar_estado_matriz(matriz):
#     """
#     Función que verifica qué hay en cada posición de la
#     matriz, para decidir cómo debe proceder el jugador
#     y la municipalidad.
#     """

#     filas = len(matriz)
#     columnas = len(matriz[0])

#     for i in range(filas):
#         for j in range(columnas):
#             elemento = matriz[i][j]

#     return elemento


def municipalidad(matriz):
    """
    Función que compara cada posición del matriz que
    representa la ciudad y construye placas de concreto,
    destruye ciclovías y arranca plantas.
    """

    filas = len(matriz)
    columnas = len(matriz[0])

    # Agrega concreto aleatoriamente entre 0 y n//2 filas.
    cantidad_concreto = random.randint(0, filas // 2)
    for _ in range(cantidad_concreto):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        matriz[fila][columna] = "🔳"

    # Reemplaza la semilla con concreto
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "🌱":
                matriz[i][j] = "🔳"

    # Reemplaza la ciclovía con tierra
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "🚵":
                matriz[i][j] = "🟫"

    # Reemplaza la planta con concreto
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == "🌹":
                matriz[i][j] = "🔳"

    return matriz


def verificar_fin_juego(matriz):
    """
    Función que verifica si el jugador ha ganado o perdido.
    """

    # Verifica filas
    for fila in matriz:
        if contar_objeto("🌹", fila=fila) == len(fila):
            print(
                "\033[38;2;0;255;0m" +
                "¡Has ganado! Toda una fila contiene plantas." +
                "\033[0;m"
            )
            return True
    
        elif contar_objeto("🔳", fila=fila) == len(fila):
            print(
                "\033[38;2;255;0;0m" +
                "¡Has perdido! Toda una fila contiene concreto." +
                "\033[0;m"
            )
            return False
        
    # Verifica columnas
    for i in range(len(matriz[0])):
        columna = [fila[i] for fila in matriz]
        
        if contar_objeto("🌹", columna=columna) == len(columna):
            print(
                "\033[38;2;0;255;0m" +
                "¡Has ganado! Toda una columna contiene plantas." +
                "\033[0;m"
            )
            return True
        
        elif contar_objeto("🔳", columna=columna) == len(columna):
            print(
                "\033[38;2;255;0;0m" +
                "¡Has perdido! Toda una columna contiene concreto." +
                "\033[0;m"
            )
            return False
        
        # Falta verificar diagonales (esto sería puntos extras)

    return False  # El juego aún no ha terminado.


def contar_objeto(objeto, fila=None, columna=None):
    """
    Función que cuenta la cantidad de veces que aparece un
    objeto en una fila o en una columna.
    """
    
    if fila != None and isinstance(fila, list):
        contador = 0

        for elemento in fila:
            if elemento == objeto:
                contador += 1
        
        return contador
    
    elif columna != None and isinstance(columna, list):
        contador = 0

        for elemento in columna:
            if elemento == objeto:
                contador += 1

        return contador
    
    else:
        return (
                "\033[38;2;255;0;0m" +
                "Debes especificar una fila o columna." +
                "\033[0;m"
        )


def nueva_partida():
    """
    Función que le pregunta al usuario si desea jugar
    de nuevo. El juego si no se quiere continuar y ejecuta
    la función principal si se quiere continuar.
    """

    decisión = input(
                    "\033[38;2;255;211;64m" +
                    "¿Deseas jugar otra partida? Sí/No o S/N: " +
                    "\033[0;m"
                )

    if type(decisión) != str:
        print(
            "\033[38;2;255;0;0m" +
            "Solo puedes ingresar Sí/No o S/N.\n" +
            "\033[0;m"
        )
        return nueva_partida()
   
    if decisión == "Sí" or decisión == "S":
        print("\033[2J\033[1;1f")
        return principal()

    elif decisión == "No" or decisión == "N":
        print(
            "\033[38;2;0;255;0m" +
            "Gracias por jugar. ¡Vuelve pronto!\n" +
            "\033[0;m"
        )
        return exit()


def manejador_juego():
    menú_acciones()
    solicitar_coordenadas()
    menú_sembrar_semilla()


def principal():
    """
    Función que se encarga de inicializar el juego.
    """

    global dificultad

    bienvenida()
    menú_principal()
    menú_dificultad()
    crear_matriz_aux()
    mostrar_matriz()
    manejador_juego()
    # desvincularla del menú incial, ya que necesito llamarla cuando
    # la opción elegida es 1.
    # Mostrar ciudad (matriz)


principal()
