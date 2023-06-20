# Suhu

# s = int(input("Suhu Air: "))


# if s>0 and s<100:
#     print("Air Pada Suhu" , s , "Drajad celcius akan berwujud cair")
# elif s<= 0:
#     print("Air Pada Suhu" , s , "Drajad celcius akan berwujud padat")
# else :
#     print("Air Pada Suhu" , s , "Drajad celcius akan berwujud uap")



# Data 
print("==========INPUT DATA==========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
#1=Islam, 2=Protestan, 3=Katolik, 4=Hindu, 5=Budha
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    agama = "Agama tidak ditemukan"
print("==========OUTPUT========")
print("Nama: ",nama)
print("Jenis Kelamin: ",jk)
print("Agama: ",agama)