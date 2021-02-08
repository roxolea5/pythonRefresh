"""
Arithmetic
+ adittion
- substraction
* multiplication
/ division
% module
** exponentiation
// floor division
"""

a = 9
b = 3

add = a + b
substract = a - b
divide = a / b
multiply = a * b
module = a % b
exponent = a ** b

print(add)
print(substract)
print(divide)
print(multiply)
print(module)
print(exponent)

print(9//2) 
print(9.0//2.0) 
print(-11//3) 
print(-11.0//3.0) 
print("********************")

"""
Comparison operators
==
!=
<>
>
<
>=
<=
"""

print ( a == b)
print ( a != b)
#print ( a <> b) invalid syntax
print ( a > b)
print ( a < b)
print ( a >= b)
print ( a <= b)
print("*****************")

"""
Assignation
a = b 
a += b(a = a + b)
a -= b (a = a - b)
a *= b (a = a * b)
a /= b (a = a / b)
a %= b (a = a % b)
a **= b (a = a ** b)
a //= b (a // a - b)
"""

print (a, "+=", b, "is:")
a += b
print(a)
print (a, "-=", b, "is:")
a -= b
print(a)
print (a, "/=", b, "is:")
a /= b
print(a)
print (a, "*=", b, "is:")
a *= b
print(a)
print (a, "%=", b, "is:")
a %= b
print(a)
print (a, "**=", b, "is:")
a **= b
print(a)
print("*****************")
"""
Logical operators
and
or
not
"""

print(True and False)
print(True or False)
print(not(True and False))
print("*****************")




