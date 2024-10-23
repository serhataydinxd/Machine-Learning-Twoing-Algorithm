# 152120221118, Serhat Aydın
# Twoing algorithm

while(True):
    ders = int(input("Ders adını seçiniz: (0:Matematik 1:Kimya 2:Edebiyat) "))
    if((ders == 1) or (ders == 2)): #Ders Kimya veya Edebiyat ise direkt geçer
        print("Geçti \n")
    else: #Matematik
        saat = int(input("Çalışma saati giriniz: 0:Düşük 1:Yüksek"))
        if(saat == 0): #Düşük saatli matematikten direkt kalır
            print("Kaldı \n")
        else:
            devam = int(input("Devam oranını giriniz: (0:Düşük 1:Yüksek)")) #Devam oranı yüksek ise geçer düşük ise kalır
            if(devam):
                print("Geçti \n")
            else:
                print("Kaldı \n")