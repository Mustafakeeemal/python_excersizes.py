#nested data structers:

kitaplar=[                  # list data structers
    
    ("Şeker Portakalı",180), # tuple data structers
    ("Simyacı", 184),
    ("1984", 352),
    ("Hayvan Ciftliği", 152)
]
## output: all list

for kitap in kitaplar:
    print(kitap)
    
## sum of pages:
toplam=0
for kitap_adi,sayfa_sayisi in kitaplar:
    toplam+=sayfa_sayisi

print("toplam sayfa sayisi: ", toplam)