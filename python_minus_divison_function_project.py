def divide():                               ### define a function for divison operation
    x=float(input("insert a number1: "))    ### to get value from users and make them float
    y=float(input("insert a number2: "))
    if y==0:                                ### error controlling
       print("number2 must be different than 0\n") 
    else: 
        print("x/y = ", x/y) 


def minus():                                ### define a function for minus operation
    a=float(input("insert a number1: "))    ### to get value from users
    b=float(input("insert a number2: "))

    print("x-y = ", a-b)

print("division: \n")                       
divide()                                    ## call functions
print("minus: \n")
minus()                                      ## call functions