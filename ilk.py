liste = ["ahmet","emrullah","ervanur","fatih","haydar","mustafa","nurican","ozgur","rabia","zeynep","cevaplar"]
import os
# filename = 
for item in liste:
    filename = ""
    filename = f"{item}_" + "ilk.ipynb"
    if not os.path.exists(f"Egzersizler/{item}/"):
        os.mkdir(f"Egzersizler/{item}/")
        open(f"Egzersizler/{item}/{filename}","w+")

