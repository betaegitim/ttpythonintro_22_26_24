liste = ["ahmet","emrullah","ervanur","fatih","haydar","mustafa","nurican","ozgur","rabia","zeynep","cevaplar","halilyasin"]
import os
import shutil
konu = "list_egzersiz1"
if konu.find("egzersiz") > 0:
    egzersizliste = liste.copy()
    egzersizliste.remove("cevaplar")
    for item in egzersizliste:
        filename = ""
        filename = f"02_{item}_{konu}.ipynb"
        kaynak = f"Egzersizler/cevaplar/{konu}.ipynb"
        hedef = f"Egzersizler/{item}/{filename}"
        shutil.copy(kaynak,hedef)
else:
    for item in liste:
        filename = ""
        filename = f"{item}_{konu}.ipynb"
        if not os.path.exists(f"Egzersizler/{item}/"):
            os.mkdir(f"Egzersizler/{item}/")
        open(f"Egzersizler/{item}/{filename}","w+")