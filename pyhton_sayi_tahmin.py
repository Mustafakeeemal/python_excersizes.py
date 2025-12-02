"""
Sayı Tahmin Oyunu - Python Projesi

Bu projede, Python kullanarak bir "Sayı Tahmin Oyunu" yapmanız beklenmektedir. 
Program rastgele bir sayı seçecek ve oyuncu bu sayıyı tahmin etmeye çalışacaktır.
Oyuncunun 7 tahmin hakkı olacak ve her tahminde kaç hakkı kaldığı ekrana yazdırılacaktır.

Kurallar ve Gereksinimler
-   Rastgele Sayı Üretimi: Program, 1 ile 100 arasında rastgele bir sayı seçmelidir.
-   Tahmin Girişi: Kullanıcıdan bir tahmin almalıdır.
-   Hata Kontrolü: Kullanıcının sadece sayı girdiğinden emin olunmalıdır (ipucu isdigit() kullanılabilir).

-   Geri Bildirim: Kullanıcının tahmini:
        Doğruysa: kelimeler = ["karpuz", "elma", "kardan adam", "kayak" , "kar yağışı","güneşli hava"]
print(kar_filtrele(kelimeler)) mesajı gösterilmelidir.
        Küçükse: "Daha büyük bir sayı girin." mesajı gösterilmelidir.
        Büyükse: "Daha küçük bir sayı girin." mesajı gösterilmelidir.

-   Tahmin Hakkı: Her yanlış tahminde kalan tahmin hakkı azaltılmalıdır.
-   Hakkı Biten Oyuncu: Oyuncu sayıyı bilemezse, "Bilemediniz! Doğru sayı ... idi." mesajı gösterilmelidir.
-   Tekrar Oynama Seçeneği: Oyun sonunda oyuncuya tekrar oynamak isteyip istemediği sorulmalıdır.
        "E" derse oyun tekrar başlamalıdır.
        "H" derse oyun sonlandırılmalıdır.

Örnek Çıktı:
- - - - - - -
1 ile 100 arasında bir sayı tahmin edin. 7 hakkınız var!
Kalan hakkınız: 7 - Tahmininiz: 50
Daha büyük bir sayı girin.
Kalan hakkınız: 6 - Tahmininiz: 75
Daha küçük bir sayı girin.
Kalan hakkınız: 5 - Tahmininiz: 65
Daha büyük bir sayı girin.
Kalan hakkınız: 4 - Tahmininiz: 69
Tebrikler! Doğru tahmin ettiniz! 
Tekrar oynamak ister misiniz? (E/H): 
"""
import random

def sayi_tahmin_oyunu():
    while True:
        rastgele_sayi = random.randint(1,100)
        hak = 7

        print("\n1 ile 100 arasında bir sayi tahmin edin, 7 hakkiniz var! ")
    
        while hak > 0 :
            tahmin = input(f"Kalan hakkiniz: {hak} - Tahmininiz: " )

            if tahmin.isdigit():
                tahmin = int(tahmin)    

                if tahmin == rastgele_sayi:
                    print("Tebrikler,dogru tahmin!!!")
                    break
                elif tahmin < rastgele_sayi:
                    print("Daha buyuk bir sayi girin.")

                else:
                    print("Daha kucuk bir sayi girin. ")

                hak -= 1

            else:
                print("lutfen gecerli bir sayi girin!")
        if tahmin != rastgele_sayi:
            print(f"Bilemedin! Dogru sayi {rastgele_sayi} idi ")
        
        tekrar = input("Tekrar oynamak ister misiniz?(E/H): ").strip().lower()
        if tekrar != "e":
            print("Oyunu oynadiginiz iicin tesekkurler! ")
            break
        
sayi_tahmin_oyunu()