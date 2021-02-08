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

def sorted_dic(**kwdirectory):
    ordered = sorted(kwdirectory)
    for key in ordered:
        print(key, kwdirectory[key])

if __name__ == "__main__":
    suma = operation('+', 2,4,5,8,9)      
    multiplicacion = operation('*', 2,4,5,8,9)  
    error = operation('', 2,4,5,8,9)     

    print(suma)
    print(multiplicacion)
    print(error)

    my_directory = sorted_dic(Roxana='3322382238', Beatriz='3311472274', Sergio= '3318596824')