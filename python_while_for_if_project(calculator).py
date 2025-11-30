#### while loop:
num=0
while num<10:
    num+=1
    print(num)

### using while to sum 1-10:
sum=0
num=0
while num<10:
    sum+=num
    num+=1

print("result of sum: ", sum)

### using for to sum 1-10:
toplam=0
for x in range(1,10):
    toplam+=x
print("result: ", toplam)

### examples for while:
while True:
     num=int(input("insert a number(insert -1 to exit program): "))
     if num==-1:
         print("good bye...")
         break
     num=num**2
     print("square of number: ",num)
     

### project for while(calculator):
while True:
    print("\n-----Menu-----")
    x=int(input("""
      1.Toplama
      2.Cikarma
      3.Carpma
      4.Bolme
      5.Exit
     islemlerden birini secin:"""))
  

    if x==1:
        print("\nToplamak istediginiz sayilari girin: ")
        num1=int(input("birinci sayi: "))
        num2=int(input("ikinci sayi:"))
        result=num1+num2
        print("Toplama sonucu: ", result)
        continue
    elif x==2:
        print("\nCikarma islemi istediginiz sayilari girin: ")
        num1=int(input("birinci sayi: "))
        num2=int(input("ikinci sayi:"))
        result=num1-num2
        print("Cikarma sonucu: ", result)
        continue

    elif x==3:
        print("\nCarpma istediginiz sayilari girin: ")
        num1=int(input("birinci sayi: "))
        num2=int(input("ikinci sayi:"))
        result=num1*num2
        print("Carpma sonucu: ", result)
        continue

    elif x==4:
        print("\nBolme istediginiz sayilari girin: ")
        num1=int(input("birinci sayi: "))
        num2=int(input("ikinci sayi:"))
    
        if num2==0:
            print("payda 0 olamaz")
           
        else:
            result=num1/num2
            print("Bolme sonucu: ", result)
            continue

    elif x==5:
        print("hoscakaliin...")
        break
        