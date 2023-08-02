import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from nltk.chat.util import Chat, reflections
import sqlite3
import random
import tkinter
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time

class hospital():

    def __init__(self):

        self.Database()
        self.medical_park()
        self.acibadem()
        self.anadolu()
        self.kayitli()
        self.aile_hekimi()
        self.randevu_bilgi()
        self.giris()

    # Database oluştur
    def Database(self):

        self.con = sqlite3.connect("hastane.db")
        self.cursor = self.con.cursor()

    # Gerekli tabloları oluştur
    def medical_park(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS medical_doctor(isim TEXT, soyisim TEXT, telefon INT, alan TEXT, maaş INT)")

    def acibadem(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS acibadem_doctor(isim TEXT, soyisim TEXT, telefon INT, alan TEXT, maaş INT)")

    def anadolu(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS anadolu_doctor(isim TEXT, soyisim TEXT, telefon INT, alan TEXT, maaş INT)")

    def kayitli(self):
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS hasta_bilgileri
                            (isim TEXT, soyisim TEXT, 
                            telefon INT, e_posta TEXT,
                            sifre INT, adres TEXT,boy INT,
                            kilo INT, yas INT)''')
        
    def aile_hekimi(self):

        self.cursor.execute("CREATE TABLE IF NOT EXISTS aile_hekimi_table(isim TEXT, soyisim TEXT, telefon INT, maaş INT)")
        
    def randevu_bilgi(self):

        self.con.execute("CREATE TABLE IF NOT EXISTS randevu(randevu TEXT)")

    # Giriş sayfası
    def giris(self):

        window = tk.Tk()
        window.title("Giriş")
        frame = tk.Frame(window)
        frame.pack()

        window.iconbitmap("hospital_icon.ico")

        giris_yap = tk.LabelFrame(frame,text="Giriş")
        giris_yap.grid(row=0,column=0,padx=40,pady=60)

        e_posta_label = tk.Label(giris_yap,text="E posta:")
        e_posta_label.grid(row=0,column=0)

        sifre_label = tk.Label(giris_yap,text="Şifre:")
        sifre_label.grid(row=0,column=1)

        e_posta_entry = tk.Entry(giris_yap)
        sifre_entry = tk.Entry(giris_yap,show="*")
        e_posta_entry.grid(row=1,column=0)
        sifre_entry.grid(row=1,column=1)

        a = random.randint(100,1000)
        yazdir = tk.Label(giris_yap,text=f"Güvenlik kodu: {a}")
        yazdir.grid(row=2,column=0)

        yazdir_entry = tk.Entry(giris_yap)
        yazdir_entry.grid(row=2,column=1)

        yazdir_label = tkinter.Label(giris_yap,text="")
        yazdir_label.grid(row=4,column=1)

        # Resmi yükleyip boyutunu ayarladık
        image = Image.open("user.png")
        resized_image = image.resize((50, 50)) 
        photo = ImageTk.PhotoImage(resized_image)

        # Resimin görüntülenmesi için
        image_label = tk.Label(window, image=photo)
        image_label.place(x=40, y=10)

        # Resimi görüntüleme
        image_label = tk.Label(window, image=photo)
        image_label.place(x=15, y=15, relwidth=0, relheight=0)

        def sifre_mi_unuttum():

            sifre_sifirla_top_level = tk.Toplevel()
            sifre_sifirla_top_level.geometry("280x290")

            e_posta_kontrol = tk.Label(sifre_sifirla_top_level,text="E posta adresinizi girin:")
            yeni_sifre = tk.Label(sifre_sifirla_top_level,text="Yeni şifreniz:")
            yeni_sifre_tekrar = tk.Label(sifre_sifirla_top_level,text="Yeni şifreniz tekrar:")

            e_posta_kontrol.place(x=10,y=20)
            yeni_sifre.place(x=10,y=60)
            yeni_sifre_tekrar.place(x=10,y=100)

            e_posta_kontrol_entry = tk.Entry(sifre_sifirla_top_level)
            e_posta_kontrol_entry.place(x=145,y=25)

            yeni_sifre_entry = tk.Entry(sifre_sifirla_top_level)
            yeni_sifre_entry.place(x=145,y=65)

            yeni_sifre_tekrar_entry = tk.Entry(sifre_sifirla_top_level)
            yeni_sifre_tekrar_entry.place(x=145,y=105)

            def parola_sifirla():

                posta = e_posta_kontrol_entry.get()
                yeni_sifre1 = yeni_sifre_entry.get()
                yeni_sifre_tekrar1 = yeni_sifre_tekrar_entry.get()

                if yeni_sifre1 != yeni_sifre_tekrar1:
                    messagebox.showerror("Hata","Şifreler uyuşmuyor Tekrar deneyiniz")
                    return False

                self.cursor.execute("SELECT * FROM hasta_bilgileri")
                user = self.cursor.fetchall()

                for i in user:
                    if i[3] != posta:
                        messagebox.showerror("Hata","Kayıtlı e posta adresi bulunamadı")
                    else:
                        self.cursor.execute("UPDATE hasta_bilgileri SET sifre = ?",(yeni_sifre1,))
                        self.con.commit()
                        messagebox.showinfo("Bilgilendirme","Parolanız sıfırlandı")

            sifirla_button = tk.Button(sifre_sifirla_top_level,text="Sıfırla",command=parola_sifirla)
            sifirla_button.place(x=10,y=140)
        
        sifre_sifirla_button = tk.Button(giris_yap,text="Parolamı unuttum",command=sifre_mi_unuttum)
        sifre_sifirla_button.grid(row=5,column=1)

        # Kayıt sayfası
        def kayit():

            yeni_sayfa2 = tk.Toplevel()
            yeni_sayfa2.title("Kayıt")
            frame2 = tk.Frame(yeni_sayfa2)
            frame2.pack()

            kayit_olma = tk.LabelFrame(frame2,text="Kayıt ol")
            kayit_olma.grid(row=0,column=0,padx=20,pady=20)

            isim_label = tk.Label(kayit_olma,text="İsim:")
            isim_label.grid(row=0,column=0)

            soyisim_label = tk.Label(kayit_olma,text="Soyisim:")
            soyisim_label.grid(row=0,column=1)

            isim_entry = tk.Entry(kayit_olma)
            isim_entry.grid(row=1,column=0)

            soyisim_entry = tk.Entry(kayit_olma)
            soyisim_entry.grid(row=1,column=1)

            telefon_label = tk.Label(kayit_olma,text="Telefon Numarası:")
            telefon_label.grid(row=2,column=0)

            telefon_entry = tk.Entry(kayit_olma)
            telefon_entry.grid(row=3,column=0)

            posta_label = tk.Label(kayit_olma,text="E posta:")
            posta_label.grid(row=2,column=1)

            posta_entry = tk.Entry(kayit_olma)
            posta_entry.grid(row=3,column=1)

            sifre = tk.Label(kayit_olma,text="Şifre:")
            sifre.grid(row=4,column=0)

            sifre_entry1 = tk.Entry(kayit_olma,show="*")
            sifre_entry1.grid(row=5,column=0)

            sifre_tekrar = tk.Label(kayit_olma,text="Şifre Tekrar")
            sifre_tekrar.grid(row=4,column=1)

            sifre_tekrar_entry = tk.Entry(kayit_olma,show="*")
            sifre_tekrar_entry.grid(row=5,column=1)

            adres = tk.Label(kayit_olma,text="Adres:")
            adres.grid(row=6,column=0)

            adres_Entry = tk.Entry(kayit_olma)
            adres_Entry.grid(row=7,column=0)

            # Kayıt sayfasının devamı
            def devam_et():
                
                # Şifre kontrolü
                sifre_kontrol = sifre_entry1.get()
                sifre_tekrar_kontrol = sifre_tekrar_entry.get()

                if sifre_kontrol != sifre_tekrar_kontrol:
                
                    errorr = messagebox.showerror("Hata","Şifreler uyuşmuyor")
                    if errorr:
                        sifre_entry1.delete(0,tk.END)
                        sifre_tekrar_entry.delete(0,tk.END)
                        return False
                else:
                    devam_top
                
                devam_top = tk.Toplevel()
                devam_top.geometry("280x270")

                boy = tk.Label(devam_top,text="Boyunuzu giriniz:")
                boy.place(x=10,y=20)

                kilo = tk.Label(devam_top,text="Kilonuzu giriniz:")
                kilo.place(x=10,y=60)

                yas = tk.Label(devam_top,text="Yaşınızı giriniz:")
                yas.place(x=10,y=100)

                boy_entry = tk.Entry(devam_top)
                boy_entry.place(x=110,y=25)

                kilo_entry = tk.Entry(devam_top)
                kilo_entry.place(x=110,y=65)

                yas_entry = tk.Entry(devam_top)
                yas_entry.place(x=110,y=105)

                # Kayıt oluken girdiğimiz bilgileri veritabanına kaydediyoruz          
                def veritabani():

                    isim = isim_entry.get()
                    soyisim = soyisim_entry.get()
                    telefon = telefon_entry.get()
                    posta = posta_entry.get()
                    sifre_gir = sifre_entry1.get()
                    adres1 = adres_Entry.get()
                    boy_gir = boy_entry.get()
                    kilo_gir = kilo_entry.get()
                    yas_gir = yas_entry.get()

                    self.cursor.execute("INSERT INTO hasta_bilgileri VALUES(?,?,?,?,?,?,?,?,?)",(isim,soyisim,telefon,posta,
                                                                                                sifre_gir,adres1,boy_gir,kilo_gir,yas_gir))
                    self.con.commit()

                button1 = tk.Button(devam_top,text="Kaydı tamamla",command=veritabani)
                button1.place(x=10,y=150)

            button_devam = tk.Button(kayit_olma,text="Devam",command=devam_et)
            button_devam.grid(row=7,column=1)

        button = tk.Button(giris_yap,text="Kayıt ol",command=kayit)
        button.grid(row=4,column=1)

        # Kayıt olduktan sonra isteme giriş sağlamak için gerekli bilgiler kontrol ediliyor
        def giris_yapma():

            e_posta1 = e_posta_entry.get()
            sifre1 = sifre_entry.get()

            self.cursor.execute("SELECT * FROM hasta_bilgileri WHERE e_posta = ? AND sifre = ?", (e_posta1, sifre1))
            user = self.cursor.fetchone()

            if a == int(yazdir_entry.get()):
                time.sleep(1)
                yazdir_label_Dogru = tkinter.Label(giris_yap,text="Güvenlik kodu Doğru")
                yazdir_label_Dogru.grid(row=3,column=1)
            else:
                time.sleep(1)
                yazdir_label_false = tkinter.Label(giris_yap,text="Güvenlik kodu Yanlış")
                yazdir_label_false.grid(row=3,column=1)
                messagebox.showerror("Hata","Güvenlik kodunu tekrar giriniz")

                return False

            if user:
                islemler()
            else:
                messagebox.showerror("Hata","Hatalı giriş Tekrar deneyiniz.")

        giris_button = tk.Button(giris_yap,text="Giriş yap",command=giris_yapma)
        giris_button.grid(row=4,column=0,padx=15,pady=30)

        # Girişden sonra yapmak istediğimiz işlemi seçiyoruz
        def islemler():

            yeni_sayfa3 = tk.Toplevel()
            yeni_sayfa3.geometry("350x500")
            yeni_sayfa3.title("İşlemler")
            
            def randevu_al():
            
            # Randevu alma alanında Combboxlar ile gideceğimiz bölüm, hastane ve doktoru seçiyoruz
                top_level_aa = tk.Toplevel()
                top_level_aa.geometry("280x280")

                combo = ttk.Combobox(top_level_aa,values=["Beyin Cerrahisi","Deri ve Zührevi","Kalp cerrahisi","kulak,burun,boğaz","kemik","Diş"])
                combo.pack()

                def yazdir():
                    a1 = combo.get()
                    if a1 == "Beyin Cerrahisi":
                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def beyin():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=beyin)
                        button_medical.place(x=80, y=120)

                    elif a1 == "Deri ve Zührevi":
            
                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def deri():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=deri)
                        button_medical.place(x=80, y=120)

                    elif a1 == "Kalp cerrahisi":

                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def kalp():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=kalp)
                        button_medical.place(x=80, y=120)

                    elif a1 == "kulak,burun,boğaz":
                        a = combo.get()

                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def kbb():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=kbb)
                        button_medical.place(x=80, y=120)

                    elif a1 == "kemik":

                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def kemik():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=kemik)
                        button_medical.place(x=80, y=120)

                    elif a1 == "Diş":

                        combo2 = ttk.Combobox(top_level_aa, values=["Medical Park", "Acıbadem", "Anadolu Hastanesi"])
                        combo2.place(x=70, y=90)
                        
                        def dis():
                            b = combo2.get()
                            if b == "Medical Park":
                                self.cursor.execute("SELECT * FROM medical_doctor WHERE alan = ?",(a1,))
                                user1 = self.cursor.fetchall()
                                doctors = []
                                for doktor in user1:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Acıbadem":
                                self.cursor.execute("SELECT * FROM acibadem_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec1():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")
                                        
                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec1)
                                button_onayla.place(x=70,y=200)

                            elif b == "Anadolu Hastanesi":
                                self.cursor.execute("SELECT * FROM anadolu_doctor WHERE alan = ?",(a1,))
                                user = self.cursor.fetchall()
                                doctors = []
                                for doktor in user:
                                    doktor1 = doktor[0]
                                    doktor2 = doktor[1]
                                    topla = f"{doktor1} {doktor2}"
                                    doctors.append(topla)
                                combo3 = ttk.Combobox(top_level_aa, values=doctors)
                                combo3.place(x=70, y=160)

                                def doktor_sec():

                                    a = combo3.get()
                                    message = messagebox.askyesnocancel("Bildirim",f"'{a}' - isimli doktora randevunuzu onaylıyormusunuz.")
                                    if message == YES:
                                        self.cursor.execute("INSERT INTO randevu VALUES(?)",(a1,))
                                        self.con.commit()
                                        messagebox.showinfo("Bildirim","Lütfen Randevu iptali için 1 gün önceden iptal edin")
                                    elif message == NO:
                                        messagebox.showinfo("Bildirim","Randevu alımı iptal edildi")

                                button_onayla = tk.Button(top_level_aa,text="Randevu al",command=doktor_sec)
                                button_onayla.place(x=70,y=200)
                                
                        button_medical = tk.Button(top_level_aa, text="Hastaneyi seç", command=dis)
                        button_medical.place(x=80, y=120)

                button_yazdir = tk.Button(top_level_aa,text="Hastaneleri Göster",command=yazdir)
                button_yazdir.place(x=80,y=40)

            image2 = Image.open("medicine.png")
            resized_image2 = image2.resize((70, 70))
            photo2 = ImageTk.PhotoImage(resized_image2)

            button_randevu = tk.Button(yeni_sayfa3, image=photo2, command=randevu_al)
            button_randevu.image = photo2
            button_randevu.place(x=50, y=50)

            randevu_alma = tk.Label(yeni_sayfa3,text="Randevu Al")
            randevu_alma.place(x=50,y=140)

            # Daha önce oluşturduğumuz randevumuzu burada siliyoruz
            def randevu_sil():

                top_level_aa1 = tk.Toplevel()
                top_level_aa1.geometry("280x280")

                frame4 = tk.Frame(top_level_aa1)
                frame4.pack()

                randevu_sil = tkinter.LabelFrame(frame4,text="Randevu Silme") 
                randevu_sil.grid(row=0,column=3,padx=20,pady=20)

                randevu_sil_label = tk.Label(randevu_sil,text=("Randevularım"))
                randevu_sil_label.grid(row=1,column=0)
                
                # Bütün randevularımızı Combobox ile gösteriyoruz
                self.cursor.execute("SELECT  * FROM randevu")
                ara = self.cursor.fetchall()

                randevu_delete = [i[0] for i in ara]
                
                randevu_box = ttk.Combobox(randevu_sil,values=randevu_delete)
                randevu_box.grid(row=2,column=0)

                # Silme işlemi burada gerçekleşiyor
                def randevu_silme_islem():

                    secilen = randevu_box.get()

                    self.cursor.execute("DELETE FROM randevu WHERE randevu = ?",(secilen,))
                    self.con.commit()

                    messagebox.showinfo("",f"{secilen} Randevunuz silimiştir")
                sil = tkinter.Button(randevu_sil,text="Sil",command=randevu_silme_islem)
                sil.grid(row=3,column=0)


            image3 = Image.open("close.png")
            resized_image3 = image3.resize((70, 70))
            photo3 = ImageTk.PhotoImage(resized_image3)

            button_randevu = tk.Button(yeni_sayfa3, image=photo3, command=randevu_sil)
            button_randevu.image = photo3
            button_randevu.place(x=200, y=50)

            randevu_delete = tk.Label(yeni_sayfa3,text="Randevu silme")
            randevu_delete.place(x=200,y=140)

            # Randevularımızı görüntüleyebiliriz
            def randevularım():
                top_level_aa2 = tk.Toplevel()
                top_level_aa2.geometry("280x280")

                frame3 = tk.Frame(top_level_aa2)
                frame3.pack()

                randevu = tkinter.LabelFrame(frame3, text="Yaklaşan Randevularım")
                randevu.grid(row=0, column=3, padx=20, pady=20)

                randevu_label = tkinter.Label(randevu, text="Randevu ara")
                randevu_label.grid(row=1, column=0)

                self.cursor.execute("SELECT * FROM randevu")
                ara = self.cursor.fetchall()

                randevu_names = [i[0] for i in ara]

                randevu_box = ttk.Combobox(randevu, values=randevu_names)
                randevu_box.grid(row=2, column=0)

            image4 = Image.open("diagnosis.png")
            resized_image4 = image4.resize((70, 70))
            photo4 = ImageTk.PhotoImage(resized_image4)

            button_randevu = tk.Button(yeni_sayfa3, image=photo4, command=randevularım)
            button_randevu.image = photo4
            button_randevu.place(x=50, y=180)
            randevu = tk.Label(yeni_sayfa3,text="Randevularım")
            randevu.place(x=50,y=270)

            # Aile hekiminizden randevu almak için...
            def  aile_hekimi_randevu():
                
                top_level_aa3 = tk.Toplevel()
                top_level_aa3.geometry("280x280")

                # Burada Combobox ile doktor seçiyoruz
                def aile_hekimi():

                    top_level_aa4 = tk.Toplevel()
                    top_level_aa4.geometry("245x245")

                    self.cursor.execute("SELECT * FROM aile_hekimi_table")
                    user = self.cursor.fetchall()

                    doktor_isimleri = [i[0] for i in user]

                    combo = ttk.Combobox(top_level_aa4,values=doktor_isimleri)
                    combo.place(x=60,y=50)

                    # Randevu onaylamak için gelen mesaj kutusuna YES yada NO diyoruz
                    def onay_iptal():
                        
                        aile_hekimi_kayit = ("Aile hekimi")
                        message = messagebox.askyesno("Mesaj","aile hekiminden randevu alamayı onaylıyormusunuz")
                        if message == YES: # Randevu tablosuna randevuyu kaydetmek için
                            self.cursor.execute("INSERT INTO randevu VALUES(?)",(aile_hekimi_kayit,))
                            self.con.commit()
                        elif message == NO: # İptal
                            messagebox.showerror("Bildirim","Randevu alımı iptal edildi")

                    button_onay_iptal = tk.Button(top_level_aa4,text="Doktoru seç",command=onay_iptal)
                    button_onay_iptal.place(x=60,y=85)
                            
                button_aile_hekimi = tk.Button(top_level_aa3,text="Aile Hekiminden sıra al",command=aile_hekimi,width=20) 
                button_aile_hekimi.place(x=70,y=75)

                # Misafir girişi oluştur 
                def misafir():

                    top_level_aa5 = tk.Toplevel()
                    top_level_aa5.geometry("245x245")

                    t_c_no = tk.Label(top_level_aa5,text="T.C kimlik numaranızı giriniz:")
                    t_c_no.place(x=10,y=20)

                    t_c_no_entry = tk.Entry(top_level_aa5,width=20)
                    t_c_no_entry.place(x=10,y=65)

                    # Misafirlerle ilgilenen doktoru seçiyoruz                    
                    self.cursor.execute("SELECT * FROM aile_hekimi_table")
                    sec = self.cursor.fetchall()

                    liste = []
                    for i in sec:
                        b = i[0]
                        b1 = i[1]
                    topla = f"{b} {b1}"
                    liste.append(topla)

                    combo1 = ttk.Combobox(top_level_aa5,values=liste)
                    combo1.place(x=10,y=90)

                    # Randevu alma
                    def doktor_sec():

                        messagebox.askokcancel("Bildirim","Randevu alındı")

                    doktor_sec_button = tk.Button(top_level_aa5,text="Seç",width=20,command=doktor_sec)
                    doktor_sec_button.place(x=10,y=120)

                button_misafir_hekimi = tk.Button(top_level_aa3,text="Misafir Girişi",command=misafir,width=20)
                button_misafir_hekimi.place(x=70,y=125)

            image5 = Image.open("stethoscope.png")
            resized_image5 = image5.resize((70, 70))
            photo5 = ImageTk.PhotoImage(resized_image5)

            button_randevu = tk.Button(yeni_sayfa3, image=photo5, command=aile_hekimi_randevu)
            button_randevu.image = photo5
            button_randevu.place(x=200, y=180)
            aile_hekimi = tk.Label(yeni_sayfa3,text="Aile Hekimi")
            aile_hekimi.place(x=200,y=270)

            # Kişisel bilgileri göstermek için
            def bilgilerim():
                
                Toplevel_bilgi = tk.Toplevel()
                Toplevel_bilgi.geometry("250x240")

                # hasta bilgilerine git
                self.cursor.execute("SELECT * FROM hasta_bilgileri")

                user=self.cursor.fetchall()
                for index, row in enumerate(user):

                    isim_label = tk.Label(Toplevel_bilgi, text=f"İsim: {row[0]}")
                    isim_label.grid(row=index, column=0, pady=5)

                    soyisim_label = tk.Label(Toplevel_bilgi, text=f"Soyisim: {row[1]}")
                    soyisim_label.grid(row=index+1, column=0, pady=5)

                    boy_label = tk.Label(Toplevel_bilgi, text=f"Boy: {row[6]}")
                    boy_label.grid(row=index+2, column=0, pady=5)

                    kilo_label = tk.Label(Toplevel_bilgi, text=f"Kilo: {row[7]}")
                    kilo_label.grid(row=index+3, column=0, pady=5)

                    yas_label = tk.Label(Toplevel_bilgi, text=f"Yaş: {row[8]}")
                    yas_label.grid(row=index+4, column=0, pady=5)

                # Bilgilerimizi değiştirmek, güncellemek için...
                def bilgilerimi_guncelle():

                    Toplevel_guncelle = tk.Toplevel()
                    Toplevel_guncelle.geometry("250x240")

                    boy_guncelle = tk.Label(Toplevel_guncelle,text="Boyunuzu giriniz:")
                    kilo_guncelle = tk.Label(Toplevel_guncelle,text="Kilonuzu giriniz:")

                    boy_guncelle.place(x=15,y=20)
                    kilo_guncelle.place(x=15,y=50)

                    boy_entry = tk.Entry(Toplevel_guncelle)
                    kilo_entry = tk.Entry(Toplevel_guncelle)

                    boy_entry.place(x=120,y=25)
                    kilo_entry.place(x=120,y=55)

                    # Girilen yeni bilgileri kaydetmek için 
                    def guncel_bilgi_kaydet():

                        try:
                            boy1 = int(boy_entry.get())
                            kilo1 = int(kilo_entry.get())

                            self.cursor.execute("UPDATE hasta_bilgileri SET boy=?, kilo=?", (boy1, kilo1))
                            self.con.commit()
                            messagebox.showinfo("Bilgilendirme", "Bilgileriniz başarıyla güncellendi!")

                        except ValueError:
                            messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

                    kaydet_button = tk.Button(Toplevel_guncelle,text="Güncelle",command=guncel_bilgi_kaydet)
                    kaydet_button.place(x=15,y=90)

                guncelle_button = tk.Button(Toplevel_bilgi,text="Bilgilerimi güncelle",command=bilgilerimi_guncelle)
                guncelle_button.place(x=15,y=180)

            image6 = Image.open("cardiogram.png")
            resized_image6 = image6.resize((70, 70))
            photo6 = ImageTk.PhotoImage(resized_image6)

            button_bilgi = tk.Button(yeni_sayfa3, image=photo6, command=bilgilerim)
            button_bilgi.image = photo6
            button_bilgi.place(x=50, y=310)
            aile_hekimi = tk.Label(yeni_sayfa3,text="Bilgilerim")
            aile_hekimi.place(x=50,y=400)

        
        window.mainloop()

if __name__ == "__main__":

    app = hospital()