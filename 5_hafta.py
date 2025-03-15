# Lambda ile fonksiyon yazımı ve kullanımı

# Söz dizimi:
# lambda argümanlar:ifade

# lambda = anahtar kelimedir ve kesinlikle kullanılmalıdır
# tıpkı normal fonksiyon yazarken def anahtar kelimesinin kullanılması gibi
# argümanlar = fonksiyonun parametreleri olarak düşünülebilir
# sadece isimleri yazılır (argümanlar kısmında)
# ifade = return yapılan işlem ya da işlem türüdür
# Normal fonksiyon tanımlayarak bir sayının karesini hesaplama

def fonk_kare(x):
    return x**2

print(f"5 sayısının karesi = {fonk_kare(5)}")

# Lambda ile bir sayının karesini hesaplama

# Genellikle şöyle kullanılır

# fonksiyon_adı = lambda argümanlar:işlem

kare_lm = lambda v:v**2

print(f"5 sayısının karesi = {kare_lm(5)}")
# İki veya daha fazla parametre ile lambda'nın kullanımı

# Örnek: 2 sayının toplamını lambda ile yazma

toplam = lambda x,y:x+y
print(f"8 ve 13 sayılarının toplamı = {toplam(8,13)}")
# İki veya daha fazla parametre ile lambda'nın kullanımı

# Örnek: 2 sayının toplamını lambda ile yazma

toplam = lambda x,y:x+y
print(f"8 ve 13 sayılarının toplamı = {toplam(8,13)}")
# Girilen bir metindeki toplam karakter sayısını döndüren
# kod-lambda ile

kelime_sayisi = lambda x:len(x)

print(f"Toplam Karakter sayısı = {kelime_sayisi('Furkan ATLAN')}")
# Girilen bir metindeki toplam kelime sayısını döndüren
# kod-lambda ile

kelime_sayisi = lambda x:len(x.split())
print(f"Kelime Sayısı = {kelime_sayisi('Furkan ATLAN')}")
# Girilen bir str ifadeyi tersten yazdıran lambda kodu

tersten = lambda x:x[::-1]
print(f"Furkan kelimesinin tersten yazılışı = {tersten('Furkan')}")

# Girilen bir str ifade içerisindeki sesli harfleri
# kendisinden önce veya sonraki sessiz harf ile değiştiren
# lambda kodu
# örneğin a harfi girildiğinde b  ya da z harfini yazacak
# Önce cümlenin tüm kelimelerini küçük harfe dönüştürecek sonra değiştirecek

harf_degistirme = lambda cumle:cumle.lower().replace('a','b').replace('e','d').replace('ı','h').replace('i','j').replace('o','n').replace('ö','r').replace('u','t').replace('ü','v')

print(harf_degistirme("Furkan ATLAN Yönetim Bilişim Sistemleri Bucak Zeliha Tolunay"))
# If-Else Kullanımıyla lambda örnekleri
# İki veya daha fazla şartın olması durumunda lambda söz dizimi:

# İki Durum için lambda söz dizimi: aşağıdaki örnekte x rastgele bir değişkendir

# fonksiyon_adı = lambda x: "True ise" if x>100 else "False ise"

# 3 durum için lambda söz dizimi: aşağıdaki örnekte x rastgele bir değişkendir
# fonksiyon_adı = lambda x: "True" if x>100 else("2. True" if x<50 else "False")
# Girilen sayı tek ise "TEK" yazan, değilse "ÇİFT" yazan lambda kodu

tek_cift = lambda y:"TEK" if y%2!=0 else "ÇİFT"
print(f"56 sayısı {tek_cift(56)} sayıdır")
print(f"573 sayısı {tek_cift(573)} sayıdır")
# Girilen 3 sayıdan en büyüğünü döndüren lambda kodu

buyuk_kucuk = lambda x,y,z:x if x>y and x>z else(y if y>z else z)

print(buyuk_kucuk(7,6,5))
print(buyuk_kucuk(7,61,5))
print(buyuk_kucuk(7,6,555))
def yeni_buyuk_kucuk(x,y,z):
    if x>y and x>z:
        return x
    else:
        if y>z:
            return y
        else:
            return z
# Girilen not değeri:
# 91 ile 100 arasındaysa AA
# 81 ile 90 arasındaysa BA
# 71 ile 80 arasındaysa BB
# 61 ile 70 arasındaysa CB
# bunlardan hiçbiri değilse FF yazdıran lambda kodu

harf_notu = lambda deger:"AA" if 91<=deger<=100 else("BA" if 81<=deger<=90 else("BB" if 71<=deger<=80 else("CB" if 61<=deger<=70 else "FF")))

print(f"92 notunun harf notu = {harf_notu(92)}")
print(f"82 notunun harf notu = {harf_notu(82)}")
print(f"72 notunun harf notu = {harf_notu(72)}")
print(f"62 notunun harf notu = {harf_notu(62)}")
print(f"60 notunun harf notu = {harf_notu(60)}")