'''Match Case Statement'''

# case statement will run from begining until it gets match,in python statement which are not matched will not run
#if x matches the case statement it will not run further
x=4

match x:
    case 0:
        print("x is zero")
    case 4 :
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 90")
    case _:
        print(x)
      