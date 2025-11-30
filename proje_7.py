"""
Aşağıdaki adımları izleyerek bir Python programı yazınız:

I. Adım) 1 ile 35 arasında (1 ve 35 dahil) rastgele üretilen tam sayılardan oluşan bir liste oluşturun. 
Bu liste, 1 haftanın (7 günün) her bir günü için ölçülen ortalama sıcaklık değerlerini temsil etsin.

II. Adım) Bu listeyi ekrana yazdırın.

III. Adım) Bu 7 günün (yani haftanın) ortalama sıcaklığını hesaplayıp ekrana yazdırın.
"""

import random

# 1 ile 35 arasında 7 adet tam sayıdan oluşan listeyi üret
sicaklik_degerleri = []   # 3 boş bir liste oluşturuyoruz
for i in range(7):
    rastgele_sicaklik = random.randint(1, 35)
    sicaklik_degerleri.append(rastgele_sicaklik)

# Bu listeyi ekrana yazdıralım
print("Haftanın ortalama sıcaklık değerleri:", sicaklik_degerleri)

#  Bu 7 günün (yani haftanın) ortalama sıcaklığını hesaplayalım
# ortalama_sicaklik = sum(sicaklik_degerleri) / len(sicaklik_degerleri)
sicaklik_toplam = 0
for deger in sicaklik_degerleri:
    sicaklik_toplam += deger

ortalama_sicaklik = sicaklik_toplam / len(sicaklik_degerleri)

print("Haftanın ortalama sicaklığı:", round(ortalama_sicaklik, 2))












