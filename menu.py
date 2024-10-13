from mostrar import display_menu
from puntos import suma, subtraction, multiply, split, operations

def menu():
    while True:
        display_menu()
        choice = input('Elige una opción: ')
        if choice == '1':
            suma()
        elif choice == '2':
            subtraction()
        elif choice == '3':
          multiply()
        elif choice == '4':
            split()
        elif choice == '5':
            operations() 
        elif choice == '0':
            print('Fin de la aplicación, hasta luego')
            break
        else:
            print('Opción invalida, por favor hagalo de nuevo')