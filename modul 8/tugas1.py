def linear_search(keywords,data):
    for i in range(len(data)):
        if str (data[i]).lower == keyword.lower():
            print(f"kendaraan {keyword} berada diparkiran ")
            return i
    print(f"Kendaraan {keyword} tidak berada diparkiran ")
    return -1

data = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
keyword = input("Masukan plat: ")
linear_search(keyword, data)