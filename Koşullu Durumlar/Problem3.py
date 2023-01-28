"""
Her bir vize ve final puanı, ortalamadaki ağırlığını gösteren oran ile çarpılır ve çarpımların sonucu toplanır.
 Bu toplamın 100'e bölünmesiyle de dersin ortalaması elde edilir. Üniversitenin kullandığı not sistemine göre bu puan,
harf notuna dönüştürülür ve öğrencinin transkriptine işlenir.
"""

print("""

Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF

""")

Vize1 = int(input("Vize1 Notunuz:"))
Vize2 = int(input("Vize2 Notunuz:"))
Vize3 = int(input("Vize3 Notunuz:"))


VizeOrt = (Vize1 * 30) + (Vize2 * 30) + (Vize3 * 40)

VizeYüzde = VizeOrt / 100

if VizeYüzde >= 90 :
    print("AA")

elif VizeYüzde >=  85:
    print("BA")

elif  VizeYüzde >=  80 :
    print("BB")

elif VizeYüzde >=  75 :
    print("CB")

elif VizeYüzde >=  70 :
    print("CC")

elif VizeYüzde >=  65 :
    print("CD")

elif VizeYüzde >=  60 :
    print("DD")

elif VizeYüzde >=  55 :
    print("DF")

elif VizeYüzde <  55 :
    print("FF")
