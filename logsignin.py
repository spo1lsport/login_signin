def GetData(veri): # İstediğiniz veriyi "example.txt" şeklinde listeye çekebilmeye yarar.
    veri_ndx = open(f"{veri}","r")
    veriler = veri_ndx.readlines()
    verilerIR = veriler[0].split(",")
    veri_ndx.close
    return verilerIR
def UyeOl(): # Üye olma fonksiyonu(Kullanıcı adı, Şifre, Bakiye(Otomatik 1000 bakiye ekler.) bilgilerini txt'ye yazar.).
    def kullaniciAdiEkle(kullanici_adi):
        kullanicilar = open("usernames.txt","a")
        yeni_kullanici = "," + kullanici_adi
        kullanicilar.writelines(yeni_kullanici)
        kullanicilar.close
    def sifreKaydet(sifre):
        sifreler = open("passwords.txt","a")
        sifreIR = "," + sifre
        sifreler.writelines(sifreIR)
        sifreler.close

    kullanici_adi = input("Kullanıcı adı giriniz:")
    while kullaniciAdiKontrol(kullanici_adi) == True:
        print("Bu ad kullanılıyor, lütfen bir daha deneyiniz.")
        kullanici_adi = input("Kullanıcı adı giriniz:")
    kullaniciAdiEkle(kullanici_adi)

    sifre = input("Şifrenizi giriniz:")
    while len(sifre) <8 or len(sifre) >16:
        if len(sifre) <8:
            print("Şifreniz en az 8 karakter uzunluğunda olmalıdır.")
            sifre = input("Şifrenizi giriniz:")
        if len(sifre) >16:
            print("Şifreniz en fazla 16 karakter uzunluğunda olmalıdır.")
            sifre = input("Şifrenizi giriniz:")
    sifreKaydet(sifre)
def kullaniciAdiKontrol(kullanici_adi): # Kullanıcı adının sistemde kayıtlı olup olmadığını kontrol eder.
    kullanicilar = GetData("usernames.txt")
    if kullanici_adi in kullanicilar:
        return True
    else:
        return False
def sifreKontrol(kullanici_adi,sifre): # Kullanıcının girdiği ad ve şifrenin sistemde birbiriyle eşleşiğ eşleşmediğini kontrol eder.
    kullanicilar = GetData("usernames.txt")
    sifreler = GetData("passwords.txt")
    if sifre in sifreler:
        kullanici_adı_yeri = kullanicilar.index(kullanici_adi)
        sifre_yeri = sifreler.index(sifre)
        if sifre_yeri == kullanici_adı_yeri:
            return True
        else:
            return False
    else:
        return False
def GirisYap(): # Sisteme giriş yapma fonksiyonu. Giriş yapan kullanıcının adını return eder.
    kullanici_adi = input("Kullanıcı adınızı giriniz:")
    while kullaniciAdiKontrol(kullanici_adi) == False:
        print("Kullanıcı adı sistemde bulunamadı.Lütfen tekrar deneyiniz.")
        kullanici_adi = input("Kullanıcı adınızı giriniz:")
    if kullaniciAdiKontrol(kullanici_adi) == True:
        sifre = input("Şifrenizi giriniz:")
        if sifreKontrol(kullanici_adi,sifre) == True:
            print("Başarıyla giriş yaptınız.")
            print("Tekrar hoşgeldiniz, " + kullanici_adi + ".")
            return kullanici_adi
        if sifreKontrol(kullanici_adi,sifre) == False:
            while sifreKontrol(kullanici_adi,sifre) == False:
                print("Yanlış şifre girdiniz.")
                sifre = input("Şifrenizi giriniz:")
            print("Başarıyla giriş yaptınız.")
            print("Tekrar hoşgeldiniz, " + kullanici_adi + ".")
            return kullanici_adi
def uyelikVarMi(): # Kullanıcıya sisteme üyeliğinin olup olmadığını sorar; varsa giriş yapma modulüne gönderir, yoksa üye olma modülüne gönderir. Giriş yapan kullanıcının adını return eder.
    while True:
        try:
            uyelik_var_mi = int(input("Üyeliğiniz varsa 1, yoksa 2 tuşlayınız."))
            if uyelik_var_mi == 2:
                print("Lütfen üye olunuz.")
                UyeOl()
                print("Başarıyla kayıt oldunuz." + "\n" + "Lütfen giriş yapınız.")
                return GirisYap()
                break
            elif uyelik_var_mi == 1:
                print("Lütfen giriş yapınız")
                return GirisYap()
                break
            else:
                print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")
                pass
        except ValueError:
            print("Yanlış tuşlama yaptınız. Tekrar deneyiniz.")


giris_yapan_kullanici = uyelikVarMi() # Kimin giriş yaptıgı bilgisini saklamak amacıyla yazıldı.