
# latihan 1 
print("SISTEM LOGIN SEDERHANA")

login = 0
while login < 3:
    username = input("Masukan Username: ")
    password = input("Masukan Password: ")

    if username == "nooralam" and password == "alam69":
        print("Selamat datang", username)
        break
    else:
        print("Login gagal!")
        login += 1

if login == 3:
    print("Kesempatan mencoba sudah habis. silahkan hubungi administrasi.")