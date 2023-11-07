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


def menú_inicial():
    """
    Imprime el banner de bienvenida y muestra y valida el
    menú inicial del juego.
    """

    print("\033[38;2;255;211;64m ┌──────────────────────────────────────┐ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  SOLARPUNK Y JARDINERÍA CLANDESTINA  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  <<<<<<<<< MENÚ PRINCIPAL >>>>>>>>>  │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m │  [1] Iniciar juego                   │ \033[0;m")
    print("\033[38;2;255;211;64m │  [2] Instrucciones                   │ \033[0;m")
    print("\033[38;2;255;211;64m │  [3] Sobre Jardinería clandestina    │ \033[0;m")
    print("\033[38;2;255;211;64m │                                      │ \033[0;m")
    print("\033[38;2;255;211;64m └──────────────────────────────────────┘ \033[0;m")
    print()

    opción = menú_inicial_aux()

    # Validaciones
    if opción.isdigit():
        if 1 <= int(opción) <= 3:
            # print("\033[2J\033[1;1f")
            # Aquí debe ir alguna referencia para el menú de dificultad
            print("Menú de dificultad")

        else:
            print("\033[;31m Opción no válida.\n \033[0;m")
            menú_inicial_aux()

    else:
        print("\033[;31m Entrada no válida. Únicamente números entre 1 y 3.\n \033[0;m")
        menú_inicial_aux()


def menú_inicial_aux():  # Menu Aux 1
    """
    Auxiliar
    """

    opción = input("\033[38;2;255;211;64m Elija una opción: \033[0;m")

    if opción == "1":  # Iniciar juego
        return opción

    elif opción == "2":  # Intrucciones
        return opción

    elif opción == "3":  # Solarpunk y Jardinería clandestina
        return opción

    else:
        return menú_inicial_aux()


def principal():
    menú_inicial()


principal()
