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


def bienvenida():
    """
    Imprime el banner de bienvenida y el menú inicial
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


def menú_inicial():
    """
    Solicita al jugador que elija una opción y valida que
    la entrada sea un número entre 1 y 3.
    """

    opción = input("\033[38;2;255;211;64m >> \033[0;m")

    if opción.isdigit():
        opción = int(opción)

        if 1 <= opción <= 3:
            # print("\033[2J\033[1;1f")

            if opción == 1:  # Iniciar juego
                print("\033[2J\033[1;1f")
                print("\nMenú de dificultad\n")

            elif opción == 2:  # Intrucciones
                print("\033[2J\033[1;1f")
                print("\nIntrucciones\n")

            elif opción == 3:  # Solarpunk y jardinería clandestina
                print("\033[2J\033[1;1f")
                print("\nSolarpunk y jardinería clandestina\n")

        else:
            print("\033[38;2;255;0;0m Opción no válida.\n \033[0;m")
            menú_inicial()

    else:
        print("\033[38;2;255;0;0m Entrada no válida. Solo números entre 1 y 3.\n \033[0;m")
        menú_inicial()


def principal():
    bienvenida()
    menú_inicial()
    # Menú de dificultad
    # Mostrar ciudad (matriz)


principal()
