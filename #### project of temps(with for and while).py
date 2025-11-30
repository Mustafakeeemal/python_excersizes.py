#### project of temps(with for and while loop):
import random

list_temps=[]
i=0
##create a list of random temps:
while i<7:
    random_temps=random.randint(1,35)
    list_temps.append(random_temps)
    i+=1

print("average of the temps on the week: " ,list_temps)
## calculate the average temp:
sum_temp=0
for i in list_temps:
    sum_temp+=i

print("average of the week: ", int(sum_temp/7))
