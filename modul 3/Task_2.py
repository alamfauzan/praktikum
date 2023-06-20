#if pada dua kondisi

nilai = int(input("Masukkan angka yang akan dibagi : "))
pembagi = int(input("Masukkan angka untuk membagi : "))

if (pembagi==0):
    print("Angka Harus lebih dari 0")
else:
    print("Hasil Pembagian", nilai/pembagi)