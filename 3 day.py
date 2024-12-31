'''Variables and Data types'''

#variables are like container that holds data

a=1    #integer
print(a,type(a))
b="Yashraj"   #string
print(b,type(b))
c=True     #Boolean
print(c,type(c))
d=None     # nonetype
print(type(d))   # type() ,this func is used to get type of any variable

#we can't add string and integer
#print(a+b) #error


e=2.5     #float(decimal value)
print(e,type(e))

f=complex(8,2)    #complex number
print(f,type(f))

# Boolean data contains True or Fales/ 0 or 1

#list is colllection of different data
s=[1,2,3,["apple","banana"],"hello",[7,5]]
print(s,type(s))
'''lists are mutable(changeable)'''

#tuple are similar as list BUT
'''tuple are immutable(data is unchangeable)'''
t=(1,2,3,4,5,["apple",7,9],78)
print(t,type(t))

#dictionary is a mapped data
'''dictonaries are mutable'''
d={"a":2,"b":3}
print(d,type(d))
