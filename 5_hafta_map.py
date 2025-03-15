# map fonksiyonu:
# map fonksiyonu, bir lambda fonksiyonunun ya da başka bir fonksiyonun
# iterable (yani itere edilebilir yani birden fazla elemanlı bir veri yapısına)
# uygulanmasını sağlar.
# Girilen sayının karesini alan lambda kodu

kare = lambda x:x**2
print(f"6 sayısının karesi = {kare(6)}")
# Girilen bir listedeki tüm elemanların karesini alan lambda kodu
# map fonksiyonu ile, lambda kodunun tek bir değere uygulanmasını tüm listeye/veri yapısına
# uygulanmasına dönüştürebilirim

# map fonksiyonu mutlaka ama mutlaka bir veri yapısına dönüştürülerek kullanılmalıdır
# yani örneğin; list(map()) gibi
# map'in içinde tanımlanan kod en sonunda bir listeye dönüştürülüyor

#map'in formülü: x herhangi bir değişken ve * işareti örnek bir çarpma işlemi

# sonuç_listesi_adı = list(map(lambda x:x*işlem, parametre_verilen_liste))
# Örnek, bir listedeki tüm elemanların karesini alan map-lambda kodu

my_list = [x for x in range(1,11)]

my_list_kare = list(map(lambda x:x**2,my_list))
print(my_list_kare)
# str tipindeki değerleri barındıran bir listenin
# tüm değerlerini büyük harfle yazdıran map kodu

my_list = ["Burdur Mehmet Akif Ersoy Üniversitesi Bucak Ztyo"]

my_list_buyuk_yazma = list(map(lambda deger:deger.upper().replace('I','İ'),my_list))

print(f"Orijinal Liste = {my_list}")
print("-"*50)
print(f"İşlenmiş Liste = {my_list_buyuk_yazma}")
# Girilen aynı uzunluktaki iki listeyi toplayan map kodu
# NOT: her bir listeyi tek bir eleman gibi düşünün

list_toplam_1 = [x for x in range(1,11)] # 1'den 10'a kadar olan sayılar
list_toplam_2 = [x for x in range(11,21)] # 11'den 20'ye kadar olan sayılar

my_map_toplam = list(map(lambda x,y:x+y,list_toplam_1,list_toplam_2))

print(f"Toplanacak Liste-1 = {list_toplam_1}")
print(f"Toplanacak Liste-2 = {list_toplam_2}")
print("-"*50)
print(f"İki listedeki aynı indeksteki elemanların toplamı = {my_map_toplam}")
# Bir listedeki tek sayıların karesini alan, çift sayıların
# -3 katının 11 fazlasını alan map kodu

my_list_1 = [x for x in range(1,11)] # 1'den 10'a kadar olan sayılar (lambda'nın uygulanacağı liste)

mat_islem = list(map(lambda y:y**2 if y%2!=0 else (y*-3)+11,my_list_1))

print(f"Orijinal Liste = {my_list_1}")
print("-"*50)
print(f"İşlenmiş Liste = {mat_islem}")
# Dictionary veri tipiyle map-lambda kullanımıi
# Örnek: ürünlerin fiyat bilgisinin kdv oranıyla toplanması
# NOT-1: dictionary veri yapısında :'nın öncesinde "key", sonrasında "value" bulunur
# NOT-2: dictionary.items() fonksiyonu ('Key':Value) şeklinde her bir eleman çiftini döndürür
# NOT-3: bir fonksiyonun kısa yazılmasında dictionary kullanılırken 
# dictionary'ye ait key bilgisi dict[0] ile
# dictionary'ye ait value bilgisi dict[1] ile temsil edilir/erişilir.

dict_products = {"kalem":150,"silgi":40,"kitap":430,"uç":25}

kdv_products = dict(map(lambda deger:(deger[0],deger[1]*1.10),dict_products.items()))

print(f"Orijinal ürün ve fiyatları = {dict_products.items()}")
print(f"-"*50)
print(f"KDV'si hesaplanmış hali = {kdv_products}")
# 4 kişi adı ve bunların yaşını bir dictionary olarak tanımlayın
# yazacağınız map kodu ile bu kişilerin yaşı 18'den küçük ise 'ÇOCUK' yazsın
# değilse 'YETİŞKİN' yazsın

my_dict_people = {"ahmet":19,"leyla":27,"yusuf":12,"mehmet":17,"hakan":52}

#1. Hesaplama (dictionary.items() ile dönen 2 değer üzerinden hesaplama)

yas_hesaplama_1 = dict(map(lambda deger: (deger[0],"YETİŞKİN" if deger[1]>18 else "ÇOCUK"),my_dict_people.items()))

print(f"1. HESAPLAMA ile ÇOCUK-YETİŞKİN AYRIMI = {yas_hesaplama_1}")

# dictionary.values() üzerinden sadece yaş değerlerini tutarak (yani tek bir değişken kullanarak)

#yas_hesaplama_2 = dict(map(lambda x: "YETİŞKİN" if x>18 else "ÇOCUK"),my_dict_people.values()))
yas_hesaplama_2 = list(map(lambda x: "YETİŞKİN" if x>18 else "ÇOCUK",my_dict_people.values()))
print("-"*50)
print(f"2. HESAPLAMA ile ÇOCUK-YETİŞKİN AYRIMI = {yas_hesaplama_2}")
my_dict_people.values()
# Map aşağıdaki gibi çalışır

sonuc = lambda x:x**2

my_list = [1,2,3,4,5,6,7,8,9,10]

bos_list = []

for i in my_list:
    bos_list.append(sonuc(i))

print(bos_list)
