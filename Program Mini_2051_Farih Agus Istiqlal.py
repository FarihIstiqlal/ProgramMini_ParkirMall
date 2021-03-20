'''
Program Untuk Menghitung Harga Parkir dan Mencetak Struk

'''
import os

harga = int(0)
total = int(0)
denda = int(0)

os.system("cls")
print("\n", ">"*15, "SELAMAT DATANG", "<"*15)
print(">"*10, "DILOKET PEMBAYARAN PARKIR", ">"*10)
print(">"*5,"DIKENAKAN DENDA PARKIR DIATAS 24 JAM", ">"*5, "\n")

while True:
    try:
        jenis = int(input('kendaraan roda (2/4) : '))
        break
    except ValueError:
        print('Mohon input menggunakan angka!!\n')

while True:
    try:
        waktu = int(input('Waktu Parkir (jam) : '))
        break
    except ValueError:
        print('Mohon input menggunakan angka!!\n')

if waktu > 24:
    denda = int(10000) * (waktu // 24)

if jenis == 2 :
    harga = 2000
elif jenis == 4 :
    harga = 4000
else :
    print('error')
    exit()
total = harga * waktu + 10000 * (waktu // 24)

os.system("cls")
print("=="*15)
print('         MALL ALPHA')
print("==" * 15)
print('Waktu Parkir :',waktu,'Jam')
print('Biaya parkir : Rp.',harga )
print('Denda : Rp.',denda)
print('Total : Rp.',total)
print("==" * 15)
print()