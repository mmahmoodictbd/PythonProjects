print("***************$ Tuples(readonly list) manipulation $*****************")

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # print(s complete list
print(tuple[0])  # print(s first element of the list
print(tuple[1:3])  # print(s elements starting from 2nd till 3rd
print(tuple[2:])  # print(s elements starting from 3rd element
print(tinytuple * 2)  # print(s list two times
print(tuple + tinytuple)  # print(s concatenated lists



tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list