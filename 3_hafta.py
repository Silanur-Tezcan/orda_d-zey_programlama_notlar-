# 1'den 100'e kadar (100 de dahil) olan sayıları bir listeye ekleme

my_list_1 = []

for x in range(1,101):
    my_list_1.append(x)

print(my_list_1)
# List comprehension ile
# 1'den 100'e kadar (100 de dahil) olan sayıları bir listeye ekleme

# formül = [değişken_adı for değişken_adı in range(1,101)]
my_list_1_comp = [x for x in range(1,101)]
print(my_list_1_comp)
# 1'den 100'e kadar olan sayılar arasında
# Sadece 2'ye tam bölünen sayıları (çift sayıları) ekleyen kodu yazınız

# 1. yol:
#my_list_2 = []
#
#for x in range(2,101,2):
#    my_list_2.append(x)
#
#my_list_2

# 2. yol = []

my_list_2 = []

for x in range(1,101):
    if x%2 == 0:
        my_list_2.append(x)
    else:
        pass
my_list_2
# List Comprehension ile 1'den 100'e kadar olan sayılar arasında
# Sadece 2'ye tam bölünen sayıları (çift sayıları) ekleyen kodu yazınız

# 1. yol
#my_list_2_comp = [x for x in range(2,101)]
#my_list_2_comp

# 2. yol:

my_list_2_comp = [x for x in range(1,101) if x%2==0]
my_list_2_comp
# List comprehension ile 1'den 100'e kadar olan her sayının 3 katını
# ekleyen kodu yazınız

# list comprehension formülü
# [değişken_adı_ve_yapılacak_işlem for değişken_adı in range(başlangıç, bitiş)]

my_list_3_comp = [x*3 for x in range(1,101)]
my_list_3_comp
my_word_list_1 = ["Furkan","Atlan","ybs","ztyo","ybs-3b"]
# bu listenin tüm elemanlarını büyük karakterle yazdırıp
# yeni bir listeye ekleyen kodu yazınız...

gecici_liste = []

#for x in my_word_list_1:
#    gecici_liste.append(x.upper())

for x in range(len(my_word_list_1)):
    my_item = my_word_list_1[x]
    gecici_liste.append(my_item.upper())
gecici_liste
my_word_list_1 = ["Furkan","Atlan","ybs","ztyo","ybs-3b"]
# bu listenin tüm elemanlarını büyük karakterle yazdırıp
# yeni bir listeye ekleyen kodu yazınız... (list comprehension ile)

my_word_list_1_comp = [x.upper() for x in my_word_list_1]
my_word_list_1_comp
my_word_list_1 = ["Furkan","Atlan","ybs","ztyo","ybs-3b"]

# Aynı kelime listesindeki a harflerini e harfi olarak değiştirip
# bu kelimeleri yeni bir listeye ekleyin (list comprehension ile yapın)

my_word_list_1_replace_comp = [x.replace("a","e").replace("A","E") for x in my_word_list_1]
my_word_list_1_replace_comp

# 1'den 100'e kadar olan sayılar içerisinde tek sayıları negatife dönüştüren
# çift sayıların da karesini alan ve bunları yeni bir listeye ekleyen kod

gecici_liste_2 = []

for x in range(1,101):
    if x%2==0:
        gecici_liste_2.append(x**2)
        #gecici_liste_2.append(x*x)
    else:
        gecici_liste_2.append(-x)

gecici_liste_2
# 1'den 100'e kadar olan sayılar içerisinde tek sayıları negatife dönüştüren
# çift sayıların da karesini alan ve bunları yeni bir listeye ekleyen kod
# (list comprehension ile (list comprehension if else kullanımı))

# formül = [x_if_hali if x_şart else x_else_hali_ for x in liste]

my_list_4_comp = [-x if x%2!=0 else x**2 for x in range(1,101)]
my_list_4_comp
# 1'den 100'e kadar olan tek sayılarda "tek"
# çift sayılarda "çift" yazan kodu yazınız
# hem normal kod hem de list comprehension ile (listeye eklemek)

gecici_liste_3 = []

for x in range(1,101):
    if x%2==0:
        #gecici_liste_3.append("Çift")
        #gecici_liste_3.append(["Çift",x])
        gecici_liste_3.append(f"Çift, {x}")
    else:
        #gecici_liste_3.append("Tek")
        #gecici_liste_3.append(["Tek",x])
        gecici_liste_3.append(f"Tek, {x}")

print(gecici_liste_3)

print("*"*100)

my_list_5 = ["Çift" if x%2==0 else "Tek" for x in range(1,101)]
print(my_list_5)
# 1'den 5'e kadar olan bir listenin değeriyle (5'te dahil)
# 6'dan 10'a kadar (10'da dahil) olan başka bir listenin değerini çarpan kod

print("Normal kod ile gösterim...")

gecici_liste_4 = []

for i in range(1,6):
    for j in range(6,11):
        print(f"i = {i} iken ve j = {j} iken i*j = {i*j}")

print("-"*50)

my_list_comp_ic_ice_dongu = [a*b for a in range(1,6) for b in range(6,11)]
print(my_list_comp_ic_ice_dongu)
notlar = {"ahmet":65, "ali":28, "ayşe":78, "yusuf":15,"tuğçe":40,"kaan":50}

# Notları 50'den büyük olan öğrencilerin isimlerini getiren kodu yazın

print("Normal kod ile gösterim")
#dictionary.items() fonksiyonu sırasıyla key ve value değerlerini döndürür
# dolayısıyla bu fonksiyonu kullanıp iki değişkene atama yaparız

for my_key, my_value in notlar.items():
    if my_value > 50:
        print(my_key)

print("*"*50)

my_list_6_comp = [key for key,value in notlar.items() if value>50]
print(my_list_6_comp)