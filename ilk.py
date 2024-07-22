liste = ["ahmet","emrullah","ervanur","fatih","haydar","mustafa","nurican","ozgur","rabia","zeynep","cevaplar"]
import os
import shutil
konu = "egzersiz_01_02"
for item in liste:
    filename = ""
    filename = f"{item}_{konu}.ipynb"
    if not os.path.exists(f"Egzersizler/{item}/"):
        os.mkdir(f"Egzersizler/{item}/")
    open(f"Egzersizler/{item}/{filename}","w+")

egzersizliste = liste.copy()
egzersizliste.remove("cevaplar")
for item in egzersizliste:
    filename = ""
    filename = f"02_{item}_{konu}.ipynb"
    kaynak = f"Egzersizler/cevaplar/{filename}"
    hedef = f"Egzersizler/{item}/{filename}"
    shutil.copy(kaynak,hedef)