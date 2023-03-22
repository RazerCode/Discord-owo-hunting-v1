import requests
import time
import os
from os import system
import colorama
from colorama import Fore, Back, Style
import random

#!kullanıcı ayarları
kanalid = "951779689578512404" #kanal id
ownerid = "" #owner id

#!program ayarları
url = f"https://discord.com/api/v9/channels/{kanalid}/messages"
mesajsayi = 0
totalyazi = 0
dinlenmesure = 240
dinlenmesaj = 10
gelismiskoruma = 0 #0 = kapalı / 1 = açık

token = {
    'authorization': '' #tokeniniz
}

baslatildimesaj = {
    'content': f"Bot Başlatıldı :white_check_mark:"
}

requests.post(url,headers=token,data=baslatildimesaj)

#!seçim ekranı
def ekran():
    system("cls")
    system("title FastAll Owo Hunting Bot")
    print("")
    print(Fore.RED+" 1-" + Fore.RESET + " Başlat")
    print(Fore.RED+" 2-" + Fore.RESET + " Ayarlar")
    print(Fore.RED+" 3-" + Fore.RESET + " Yönetim Paneli (v2 de gelecek)")
    secim = int(input(" Seçiminiz: "))
    if secim == 1:
        tekrar()

    elif secim == 2:
        ayarlar()

    elif secim == 3:
        yonetimpanel()

#!owo hunting
def tekrar():
    #*global tanımlama
    global ownerid
    global url
    global mesajsayi
    global totalyazi
    global dinlenmesure
    global gelismiskoruma
    #!döngü
    while True:
        #*veriler
        system("cls")
        print(Fore.BLUE + " FastAll Owo Hunting Bot")
        print(Fore.GREEN + " Writed:" + " " + Fore.RESET+ str(mesajsayi))
        print("")
        print(Fore.GREEN + " Total Writed:" + " " + Fore.RESET+ str(totalyazi))
        avla = {
            'content': f"owo hunt"
        }

        sat = {
            'content': f"owo sell all"
        }

        dinlenmemesaj = {
            'content': f"Bot kendini {dinlenmesure} saniye boyunca molaya aldı"
        }


        #*mesaj gönderici
        requests.post(url,headers=token,data=avla)
        #!gelişmiş koruma
        if gelismiskoruma == 1:
            #*gelişmiş koruma mesajları
            mesajliste = [
                "Merhaba nasılsın?",
                "Merhaba günün nasıl geçti?",
                "Bende iyiyim sağ ol",
                "Umarım daha iyi olursun",
                "FastAll çok iyi bir insan",
                "Hayatın nasıl gidiyor?"
            ]
            #*yüzdelik ve randomlar
            randomsayi = random.randint(0, 5)
            yuzdelik = random.randint(0,1)
            mesajicerik = {
                'content': f"{mesajliste[randomsayi]}"
            }
            kiss = {
                'content': f"owo kiss <@!{ownerid}>"
            }

            #*yüzdeliğe göre random owo kiss
            if yuzdelik == 1:
                requests.post(url,headers=token,data=kiss)
            
            requests.post(url,headers=token,data=mesajicerik)
        #!dinlenme aşaması
        if mesajsayi == dinlenmesaj:
            requests.post(url,headers=token,data=sat)
            requests.post(url,headers=token,data=dinlenmemesaj)
            time.sleep(dinlenmesure)
            #*verileri sıfırlama
            totalyazi = totalyazi + 1
            mesajsayi = 0
            tekrar()
        #!veri çoğaltma
        mesajsayi = mesajsayi + 1
        totalyazi = totalyazi + 1
        time.sleep(15)

#!ayarlar
def ayarlar():
    #*global tanımlama
    global dinlenmesure
    global dinlenmesaj
    global gelismiskoruma
    #*seçim ekranı
    system("cls")
    print("")
    print(Fore.BLUE+" Eğer belirtilen ayarın yanında 0 varsa kapalı 1 varsa açık demektir!"+Fore.RESET)
    print("")
    print(" Dinlenme süresi: " + str(dinlenmesure))
    print(" Kaç Mesaja Ulaşınca Program Dinlenir: " + str(dinlenmesaj))
    print(" Gelişmiş Koruma: " + str(gelismiskoruma))
    print("")
    print(Fore.RED+" 1-" + Fore.RESET+" Dinlenme Süresi")
    print(Fore.RED+" 2-" + Fore.RESET+" Kaç mesajda bir mola vereceği")
    print(Fore.RED+" 3-" + Fore.RESET+" Gelişmiş Sohbet Koruma Aç/Kapat")
    print(Fore.RED+" 4-" + Fore.RESET+" Geri Gel")
    secim2 = int(input(" Seçiminiz: "))
    #!dinlenme süresi ayarlama
    if secim2 == 1:
        system("cls")
        print("")
        print(Fore.BLUE+" Default süre 240 saniyedir"+Fore.RESET)
        print(Fore.BLUE+" Bu süre 220 saniyenin altında belirlenirse hesabınız doğrulama yiyebilir"+Fore.RESET)
        print("")
        dinlenmesure = int(input(" Süre giriniz: "))
        ayarlar()
    
    #!kaç mesaj attıktan sonra dinleneceği
    if secim2 == 2:
        system("cls")
        print("")
        print(" Default toplam 10 mesaja ulaşılınca belirtilen süre kadar dinlenilir")
        print("")
        dinlenmesaj = int(input(" Kaç mesaja ulaşılınca dinlendirmek istediğinizi giriniz: "))
        ayarlar()

    #!gelişmiş koruma açıp kapama
    if secim2 == 3:
        if gelismiskoruma == 1:
            gelismiskoruma = 0
            ayarlar()

        elif gelismiskoruma == 0:
            gelismiskoruma = 1
            ayarlar()

    #!seçim ekranına geri dönme
    if secim2 == 4:
        ekran()

#!yönetim panele giriş
def yonetimpanel():
    print("test")


#!program başlatılınca ilk önce seçim ekranına yönlendirilir
ekran()

#*PROGRAM HAKKINDA
#!Program tamamen fastall tarafından kodlanmıştır
#?Programın v1 sürümüne sahip olanlar v2 sürümü çıkınca belli bir ücret karşılığında o sürümede erişebilirler
#!Programın izinsiz paylaşılması ve satılması yasaktır program tamamen 10=% şekilde fastalla aittir satılması durumunda yetkililer ile iletişime geçilip gereken uygulama yaptırılacaktır
#?Yönetim paneli üzerinden bota ek komutlar yollayabilirsiniz böyle bir sistem kullanılmasının sebebi çoklu görev kullanılmamasındandır
#?Program hiç bir şekilde token vb sızdırmaz verileri 3. kişilere göndermez veriler sadece programı kim kullanıyorsa onun şahsi bilgisayarında kalır
#?Programı kullanırken token bölümüne tel onaysız token girilirse sıkıntılar yaşanabilir captcha yiyebilir oda düşük bir ihtimal
#?Birdem den fazla tokenle çalıştırılabilir
#!Program çalışmamakta ise discord üzerinden iletişime geçebilirsiniz Fast#6099
#!Programı ana hesaplarınızda kullanmamanız önerilir olası bir owo yetkilisi bunu fark ederse sizi bottan banlayabilirler onun dışında captcha takılmamaktadır
#!Bot captchaya takılır ise seçim ekranından ayarlara gelip dinlenme süresini yükseltip gelişmiş korumayı açabilirsiniz