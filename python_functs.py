sehirler=["ankara","istanbul","izmir"]

#append()fonksiyonu sona ekleme fonksiyonu

sehirler.append("bursa")
print(sehirler)

#insert() istedigimiz indise eleman ekleme ve sonrakiler kaydırılır

sehirler.insert(1,"antalya")
print(sehirler[3])

#extend() append gibidir fakat briden fazla eleman eklemek istedigimiz zaman kullanılır

sehirler.extend(["hatay","maraş"])
print(sehirler)

#remove() diziden eleman silmeye yarar
sehirler.remove("istanbul")
print(sehirler)

#pop() ici bossa dizinin sonundan eleman cikarmaya yarar -->> pop(1,2..) icine yazdıgımız indise ait degeri kaldırır

cikartilan_sehir=sehirler.pop()
print("listeden cikarilan sehir: ", cikartilan_sehir)
print("listenin yeni hali:", sehirler)

#index() belirtilen elemanın indeksini döndurur
if "hatay" in sehirler:

    indeks=sehirler.index("hatay") 
    print(indeks)

else:
    print("aranan sehir listede bulunmamaktadir.")

#count() listede istenen elemanın kaç tane oldugunu dondurur

adet=sehirler.count("hatay")
print(adet) 

#sort() liste elemanları artan veya kucukten buyuge göre sıralanır.A-Z'ye mesela

sehirler.sort()
print(sehirler)

#reverse()liste elemanları tersten siralanir.Z-A'ya 
sehirler.reverse()
print(sehirler)

#clear() tüm elemanlari siler

sehirler.clear()
print(len(sehirler))
