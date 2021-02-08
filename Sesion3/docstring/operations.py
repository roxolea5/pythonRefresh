"""Módulo de operaciones a realizar"""

def operation(op, *args): 
    """Devuelve el producto o la suma de una serie de números dado un signo"""
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
    """Devuelve el promedio de una serie de números"""
    total = len(numeros)
    sumatoria = operation('+', *numeros)
    return sumatoria/total
