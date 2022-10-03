# Uygulama: Python gorevlerini tamamlayiniz.

# Gorev 1: Verilen degerlerin veri yapilarini inceleyiniz.

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

# Gorev 2: Verilen string ifadenin tum harflerini buyuk harfe ceviriniz. Virgul ve nokta yerine space koyunuz,
# kelime kelime ayiriniz.

text = "The goal is to turn data into information, and information into insight."

new_text = text.upper().replace(",", " ").replace(".", " ").split()

new_text

# Gorev 3: Verilen listeye asagidaki adimlari uygulayiniz.

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adim 1: Verilen listenin eleman sayisina bakiniz.

len(lst)

# Adim 2: Sifirinci ve onuncu indeksteki elemanlari cagiriniz.

lst[0]
lst[10]

# Adim 3: Verilen liste üzerinden ["D","A","T","A"] listesi olusturunuz.

lst[0:4]

# Adim 4: Sekizinci indeksteki elemani siliniz.

lst.pop(8)

# Adim 5: Yeni bir eleman ekleyiniz.

lst.append("B")

# Adim 6: Sekizinci indekse "N" elemanini tekrar ekleyiniz.

lst.insert(8, "N")

# Gorev 4: Verilen sozluk yapisina asagidaki adimlari uygulayiniz.

dict = {'Christian': ["America",18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}

# Adim 1: Key degerlerine erisiniz.

dict.keys()

# Adim 2: Value' lara erisiniz.

dict.values()

# Adim 3: Daisy key' ine ait 12 degerini 13 olarak guncelleyiniz.

dict['Daisy'][1] = 13

# Adim 4: Key degeri Ahmet value degeri [Turkey,24] olan yeni bir deger ekleyiniz.

dict['Ahmet'] = ["Turkey",24]

# Adim 5: Antonio' yu dictionary'den siliniz.

dict.pop("Antonio")

# Gorev 5: Arguman olarak bir liste alan, listenin icerisindeki tek ve cift sayilari ayri listelere
# atayan ve bu listeleri return eden fonksiyon yaziniz.

l = [2, 13, 18, 93, 22]

def func(l):
     odd_list = []
     even_list = []
     for i in l:
          if i % 2 != 0:
               odd_list.append(i)
          else:
               even_list.append(i)
     return odd_list, even_list

odd_list, even_list = func(l)

# Gorev 6: Asagida verilen listede muhendislik ve tip fakulterinde dereceye giren ogrencilerin isimleri
# bulunmaktadir. Sirasiyla ilk uc ogrenci muhendislik fakultesinin basari sirasini temsil ederken son uc ogrenci de
# tip fakultesi ogrenci sirasina aittir. Enumarate kullanarak ogrenci derecelerini fakulte ozelinde yazdiriniz.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler,1):
     if index <= 3:
          print(f"Muhendislik Fakultesi {index}. ogrenci: {ogrenci}")
     else:

          print(f"Tip Fakultesi {index-3}. ogrenci: {ogrenci}")

# baska bir yontem:

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
        i += 1
        print("Mühendislik Fakültesi",i,". öğrenci: ",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,". öğrenci: ",x)


# Gorev 7: Asagida 3 adet liste verilmistir. Listelerde sirası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadir. Zip kullanarak ders bilgilerini bastiriniz.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

zip_list = list(zip(kredi, ders_kodu, kontenjan))
print(zip_list)

for kredi, ders_kodu, kontenjan in zip_list:
     print(f"Kredisi {kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

# enumerate ile su sekilde yazilabilir.

# zipList = list(zip(kredi, ders_kodu, kontenjan))
#
# for index, list in enumerate(zipList):
#     print(f"Kredisi {list[0]} olan {list[1]} kodlu dersin kontenjanı {list[2]} kişidir.")

# Görev 8: Asagida 2 adet set verilmistir. Sizden istenilen eger 1. kume 2. kumeyi kapsiyor ise ortak elemanlarini
# eger kapsamiyor ise 2. kumenin 1. kumeden farkini yazdiracak fonksiyonu tanimlamaniz beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def set_func(set1, set2):
     if kume1.issuperset(kume2):
          print(kume1.intersection(kume2))
     else:
          print(kume2.difference(kume1))

set_func(kume1, kume2)


