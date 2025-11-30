isimler= ["Ali","Ece","Kaan","Mete","Batu","Veli","Ayşe"]
numaralar = [145,178,164,175,185,180,134]
### en yuksek ogrenci no yu bul ve sahibinin ismini yazdır

max_no=0
max_ogrenci=""

for i in range(len(numaralar)): #range kullandigimiz zaman i degiskenimiz listeye erismek adına indis tutar
    if numaralar[i]>max_no:
        max_no= numaralar[i]
        max_ogrenci=isimler[i]

print("en dusuk numara ve sahibi olan ogrenci: \n", max_no,max_ogrenci)


### en dusuk ogrenci no yu bul ve sahibinin ismini yazdir

min_no=1000
min_ogrenci = ""

for i in range(len(numaralar)):
    if numaralar[i]<min_no:
        min_no=numaralar[i]
        min_ogrenci=isimler[i]

print("en dusuk numara ve sahibi olan ogrenci: \n",min_no,min_ogrenci)