print("***************$ List manipulation $*****************")

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 3rd
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists


myList = ["The", "earth", "revolves", "around", "sun"]
print(myList[-1]) # Shows 'sun'

myList.append(".");
print(myList)

myList.remove(".")
print(myList)

myList.reverse();
print(myList)

print(len(myList))

print(myList.index("revolves"))

isSunInList = "sun" in myList
print(isSunInList)

myList = myList + ["sure"]
print(myList)

myList.pop()
print(myList)
