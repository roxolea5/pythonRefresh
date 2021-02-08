thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print("thisset mide ", len(thisset))

set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}

print(type(set4))

for x in thisset:
  print(x)

print("banana" in thisset)

thisset.add("orange")

print(thisset)

tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset.remove("banana") #si el elemento no existe, arrojara error

print(thisset)

thisset.discard("banana") #funcoiona como remove pero no arroja error

print(thisset)

x = thisset.pop()

print(x)

print(thisset)


thisset.clear()

print(thisset)

del thisset

print(thisset) #arroja not defined
