def operation(op, *args): 
    result = 0
    if op == '+':
        for num in args:
            result += num
    elif op == '*':
        result = 1
        for num in args:
            result *= num
    else:
        result = 'Operación no válida'

    return result

def promedio (*numeros):
    total = len(numeros)
    sumatoria = operation('+', *numeros)
    return sumatoria/total
