from mostrar import clear_console


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
    


def operations(historial):
    clear_console()
    if not historial:
        print('No hay historial disponible, elija otra opción.')
        return

    for i in historial:
        
        print(f'{i}')
        
