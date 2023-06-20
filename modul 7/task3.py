def insertion_sort(nama):
    for i in range(1, len(nama)):
        key = nama[i]
        j = i - 1
        while j >= 0 and nama[j] > key:
            nama[j + 1] = nama[j]
            j -= 1
        nama[j + 1] = key

def display_books(nama):
    print("Daftar Buku:")
    for i, name in enumerate(nama):
        print(f"Judul buku ke-{i+1}: {name}")

nama = []

n = int(input("Masukkan Total buku: "))

for i in range(n):
    namabuku = input(f"Masukkan judul buku ke-{i+1}: ")
    nama.append(namabuku)

print("<======= Urutkan ? =======>")
print("1. Ascending")
print("2. Descending")
option = int(input("Pilih: "))

if option == 1:
    insertion_sort(nama)
    print("Sorting Buku Secara Ascending:")
    display_books(nama)
elif option == 2:
    insertion_sort(nama)
    nama_desc = nama[::-1]
    print("Sorting Buku Secara Descending:")
    display_books(nama_desc)
else:
    print("Pilihan salah. Silakan pilih 1 atau 2.")
