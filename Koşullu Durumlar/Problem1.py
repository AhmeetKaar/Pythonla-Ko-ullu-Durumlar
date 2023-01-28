print("""

Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
c = int(input("Üçüncü Sayı:"))

if a > b and a > c :
    print(a)

elif b > a and b > c :
    print(b)

elif c > a and c > b :
    print(c)

else :
    print("TÜM SAYILAR EŞİT")
