from mostrar import clear_console, display_menu
from puntos import suma, subtraction, multiply, split, operations

def main():
    historial = []
    clear_console()
    while True:
        display_menu()
        choice = input('Elige una opción: ')
        if choice == '1':
            suma(historial)
        elif choice == '2':
            subtraction(historial)
        elif choice == '3':
          multiply(historial)
        elif choice == '4':
            split(historial)
        elif choice == '5':
            operations(historial)   
        elif choice == '0':
            print('Fin de la aplicación, hasta luego')
            break
        else:
            print('Opción invalida, por favor hagalo de nuevo')


if __name__ == '__main__':
    main()
