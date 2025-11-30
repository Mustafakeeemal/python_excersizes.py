# Dictionary (Sözlük) Veri yapısı: mutable
# key : must be an unique
# value: value of the key
# 100(ID)= Ali Kaya(value)
# 101(ID)=Mehmet Aksu (value)
# 102(ID)= Ali Kaya (value) = There are a lot of person as 'ali kaya' but shouldn't be same ID

ogrenciler_dict={100:"ali kaya", 101:"zeynep tas"}

print(ogrenciler_dict[100]) ## output: ali kaya

deger=ogrenciler_dict.get(102) ## output: none , type= NoneType(class)

if deger is None:
    print("can't be founded")
else:
    print("founded") 

print(list(ogrenciler_dict.keys()))## output: [101,102]
print(list(ogrenciler_dict.values())) ## output: ['ali kaya', 'zeynep tas']

ogrenciler_dict[105]="kaan caliskan" ## output: add a new value and key
print(ogrenciler_dict)

ogrenciler_dict.pop(101) ## output: popping key and value
print(ogrenciler_dict)

del ogrenciler_dict[105]  ## output: same with popping
print(ogrenciler_dict)