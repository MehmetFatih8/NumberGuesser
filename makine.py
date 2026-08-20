import random

liste = []
hayat = 1234
while hayat < 10000:
    liste.append(hayat)
    hayat=hayat+1
print("Başlangıç liste:  " + str(liste))
print("Başlangıç ihtimal sayısı:  " + str(len(liste)))

print("Karakter tekrarı olanlar siliniyor...")
#i = 0
#while i < len(liste):
#    if liste[i] < 1234:
#        liste.pop(i)
#    else:
#        i = i + 1
#print(liste)
#print(len(liste))

i = 0
while i < len(liste):
#    print(liste[i])
    if str(liste[i])[0] == str(liste[i])[1] or str(liste[i])[0] == str(liste[i])[2] or str(liste[i])[0] == str(liste[i])[3] or str(liste[i])[1] == str(liste[i])[2] or str(liste[i])[1] == str(liste[i])[3] or str(liste[i])[2] == str(liste[i])[3]:
        liste.pop(i)
    else:
        i = i + 1
print("Aynı olan karakterler siliniyor" + str(liste))
print("Silinme sonrası ihtimal sayısı:  " + str(len(liste)))

#======BAŞLAGIÇ SEÇİMLERİ=====================================================================================================================
baslasoru = input("Sayıyı tahmin etmek istiyorsan t --- Oyunu yönetmek istiyorsan y --- Analiz etmek istiyorsan a'ya bas: " )

#======OYUN YÖNETİMİ=====================================================================================================================
if baslasoru == "Y" or baslasoru == "y":

    arasonuc=str(00)

    while arasonuc != str(40):
        test=random.choice(liste)
        print("Tahminim: " + str(test))
        arasonuc=input("Artı eksi değerini giriniz: ")

        z = 0
        while z < len(liste):
            arti=0
            eksi=0
            k=0
            while k < 4:
                l = 0
                while l < 4:
                    if str(test)[k] == str(liste[z])[l]:
                        if k == l:
                            arti = arti+1
                        else:
                            eksi = eksi+1
                    l=l+1
                k = k + 1
            sonuc=str(arti)+str(eksi)
            if sonuc != arasonuc:
                liste.pop(z)
            else:
                z = z + 1
        print("Aynı olan karakterler siliniyor" + str(liste))
        print("Silinme sonrası ihtimal sayısı:  " + str(len(liste)))

    if arasonuc == "40":
        exit(print ("iş bitti"))

#===========================================================================================================================


#======TAHMİN ETME OYUNU=====================================================================================================================
if baslasoru == "T" or baslasoru == "t":
    bottahmin = random.choice(liste)
    #print(bottahmin)
    u = 0
    tahminsonuc = 0
    print("Tahminin 0 ile başlamamalı ve rakamları farklı olmalı!")
    while tahminsonuc == 0:
        tarti = 0
        teksi = 0
        kutahminonaylama = 0
        while kutahminonaylama == 0:
            kutahmin = input("Tahminini gir: ")
            if liste.count(int(kutahmin)) == 1:
                kutahminonaylama = 1
            if liste.count(int(kutahmin)) == 0:
                print("Girişiniz kurallara uygun değil.")
        if str(kutahmin)[0] == str(bottahmin)[0]:
            tarti = tarti+1
        if str(kutahmin)[1] == str(bottahmin)[1]:
            tarti = tarti+1
        if str(kutahmin)[2] == str(bottahmin)[2]:
            tarti = tarti+1
        if str(kutahmin)[3] == str(bottahmin)[3]:
            tarti = tarti+1

        if str(kutahmin)[0] == str(bottahmin)[1] or str(kutahmin)[0] == str(bottahmin)[2] or str(kutahmin)[0] == str(bottahmin)[3]:
            teksi = teksi+1
        if str(kutahmin)[1] == str(bottahmin)[2] or str(kutahmin)[1] == str(bottahmin)[3] or str(kutahmin)[1] == str(bottahmin)[0]:
            teksi = teksi+1
        if str(kutahmin)[2] == str(bottahmin)[3] or str(kutahmin)[2] == str(bottahmin)[1] or str(kutahmin)[2] == str(bottahmin)[0]:
            teksi = teksi+1
        if str(kutahmin)[3] == str(bottahmin)[2] or str(kutahmin)[3] == str(bottahmin)[0] or str(kutahmin)[3] == str(bottahmin)[1]:
            teksi = teksi+1
        print("Artı değeri ="+str((tarti))+" Eksi değeri="+str((teksi)))
        u = u+1
        if tarti == 4:
            tahminsonuc = 1


    exit(print("Toplam deneme sayınız: "+str(u)))

#======OTOMATİK ANALİZ=====================================================================================================================
baslangicliste = liste.copy()
dagilim = [0,0,0,0,0,0,0,0,0,0]

if baslasoru == "a" or baslasoru == "A":
    debulmasayisi1 = 0
    debulmasayisi2 = 0
    debulmasayisi3 = 0
    debulmasayisi4 = 0
    debulmasayisi5 = 0
    dabulmasayisi6 = 0
    debulmasayisi7 = 0
    debulmasayisi8 = 0
    dabulmasayisi9 = 0
    dabulmasayisi10 = 0

    tekrarlamasayisi = 0
    while tekrarlamasayisi < 100:
        liste=baslangicliste.copy()
        bottahmin = random.choice(liste)
        print(bottahmin)
        arasonuc=str(00)
        tahminsayisi = 1
        while arasonuc != str(40):
            kutahmin=random.choice(liste)
            print(str(tahminsayisi)+ ". Tahminim: " + str(kutahmin))
            tarti = 0
            teksi = 0

            if str(kutahmin)[0] == str(bottahmin)[0]:
                tarti = tarti+1
            if str(kutahmin)[1] == str(bottahmin)[1]:
                tarti = tarti+1
            if str(kutahmin)[2] == str(bottahmin)[2]:
                tarti = tarti+1
            if str(kutahmin)[3] == str(bottahmin)[3]:
                tarti = tarti+1

            if str(kutahmin)[0] == str(bottahmin)[1] or str(kutahmin)[0] == str(bottahmin)[2] or str(kutahmin)[0] == str(bottahmin)[3]:
                teksi = teksi+1
            if str(kutahmin)[1] == str(bottahmin)[2] or str(kutahmin)[1] == str(bottahmin)[3] or str(kutahmin)[1] == str(bottahmin)[0]:
                teksi = teksi+1
            if str(kutahmin)[2] == str(bottahmin)[3] or str(kutahmin)[2] == str(bottahmin)[1] or str(kutahmin)[2] == str(bottahmin)[0]:
                teksi = teksi+1
            if str(kutahmin)[3] == str(bottahmin)[2] or str(kutahmin)[3] == str(bottahmin)[0] or str(kutahmin)[3] == str(bottahmin)[1]:
                teksi = teksi+1
            print("Artı değeri: "+ str(tarti) +" Eksi Değeri: " + str(teksi))
            arasonuc = str(tarti) + str(teksi)




            z = 0
            while z < len(liste):
                arti=0
                eksi=0
                k=0
                while k < 4:
                    l = 0
                    while l < 4:
                        if str(kutahmin)[k] == str(liste[z])[l]:
                            if k == l:
                                arti = arti+1
                            else:
                                eksi = eksi+1
                        l=l+1
                    k = k + 1
                sonuc=str(arti)+str(eksi)
                if sonuc != arasonuc:
                    liste.pop(z)
                else:
                    z = z + 1
            print("Aynı olan karakterler siliniyor" + str(liste))
            print("Silinme sonrası ihtimal sayısı:  " + str(len(liste)))
            tahminsayisi = tahminsayisi+1
        if arasonuc == "40":
            print("Sonuç bulundu.")
        dagilim[tahminsayisi]=dagilim[tahminsayisi]+1
        tekrarlamasayisi = tekrarlamasayisi+1
        print(dagilim)

