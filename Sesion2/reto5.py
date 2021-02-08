"""
Realiza una función que tome como entrada una lista de números, 
y devuelca una lista con los valores en orden y sin repetidos. 
Además la función debe imprimir los valores uno a uno.

"""
first_list = [8,10,21, 8,10,21,13,15,14,21,19]

print("Valor de la lista antes de ser ordenada", first_list)

def my_func(my_list):
    ord_list = my_list
    ord_list.sort()
    my_set = set(ord_list)
    print(my_set)
    new_list = list(my_set)
    for i in new_list:
        print(i)

my_func(first_list)