""" fibonacci dizisini veren python kodunu yazınız
"""

def fibonacci():
    n = int(input("bir sayi girin (2'den buyuk olmalı): "))
    if n <= 2:
        print("2'den buyuk bir sayi giriniz ")
        return
    
    fib_seri=[]
    a=0
    b=1

    while a<=n:
        fib_seri.append(a)

        temp=a+b
        a=b
        b=temp

    print("fibonacci : " , fib_seri)
    
fibonacci()
