# FONKSİYONLAR
# Fonksiyonlar, programlamada kullanılırken tıpkı matematikte olduğu gibi
# kullanılır. Belli bir değer aralığı vardır. İşlem yapar, her defasında
# normal kod olarak tekrar tekrar yazmak yerine bir defa fonksiyon
# olarak tanımlanır, parametreli-parametresiz, geriye değer döndüren-döndürmeyen
# olarak farklı türleri vardır.

# 0 ile 10 arasında çift sayıların 8 katını alan fonksiyon
# 2 sayısının 8 katı
# 4 sayısının 8 katı
# 6 sayısının 8 katı
# 8 sayısının 8 katı

# Matematikte yukarıda istenen işlemler şöyle ifade edilebilir
# x € Z+ (0,10)%2==0 f(x) = x*8
for i in range(2,9,2):
    print(f"{i} sayısının 8 katı = {i*8}")
    
def process_of_math_1():
    for i in range(2,9,2):
        print(f"{i} sayısının 8 katı = {i*8}")

process_of_math_1()

kontrol = process_of_math_1()
print(kontrol)
# Parametreli ve geriye değer döndüren fonksiyon
# eğer istenirse, parametrelerin de tipleri en baştan belirtilebilir
# kod okunabilirliği ve hata analizi açısından bu çok önemlidir

def not_hesaplama(vize:int,final:int):
    son_not = (vize*0.4)+(final*0.6)
    return son_not

def gecti_mi_kaldi_mi(gecer_not:float):
    if gecer_not>=50:
        return "GEÇTİNİZ"
    else:
        return "KALDINIZ"
ara_not = not_hesaplama(100,100)
ara_not
son_hesaplama = gecti_mi_kaldi_mi(ara_not)
son_hesaplama
# aşağıdaki -> int ifadesinin anlamı şudur:
# bu fonksiyon int tipinde bir değer return edecektir
# Faydası?

def not_hesaplama(vize:int,final:int) -> int:
    son_not = (vize*0.4)+(final*0.6)
    return int(son_not)


yeni_not = not_hesaplama(40,40)
yeni_not
help(not_hesaplama)
# Dictionary veri yapısı içerisinde
# Yaş bilgisi, 18 ve 18'den büyük olanlar için "Yetişkin"
# olmayanlar için de "ÇOCUK" yazdıran ve bunu geriye döndüren
# fonksiyonu yazınız

my_dictionary_1 = {"ahmet":18,"ayşe":26,"mehmet":23,"ali":11,"yusuf":17}

# bir dictionary veri yapısında sadece anahtar(key) elde edilmek isteniyorsa
# dictionary.keys() fonksiyonu
# sadece o anahtarın tuttuğu değer elde edilmek isteniyorsa:
# dictionary.values() fonksiyonu
# her ikisi aynı anda elde edilmek isteniyorsa dictionary.items()
# fonksiyonu kullanılır.

def yas_durum_hesaplama(par_dictionary:dict):
    my_list = []

    for my_key,my_value in par_dictionary.items():
        if my_value>=18:
            my_list.append(f"{my_key} YETİŞKİNDİR")
        else:
            my_list.append(f"{my_key} ÇOCUKTUR")
    return my_list

sonuc_liste = yas_durum_hesaplama(my_dictionary_1)
sonuc_liste
# dışarıdan parametre olarak bir dictionary alın
# bunun içerisindeki maaş değerleri arasında maaşı 25000'den küçük olanlara
# %140, olmayanlara %50 zam yapıp zamlı hallerini döndüren fonksiyonu yazınız
# hem de bunları bir listeye ekleyip o listeyi döndürecek

my_dictionary_2 = {"ali":21000,"ayşe":35000,"yusuf":22000,"hakan":60000}

def calculate_salary(gecici_par_2:dict):
    my_list = []

    for my_key, my_value in gecici_par_2.items():
        if my_value<25000:
            # bir değişkenin %140'ını hesaplama(zamlı hali-1.yol)
            #new_salary = my_value+(my_value*1.4)
            
            # bir değişkenin %140'ını hesaplama(zamlı hali-2.yol)
            new_salary = my_value*2.4
            my_list.append(f"{my_key} yeni maaşı = {new_salary}")
        else:
            # bir değişkenin %50'sini hesaplama(zamlı hali-2.yol)
            new_salary = my_value*1.5
            my_list.append(f"{my_key} yeni maaşı = {new_salary}")

    return my_list

gecici_maas= calculate_salary(my_dictionary_2)
gecici_maas
# Kendisine parametre olarak verilen listedeki
# çift sayıları bir listeye, tek sayıları başka bir listeye
# ekleyip, bu iki listeyi de döndüren fonksiyonu yazınız

ornek_liste = [x for x in range(0,101)]

def tek_cift(par_gecici_3:list):
    liste_tek, liste_cift = [], []

    for i in par_gecici_3:
        if i%2==0:
            liste_cift.append(i)
        else:
            liste_tek.append(i)
    return liste_tek, liste_cift

my_tek, my_cift = tek_cift(ornek_liste)
print(f"Tek sayıları içeren liste = {my_tek}")
print(f"Çift sayıları içeren liste = {my_cift}")
# Dışarıdan parametre olarak bir liste alan
# bu listedeki tek sayıların negatif halinin 3 katını
# çift sayıların karesinin yarısının 2 farklı listeye ekleyen
# bu iki listeyi döndüren fonksiyonu yazınız

ornek_liste = [x for x in range(0,101)]

def tek_cift(par_gecici_3:list):
    liste_tek, liste_cift = [], []
    
    for i in par_gecici_3: 
        if i%2==0:
            liste_cift.append((i**2)/2)
        else:
            liste_tek.append(i*-3)# -i*3 ya da i*-3

    
    return liste_tek, liste_cift

my_tek, my_cift = tek_cift(ornek_liste)
print(f"Tek sayılar ile ilgili işlemleri içeren liste = {my_tek}")
print(f"Çift sayılar ile ilgili işlemleri içeren liste = {my_cift}")
# girilen ve 10'dan küçük olan pozitif sayıların faktöriyelini
# döndüren fonksiyonu yazınız
# bir sayının kendinden önceki pozitif sayılarla çarpımı

def faktoriyel(sayi):
    if sayi>0 and sayi<=10:
        faktoriyel_sayi = 1
        for i in range(1,sayi+1):
            faktoriyel_sayi *= i
            # faktoriyel_sayi = faktoriyel_sayi * i
        return faktoriyel_sayi

sonuc_1 = faktoriyel(8) # 1*2*3*4*5*6*7*8 = 40320
print(sonuc_1)
print(sonuc_1/2)
print(sonuc_1**0.5)
