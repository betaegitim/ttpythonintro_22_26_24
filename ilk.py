liste = ["ahmet","emrullah","ervanur","fatih","haydar","mustafa","nurican","ozgur","rabia","zeynep","cevaplar"]
import os
filename = "ilk.ipynb"
for item in liste:
    filename = f"{item}_" + filename
    if not os.path.exists(f"Egzersizler/{item}/"):
        os.mkdir(f"Egzersizler/{item}/")
    else:
        open(f"Egzersizler/{item}/{filename}","w+")
        print("Zaten Oluşturuldu.")
