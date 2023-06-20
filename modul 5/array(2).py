
# buah = ["apel", "jeruk", "anggur", "pisang"]
# nilai = buah[1]
# print(nilai)


# buah = ["apel", "jeruk", "anggur", "pisang"]
# #merubah nilai item array
# buah[1]= "melon"
# print(buah)


# buah = ["apel", "jeruk", "anggur","pidsng"]

# # mengetahui panjang array
# panjang=len(buah)
# print(panjang)


# buah = ["Apel", "Jeruk", "Anggur","Pisang"]

# # looping element array
# for i in buah:
#     print(i)


# buah = ["Apel", "Jeruk", "Anggur","pisang"]

# # menambahkan elemen array 
# buah.append("Semangka")
# print(buah)


# buah = ["Apel", "Jeruk", "Anggur","pisang"]

# # menghapus elemen array
# buah.pop(0)
# buah.remove("Anggur")
# print(buah)


# buah = ["Apel", "Jeruk", "Anggur","pisang"]

# # array 1 dimensi
# for i in buah:
#     print(i)

buah = [["apel","jeruk","jambu","anggur"],
         ["nanas","melon","manggis","duren"]]

for i in range(len(buah)):
    for j in range(len(buah[i])):
        print(buah[i][j]) 


