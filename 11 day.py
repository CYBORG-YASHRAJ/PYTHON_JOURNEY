'''if-else statements'''

a=int(input("enter your age:"))
print("your age is:",a)

#conditional operators
#>,<,=,>=,<=,==
#answer wil be in the form of True/False
print(a>18) # a is greater than equals to 18
print(a<=18) #a less than equals to 18
print(a==18) #a is exactly equals to 18
print(a!=18) #a not equals to 18

if a>18:
    print("you can drive")
    print("you are eligible to drive")
else:
    print("you cannot drive")
    print("you are underage")
print("YAY")

# if-else 
applePrice=210
budget=200
if (budget-applePrice>50):
    print("alexa,add 1kg apples to the cart")
else:
    print("alexa,you don't have enough money")
    
#if-elif-else
num=int(input("enter the value of number:"))
if (num<0):
    print("number is negative")
elif (num==0):
    print("number is zero")
elif (num==999):
    print("number is special")
else:
    print("number is positive")
print("i am happy now")

#nested if statements
num=18
if (num<0):
    print("number is negative")
elif (num>0):
    if (num<=10):
        print("number is between 1 to 10")
    elif (num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")
        




    