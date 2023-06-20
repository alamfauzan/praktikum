print("===== PROGRAM SEDERHANA MENGHITUNG PANGKAT =====")
bilangan = int(input("Masukan bilangan :"))
pencacah = int(input("masukan pencacah :"))
hasil = 1

for i in range(pencacah):
    hasil *= bilangan
    print(hasil)
