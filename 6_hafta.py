# Lambda ile tek satırda fonksiyon yazmıştık

kare_al = lambda x:x**2
print(kare_al(8))
# Map fonksiyonu ile normalde labmda ile tek değere uygulanan
# fonksiyonları bir iterable nesneye (örneğin bir listeye)
# uygulamıştık

# aşağıda verilen listedeki tüm elemanların karesini almak
my_list = [x for x in range(1,11)]

print(list(map(kare_al,my_list)))
# Filter fonksiyonu: adından da anlaşılacağı üzere
# bir lambda ifadesini ya da normal bir şekilde tanımlanmış fonksiyonu
# iterable bir nesneye (örneğin bir listeye) uygular. Bu açıdan map fonksiyonuyla
# bire bir aynı işlevi görür. Ancak, çok önemli bir farkı vardır:
# filter fonksiyonu sadece True olan değerleri döndürür.
# Kendi içerisinde önce bir filtreleme yapar ve bu filtrelemenin sonucunda
# sadece True olan değerleri döndürür
# 0'dan 10'a kadar sayıları içeren bir listedeki sadece çift sayıları
# bir liste olarak döndüren fonksiyonu yazınız

my_list_1 = [x for x in range(0,11)]

def cift_sayilar(deneme:list):
    bos_list = []
    for eleman in deneme:
        if eleman%2==0:
            bos_list.append(eleman)
    return bos_list

sonuc = cift_sayilar(my_list_1)
print(sonuc)
# Map ile Filter arasındaki fark
# aynı kod map ile de yazılır (filter için yazılan kod) ve çalışır da.
# Ancak, map ile çalışan kodda değer değil True, False ifadeleri döner
# yani şartı sağlayan değerler True olarak görünür, sağlamayan değerler ise
# False olarak görünür
# Filter ise bunların direkt değerlerini döndürür (sadece True olanların
# değerini döndürür)
# Aşağıda map ve filter'in aynı görev ve aynı kodla kullanımına dair
# örnekle bu durum açıklanmaktadır

# Map ile listedeki sadece çift sayıları döndürme

my_list_1 = [x for x in range(0,11)]

cift_sayi_map = list(map(lambda x: x%2==0,my_list_1))

# Filter ile listedeki sadece çift sayıları döndürme

cift_sayi_filter = list(filter(lambda x: x%2==0,my_list_1))

print(f"map ile çift sayılar = {cift_sayi_map}")
print("-"*50)
print(f"filter ile çift sayılar = {cift_sayi_filter}")

# 20 farklı değer barındıran listedeki pozitif elemanları bulan kod
# 1) normal fonksiyon ile yazın (geriye liste döndürecek)
# 2) map ile yazın
# 3) filter ile yazın

my_list_2 = [x for x in range(-10,11)]

def pozitif_sayilar(deneme:list):
    bos_list = []
    for eleman in deneme:
        if eleman>=0:
            bos_list.append(eleman)
    return bos_list

sayilar_normal_fonk = pozitif_sayilar(my_list_2)
sayilar_map = list(map(lambda x:x>=0,my_list_2))
sayilar_filter = list(filter(lambda x:x>=0,my_list_2))

print(f"Sonuç (Normal fonksiyon ile) = {sayilar_normal_fonk}")
print("-"*50)
print(f"Sonuç (Map fonksiyonu ile) = {sayilar_map}")
print("-"*50)
print(f"Sonuç (Filter fonksiyonu ile) = {sayilar_filter}")
# 20 farklı değer barındıran listedeki pozitif-tek elemanları bulan kod
# 1) normal fonksiyon ile yazın (geriye liste döndürecek)
# 2) map ile yazın
# 3) filter ile yazın

my_list_2 = [x for x in range(-10,11)]

def pozitif_sayilar(deneme:list):
    bos_list = []
    for eleman in deneme:
        if eleman>=0 and eleman%2!=0:
            bos_list.append(eleman)
    return bos_list

sayilar_normal_fonk = pozitif_sayilar(my_list_2)
sayilar_map = list(map(lambda x:x>=0 and x%2!=0,my_list_2))
sayilar_filter = list(filter(lambda x:x>=0 and x%2!=0,my_list_2))

print(f"Sonuç (Normal fonksiyon ile) = {sayilar_normal_fonk}")
print("-"*50)
print(f"Sonuç (Map fonksiyonu ile) = {sayilar_map}")
print("-"*50)
print(f"Sonuç (Filter fonksiyonu ile) = {sayilar_filter}")
# İçi, str tipindeki değerlerle dolu olan bir listedeki
# kelime uzunluğu 7'den büyük olan kelimeleri bir liste olarak döndüren
# a) Normal fonksiyon
# b) map
# c) filter

my_list_3 = ["Burdur","Makü","Bucak ZTYO","Furkan","Yazılımcı","Orta Düzey Programlama"]

def eleman_uzunluk(deneme:list):
    bos_liste = []
    for eleman in deneme:
        if len(eleman)>7:
            bos_liste.append(eleman)
    return bos_liste

uzunluk_fonksiyon = eleman_uzunluk(my_list_3)
uzunluk_map = list(map(lambda x:len(x)>7,my_list_3))
uzunluk_filter = list(filter(lambda x:len(x)>7,my_list_3))

print(f"Sonuç (Normal fonksiyon ile) = {uzunluk_fonksiyon}")
print("-"*50)
print(f"Sonuç (Map fonksiyonu ile) = {uzunluk_map}")
print("-"*50)
print(f"Sonuç (Filter fonksiyonu ile) = {uzunluk_filter}")
#str liste içinde, "fr" ifadesi geçen değerleri yazdırma (3 yolla da yapın)

my_list_4 = ["fransa","Türkiye","İtalya","frankfurt","İsviçre"]

def gecen_ifade(deneme:list):
    bos_liste = []
    for kelime in deneme:
        if "fr" in kelime:
            bos_liste.append(kelime)
    return bos_liste

kelime_arama_fonk = gecen_ifade(my_list_4)
kelime_arama_map = list(map(lambda x: "fr" in x,my_list_4))
kelime_arama_filter = list(filter(lambda x: "fr" in x,my_list_4))

print(f"Sonuç (Normal fonksiyon ile) = {kelime_arama_fonk}")
print("-"*50)
print(f"Sonuç (Map fonksiyonu ile) = {kelime_arama_map}")
print("-"*50)
print(f"Sonuç (Filter fonksiyonu ile) = {kelime_arama_filter}")
# Reduce fonksiyonu
# parametre olarak aldığı listeyi daima 2 elemanla işleyen
# ve geriye YALNIZCA TEK BİR DEĞER (SONUÇ) DÖNDÜREN özel bir fonksiyondur
# Bu nedenle, geriye bir liste olarak dönmez, tek bir değer olarak döner
# tanımlanmadan önce import edilmelidir.
# yani python'un hazır modülleri içerisinden çıkarılmadılır
from functools import reduce
# Bir listedeki tüm elemanların toplamını döndüren reduce fonksiyonu
# 1'den 100'e kadar olan sayıların toplamı
# reduce, geriye tek değer döndürdüğü için parametre olarak iki parametre 
# kullanılır, burada amaç iterable (liste vb) bir veri yapısının içindeyken
# değişim işlemlerini yönetmektir.
# iki parametre aslında şuna karşılık gelir
# i'ninci eleman işlem i+1'inci eleman

my_list_5 = [x for x in range(1,101)]
sayi_toplam = reduce(lambda x,y:x+y,my_list_5)

#sayi_toplam = list(map(lambda x,y:x+y,my_list_5,my_list_6))
#
#cift_eleman = list(filter(lambda x:x%2==0,my_list_4))
#
#def toplam_sayi(deneme:list):
#    toplam = 0
#    for deger in deneme:
#        toplam = toplam + deger
#    return toplam
#    
#def arama(deneme:list):
#    bos_list = []
#    for eleman in deneme:
#        if eleman%2==0:
#            bos_list.append(eleman)
#    return bos_list

# şöyle çalışır
# listede ilk eleman 1, sonraki 2
# 1+2 = 3
# 3+3 = 6
# 6+4 = 10
# toplam = toplam + i

print(f"1'den 100'e kadar olan sayıların toplamı = {sayi_toplam}")
# listedeki en büyük sayıyı bulan reduce kodu

my_list_6 = [15,-7,963,256,-552,1013]
# Nasıl Çalıştı?
# ilk aşamada x= 15, y= -7 oldu
# 15>7 sorusunun cevabı True döndü
# ikinci aşamada x=15, y=963 oldu
# 15>963 sorusunun cevabı False döndü
# x = 256 oldu y yine aynı kaldu 963 oldu
# 256>963 sorusunun cevabı False döndü
# x = -552 oldu y yine aynı kaldı (963)
# -552>963 sorusunun cevabı False oldu
# x = 1013 oldu y yine 963 kaldı
# 1013 > 963 sorusunun cevabı True oldu
# dolayısıyla lambda x,y:x if x>y else y kodunda x yanıtı galip geldi
# dönen değer 1013 oldu

en_buyuk_eleman = reduce(lambda x,y: x if x>y else y,my_list_6)
print(f"Listedeki en büyük sayı = {en_buyuk_eleman}")
# listedeki elemanların çarpımının toplamını veren kod
my_list_7 = [x for x in range(1,6)]

toplam_carpim = reduce(lambda x,y:x*y,my_list_7)
print(f"1*2*3*4*5 = {toplam_carpim}")
print(f" = {1*2*3*4*5==toplam_carpim}")

def faktoriyel(deneme:list):
    carpim = 1
    for sayi in deneme:
        carpim = carpim * sayi
    return carpim

print(f"Normal fonksiyon ile faktöriyel = {faktoriyel(my_list_7)}")
# bir str değerlerinden oluşan listedeki en uzun kelimeyi bulan reduce kodu

my_list_8 = ["Burdur","Makü","Bucak ZTYO","Furkan","Yazılımcı","Orta Düzey Programlama"]

en_uzun_kelime = reduce(lambda x,y:x if len(x)>len(y) else y,my_list_8)
print(f"Listedeki en uzun kelime = {en_uzun_kelime}")
# bir str değerlerinden oluşan listedeki en uzun kelimeyi bulan reduce kodu

my_list_8 = ["Burdur","Makü","Bucak ZTYO","Furkan","Yazılımcı","Orta Düzey Programlama"]

en_uzun_kelime = reduce(lambda x,y:x if len(x)<len(y) else y,my_list_8)
print(f"Listedeki en kısa kelime = {en_uzun_kelime}")
