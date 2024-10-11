import os


def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    # ? clear_console()
    print('\n--- CALCULADORA ---')
    print('1. SUMA')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. Dividir')
    print('5. Historial')
    print('0. SALIR')


    

def suma(historial):
    clear_console()
    num1 = int (input('ingrese número 1: '))
    num2 = int(input('ingrese número 2: '))
    sum = num1 + num2
    print(f'La suma de {num1} + {num2} es = "{sum}".')
    histo = (f'La suma de {num1} + {num2} es = "{sum}".')
    historial.append(histo)
   

def subtraction(historial):
    clear_console()
    num1 = int (input('ingrese número 1: '))
    num2 = int(input('ingrese número 2: '))
    res = num1 - num2
    print(f'La resta de {num1} - {num2} es = "{res}".')
    histo = (f'La resta de {num1} - {num2} es = "{res}".')
    historial.append(histo)
    
    
def multiply(historial):
    clear_console()
    num1 = int (input('ingrese número 1: '))
    num2 = int(input('ingrese número 2: '))
    multi = num1 * num2
    print(f'La multiplicación de {num1} * {num2} es = "{multi}".')
    histo = (f'La multiplicación de {num1} * {num2} es = "{multi}".')
    historial.append(histo)
    

def split(historial):
    clear_console()
    num1 = int (input('ingrese número 1: '))
    num2 = int(input('ingrese número 2: '))
    divide = num1 / num2
    print(f'La división de {num1} / {num2} es = "{divide}".')
    histo = (f'La división de {num1} / {num2} es = "{divide}".')
    historial.append(histo)
    


def operaciones(historial):
    clear_console()
    if not historial:
        print('No hay historial disponible, elija otra opción.')
        return

    for i in historial:
        
        print(f'{i}')
        
   

    




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
            operaciones(historial)   
        elif choice == '0':
            print('Fin de la aplicación, hasta luego')
            break
        else:
            print('Opción invalida, por favor hagalo de nuevo')


if __name__ == '__main__':
    main()
