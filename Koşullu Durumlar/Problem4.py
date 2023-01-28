"""
Üçgen belirtme şartı ; bir üçgenin iki kenar uzunluğunun toplamının daima üçüncü kenardan daha büyük olduğunu belirten Üçgen Eşitsizliği Teoremini kullanmaktır.

"""




sekil = input("Hangi şekli incelemek istersiniz ?")

if sekil == "Dörtgen" :
    print("Lütfen kenarları sırayla giriniz :")

    a = int(input("Birinci Kenar:"))
    b = int(input("İkinci Kenar:"))
    c = int(input("Üçüncü Kenar:"))
    d = int(input("Dördüncü Kenar:"))

    if a == b == c == d :
        print("Kare")

    elif c == d and a == b :
        print("Dikdörtgen")

    else :
        print("Dörtgen")


if sekil == "Üçgen" :
    print("Lütfen kenarları sırayla giriniz :")

    x = int(input("Birinci Kenar :"))
    y = int(input("İkinci Kenar :"))
    z = int(input("Üçüncü Kenar :"))

    if x == y == z :
        print("EŞKENAR ÜÇGEN")

    elif x == y :
        print("İKİZKENAR ÜÇGEN")

    elif x + y > z  and x + z > y and z + y > x :
        print("ÜÇGEN")

    else:
        print("Üçgen belirtmiyor")
