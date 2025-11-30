# # # #                        PYTHON PROJE #4                       # # # #
"""
isimler = ["Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar  = [145, 178, 164, 175, 185, 180, 134]

Yukarda verilen 2 liste sıralı olarak öğrenci isimleri ve bu öğrencilerin okul 
numaralarını içermektedir. Örneğin Ali'nin numarası 145, Ece'nin ise 178.

a. yukarda verilen öğrenci numaraları içindeki en yüksek olanı ve bunun sahibi olan
   öğrencinin adını bulunuz ekrana yazdıran pyhton kodunu yazınız

b. yukarda verilen öğrenci numaraları içindeki en düşük olanı ve bunun sahibi olan 
   öğrencinin adını bulunuz ekrana yazdıran pyhton kodunu yazınız
"""
isimler = ["Ali", "Ece", "Kaan", "Mete", "Batu", "Veli", "Ayşe"]
numaralar  = [145, 178, 164, 175, 185, 180, 134]

# En yüksek numarayı ve öğrenciyi bulma
max_numara = max(numaralar)  # 185
max_index = numaralar.index(max_numara)   # 4
max_ogrenci = isimler[max_index]  # Batu
print("En yüksek no: ", max_numara, " Öğrenci: ", max_ogrenci)

min_numara = min(numaralar)  # 134
min_index = numaralar.index(min_numara)   # 6
min_ogrenci = isimler[min_index]  # Ayşe
print("En düşük no: ", min_numara, " Öğrenci: ", min_ogrenci)

