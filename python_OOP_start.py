### python OOP startiing



class Tesla:        ## creating class and name Tesla

    colour = "white"                ## those properties are default 
    battery = "long distance"
    rim = 20
    autopilot = False

my_tesla = Tesla()   ## Creating object for class, first object

print(my_tesla.colour,my_tesla.autopilot,my_tesla.battery,my_tesla.rim)

my_tesla.autopilot = True ## you can change your properties

print(my_tesla.autopilot) ## outputs: true

fathers_tesla = Tesla()  ## second object

fathers_tesla.colour="Black"  
fathers_tesla.rim = 21
print(fathers_tesla.colour,fathers_tesla.battery,fathers_tesla.rim,fathers_tesla.autopilot)