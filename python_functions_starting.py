## Functions():
## def functions_names():  ##definition
    ## process blocks


def printfunctionS(name):   ### def a new functs, don't have to print data type
    print(type(name))       ### <str> python decide to data type at runtime
    print("hello",name)
    print("welcome...")
   
name=input("enter your name: ")     ## parameters

printfunctionS(name)            ### call a functs : we can call funct wherever we need.!



def sum(a,b):                                         
    print("sum: ",a+b)         ## def a new functs

a=int(input("insert a num: ")) ## input gives us str type, ıf we want to sum the values,
b=int(input("insert a num: ")) ## should be changed

sum(a,b) ##call functs