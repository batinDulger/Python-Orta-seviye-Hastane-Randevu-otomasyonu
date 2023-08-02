import sqlite3

class doctor():

    def __init__(self):

        self.veritabani()
        self.secim()

    def veritabani(self):

        self.con = sqlite3.connect("hastane.db")
        self.cursor = self.con.cursor()

    def secim(self):

        self.secim = int(input("Seçim yapınız:"))
        if self.secim == 1:
            self.medical()
        elif self.secim == 2:
            self.acibadem()
        elif self.secim == 4:
            self.anadolu()
        elif self.secim == 5:
            self.aile_hekimi()

    def medical(self):

        while True:
            isim = input("İsim:")
            soyisim = input("Soyisim:")
            telefon = int(input("Telefon numarası:"))
            alan = input("Alan:")
            maas = int(input("Maaş:"))
    
            def kaydet():

                self.cursor.execute("INSERT INTO medical_doctor VALUES(?,?,?,?,?)",(isim,soyisim,telefon,alan,maas))
                self.con.commit()

            kaydet()
            

    def acibadem(self):
        while True:
            isim = input("İsim:")
            soyisim = input("Soyisim:")
            telefon = int(input("Telefon numarası:"))
            alan = input("Alan:")
            maas = int(input("Maaş:"))
    
            def kaydet1():

                self.cursor.execute("INSERT INTO acibadem_doctor VALUES(?,?,?,?,?)",(isim,soyisim,telefon,alan,maas))
                self.con.commit()

            kaydet1()

    def anadolu(self):

        while True:
            isim = input("İsim:")
            soyisim = input("Soyisim:")
            telefon = int(input("Telefon numarası:"))
            alan = input("Alan:")
            maas = int(input("Maaş:"))
    
            def kaydet2():

                self.cursor.execute("INSERT INTO anadolu_doctor VALUES(?,?,?,?,?)",(isim,soyisim,telefon,alan,maas))
                self.con.commit()

            kaydet2()

    def aile_hekimi(self):

        while True:
            isim = input("İsim:")
            soyisim = input("Soyisim:")
            telefon = int(input("Telefon numarası:"))
            maas = int(input("Maaş:"))
    
            def kaydet3():

                self.cursor.execute("INSERT INTO aile_hekimi_table VALUES(?,?,?,?)",(isim,soyisim,telefon,maas))
                self.con.commit()

            kaydet3()

doctor()

    