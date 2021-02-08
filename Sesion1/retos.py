# Reto 1
print("Ingresa el primer número")
reto1_str1 = input()
reto1_num1 = int(reto1_str1)
print("Ingresa el segundo número")
reto1_str2 = input()
reto1_num2 = int(reto1_str2)

print ("El resultado de la concatenación de {} y {} es {}".format(reto1_str1, reto1_str2, reto1_str1 + reto1_str2))
print ("El resultado de la concatenación de {} y {} es {}".format(reto1_num1, reto1_num2, reto1_num1 + reto1_num2))

# Reto 2
print("Ingresa el primer número")
reto2_num1 = int(input())
print("Ingresa el segundo número")
reto2_num2 = int(input())

print ("El resultado de la resta de {} y {} es {}".format(reto2_num1, reto2_num2, reto2_num1 - reto2_num2))
print ("El resultado del módulo de {} y {} es {}".format(reto2_num1, reto2_num2, reto2_num1 % reto2_num2))

reto2_dato1  = True
reto2_dato2 = False
print("Operacion or de un true y un false ")
print(reto2_dato1 or reto2_dato2)

# Reto3
print("Dame un numero y te daré su tabla de multiplicar hasta 10")
reto3_num = int(input())
tabla = [1,2,3,4,5,6,7,8,9,10]

for num in tabla:
    print("{} * {} = {}".format(reto3_num, num, reto3_num * num))

# Reto4
print("Selecciona el topping que quieres en tu helado: \n 1. 'oreo' \n 2. 'm&m' \n 3. 'fresas' \n 4. 'brownie'")
reto4_sabor = int(input())

if reto4_sabor == 1:
    print ("El helado de oreo tiene un precio de $19.00")
elif reto4_sabor == 2:
    print ("El helado con m&m tiene un precio de $25.00")
elif reto4_sabor == 3:
    print ("El helado con fresas tiene un precio de $22.00")
elif reto4_sabor == 4:
    print ("El helado con brownie tiene un precio de $28.00")
else:
    print("Esa opción no está disponible")

# Reto 5

print("Ingresa el primer número")
num_1 = int(input())
print("Ingresa el segundo número")
num_2 = int(input())

print("Seleciona la operación a realizar")
print("1: Suma")
print("2: Resta")
print("3: Multiplicación")
print("4: División")
operation = input()

if operation == '1':
    op_name = 'suma'
    result = num_1 + num_2
elif operation == '2':
    op_name = 'resta'
    result = num_1 - num_2
elif operation == '3':
    op_name = 'multiplicación'
    result = num_1 * num_2
elif operation == '4':
    op_name = 'división'
    if num_2 == 0:
        print("Imposible división entre 0")
        result = "ERROR"
    else:
        result = num_1 / num_2
else:
    print("Opción inválida")
    op_name = 'operación indefinida'
    result = 'ERROR'

print("La {} de {} con {} es {}".format(op_name, num_1, num_2, result))
