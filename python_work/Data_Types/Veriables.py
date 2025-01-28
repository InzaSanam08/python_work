#        String[str] : Integar[int]:- Practice 

name = 'Ali'
age = 15
print(name,age)
print(f'{name,age}')

studentDetail: str = 'Student of midle school'
print(studentDetail[0])
# veriable type
print(type(studentDetail))
# length of studentDetail 
print(len(studentDetail))

#         Float

x = 2.0
print(x)


#        Booleans[bool]

isStudentPresent = True

print(isStudentPresent)


#       list

fruits = [5.2,1,2,3,'Apple','Banana',True,False]

#  printing list elements
print(fruits)
# list type
print(type(fruits))
# list length
print(len(fruits))

#       Access List of Elements by index 
print(fruits[0])
print(fruits[0:2])
print(fruits[:2])
print(fruits[1:])
print(fruits[5:-1])

# list Methods

#  Adding elements in list
fruits.append ('Kiwi')
print(fruits)

# Adding elements on specifice index
fruits.insert(8, True )
print(fruits)

#    remove elements from list
fruits.remove(1)
print(fruits)

#  remove specific indxe

fruits.pop(5)
print(fruits)
del fruits[7]
print(fruits)

fruits.clear()
print(fruits)



#        dictionery[=dict]

schoolDetail:[dict] = {'class':{

}}



