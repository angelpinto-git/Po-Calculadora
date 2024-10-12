import os


from termcolor import cprint


def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    #cprint('\n--- TODO List Menu ---', 'red')
    cprint('\n--- CALCULADORA ---', 'red')
    cprint('1. SUMA', 'yellow')
    cprint('2. Resta', 'yellow')
    cprint('3. Multiplicación', 'yellow')
    cprint('4. Dividir', 'yellow')
    cprint('5. Historial', 'yellow')
    cprint('0. SALIR', 'yellow')
