#program menentukan warna sekunder

while(True):
    a = input("Masukkan Warna 1 :")

    b = input("Masukkan warna 2 :")


    if(a == "red" and b == "blue") or (a == "blue" and b == "red"):
        print("Ungu")
            
    if(a == "yellow" and b == "red") or (a == "red" and b == "yellow"):
        print("orange")

    if(a == "blue" and b == "yellow") or (a == "yellow" and b == "blue"):
        print("green")
            
