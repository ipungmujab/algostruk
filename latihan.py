def ucapkanSalam():
    print("asslamualaikum pren")

def kuadratkan(x):
    return x*x

buah = 'mangga'
daftarBaju = ('batik','loreng','resmi','berdasi')
jumlahBaju=(len(daftarBaju))

class Pesan (object):
    """class pesan memahami konsep class object"""

    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def jumkar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('kalimatku mempunyai', len(self.teks),'karakter')
    def perbarui(self,stringBaru):
        self.teks = stringBaru

class Manusia(object):
    """class manusia sama dengan insiasi nama"""

    keadaan = 'kuciwo'
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("hmmmmm" , self.nama)
    def ungkapkan(self, s):
        print("saya baru saja bingung", s)
    def kesel(self, k):
        print("saya baru saja capek", k)
        self.keadaan = 'kuciwo'
    def mengalikanDenganDua(self, n):
        return n*2

p1 = Manusia('aku')
p1.ucapkanSalam()

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM)\
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class Manusia.
        Mahasiswa kalau makan sambil belajar."""
        print ("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'

m1 = Mahasiswa ('Jamil', 234, 'Surakarta', 250000)
m2 = Mahasiswa ('Andi', 365, 'Magelang', 275000)
m3 = Mahasiswa ('Sri', 676, 'Yogyakarta', 240000)


class kelasKosongan(object):
    pass

k = kelasKosongan()
k.x = 23
k.y = 47
print(k.x + k.y)
k.mystr = 'Indonesia'
print(k.mystr)





        
