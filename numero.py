
def number(n):
    try:
        num = float (input(f'ingrese número {n}: '))
        return num
    except ValueError as error:
        print('Valor erroneo', error)
        return number(n)
    #finally:
    #   print('bloque finally')
    
    