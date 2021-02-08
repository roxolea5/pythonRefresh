my_list = [1, 2.5, 'Coding', [5,6] ,4]

print (my_list[0]) # 1
print (my_list[1]) # 2.5
print (my_list[2]) # Coding
print (my_list[3]) # [5,6]
print (my_list[3][0]) # 5
print (my_list[3][1]) # 6
print (my_list[1:3]) # [2.5, 'Coding']
print (my_list[1:6]) # [2.5, 'Coding', [5, 6], 4]
print (my_list[1:6:2]) # [2.5, [5, 6]]
print("********************")

for element in my_list:
    print(element)
print("********************")


my_list.append(10)
for element in my_list:
    print(element)
print("********************")

my_list.append([8,9])
for element in my_list:
    print(element)
print("********************")

my_list.extend([8,9])
for element in my_list:
    print(element)
print("********************")

my_list.remove([8,9])
for element in my_list:
    print(element)
print("********************")

print(my_list.index('Coding'))
print("********************")

my_list.extend([2,2,2])
print(my_list.count(2))
print("********************")

my_list.reverse()
for elem in my_list:
    print(elem)





