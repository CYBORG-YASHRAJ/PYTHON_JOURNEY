'''type casting in python'''

# coversion of one data into other data is called type casting
#example data type
# int()
# float()
# str()
# ord()
# hex()
# oct()
# tuple()
# set()
# list()
# dict()

'''examples'''

a="1"
c=1
b="2"
d=2
print(a+b)
print(int(a)+int(b)) #conversion of string into integer
print(c+d)

"""TWO TYPES OF TYPECASTING"""
#EXPLICIT CONVERSION
#CONVERSION DATA DONE BY DEVOLOPER / PROGRAMER

s="24"
u=str(9)
print(s+u)
print(int(s)+int(u))

#IMPLICIT CONVERSION
#in python data types is not same ,some of the data have higher order and some have lower order
#on performing operation in such cases,python convert data types to higher order data type. 

x=24.9
y=5
print(x+y) #data is converted to float