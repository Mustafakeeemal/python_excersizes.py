
# list comprehension.1

kareler=[]
for x in range(1,11):
    print(x)
    kareler.append(x**2)
print(kareler)
###################################################
kareler=[x**2 for x in range(1,11)]
print(kareler)

#list comprehension.2

sayilar=[1,2,3,4,5,6,7,8,9,10]
cift_sayilar =[]

for i in sayilar:
    if i %2== 0:
        cift_sayilar.append(i)

print(cift_sayilar)

###################################################
ciftlerin_karesi=[i**2 for i in sayilar if i%2==0]
print(ciftlerin_karesi)

#list comprehension.3
kelimeler = ["python","java","c++","html"]
buyuk_harf=[]

for i in kelimeler:
    buyuk_harf.append(i.upper())

print(buyuk_harf)

###################################################

buyuk_harf = [i.upper() for i in kelimeler]
print(buyuk_harf)
