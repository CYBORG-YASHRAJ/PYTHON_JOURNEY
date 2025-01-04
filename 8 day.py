"""string slicing and operations in python"""

names="yashraj,piyush"
print(names[0:7])

#syntax of slicing (start,stop,step)
#slicing can also done from end of the string

'''len function-> gives length of the string or number of characters'''

print(len(names))

fruit="mango"
lenoffruit=len(fruit)
print(fruit)
print(lenoffruit)

print(fruit[0:4])  #slicing, including 0 but not 4
print(fruit[1:4])  #including 1 but not 4
print(fruit[:4])   #by default string starts from 0th position
print(fruit[2:4])

#negative indexing of string
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])

#Quick Quiz
nm="harry"
print(nm[-4:-2])
