from random import shuffle
from random import randint

### random deger üretme fonk randint(x,y)

print(randint(0,100))

### shuffle(list)=> verilen listenin öğelerinin sirasinin yerini değiştirir:
isimler=["ahmet","mehmet","ali","veli"]
print("liste karistirilmadan önce: ",isimler)

print("liste karistiriliyor...")

shuffle(isimler)
print("karistirildiktan sonra: ", isimler)





