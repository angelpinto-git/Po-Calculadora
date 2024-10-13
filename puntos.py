from mostrar import clear_console
from numero import number
from file import write_messages, read_messages

def suma():
    clear_console()
    num1 = number(1)
    num2 = number(2)
    sum = num1 + num2
    print(f'La suma de {num1} + {num2} es = "{sum}".')
    histo = (f'La suma de {num1} + {num2} es = "{sum}".')
    write_messages(histo)
   
def subtraction():
    clear_console()
    num1 = number(1)
    num2 = number(2)
    res = num1 - num2
    print(f'La resta de {num1} - {num2} es = "{res}".')
    histo = (f'La resta de {num1} - {num2} es = "{res}".')
    write_messages(histo)
    
def multiply():
    clear_console()
    num1 = number(1)
    num2 = number(2)
    multi = num1 * num2
    print(f'La multiplicación de {num1} * {num2} es = "{multi}".')
    histo = (f'La multiplicación de {num1} * {num2} es = "{multi}".')
    write_messages(histo)
    
def split():
    clear_console()
    num1 = number(1)
    num2 = number(2)
    try:
        divide = num1 / num2            
    except ZeroDivisionError:
        print('Error no se puede calcular la división con el denominador 0')
        return 0.0
        #raise Exception('Tiene que ser distinto de cero')
    print(f'La división de {num1} / {num2} es = "{divide}".')
    histo = (f'La división de {num1} / {num2} es = "{divide}".')
    write_messages(histo)


def operations():
    clear_console()
    #if not historial:
    #    print('No hay historial disponible, elija otra opción.')
    #    return
    read_messages()
    


      
        
