# program sederhana mencari kpk
def mencarikpk(x, y):
    if x > y:
        besar = x
    else:
        besar = y
        
    while True:
        if (besar % x == 0) and (besar % y == 0):
            kpk = besar
            break
        besar += 1
    
    return kpk

print("PROGRAM SEDERHANA MENCARI KPK")
x = int(input("Masukkan bilangan pertama: "))
y = int(input("Masukkan bilangan kedua: "))
print("KPK dari", x, "dan", y, "adalah", mencarikpk(x, y))