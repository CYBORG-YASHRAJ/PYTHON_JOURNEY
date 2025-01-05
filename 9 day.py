'''1) string methods in python'''
 
#strings are immutable
a="yashraj!!!"
print(len(a))

#these function works on the copy of the string

print(a.upper()) #convert  each character of string into uppercase
print(a.lower()) #convert  each character of string into lowercase
print(a.rstrip("!")) #remove ! from right side of the string
print(a.replace("yashraj","john")) # use to replace previous occurance with new occurance
print(a.split(" ")) #splits the string with wide space

blogheading="introduction to js"
print(blogheading.capitalize()) #capitalize the first letter of string

str="Welcome to the Console!!!"
print(len(str))
print(len(str.center(50)))
print(a.count("yashraj"))

print(str.endswith("!!!")) # check whether string ends with !!! gives true/false
