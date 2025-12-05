## class variables - instance variable

class employees:

    increasing_amount=1.1
    count_of_persons=0

    def __init__(self,name,salary):
        self.name= name
        self.salary = salary
        employees.count_of_persons +=1
    

employee1 = employees("ali",10000)

employee2 = employees("mehmet", 5000)

print(employees.count_of_persons) ## OUTPUT = 2

print(employee1.__dict__) ## output= {'name': 'ali', 'salary': 10000}

print(employees.increasing_amount) ## you can reach from class or from variables
print(employee1.increasing_amount)## output =1.1
print(employee2.increasing_amount) ## output = 1.1

employees.increasing_amount = 2 ## changes attracts just class 
employee1.increasing_amount = 1.1 ## changes employee1 properties

print(employee1.increasing_amount) ##output 1.1
print(employee2.increasing_amount) ## output 2

print(employee1.__dict__) ## there is an increasing amount info
print(employee2.__dict__) ## there is not an increasing amount info