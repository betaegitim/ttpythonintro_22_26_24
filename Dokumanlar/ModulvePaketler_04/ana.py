# import os
# print(os.name)
# print(os.listdir("."))
#####################
# from os import name,listdir
# print(name)
# print(listdir("."))
#####################
# from os import *
# print(name)
# print(listdir())
######################
# import sys
# sys.path.append("/workspace/ttpythonintro_22_26_24/Dokumanlar/Temeller_01")
# print(*sys.path,sep="\n")
#######################
from modul import paket
print(paket.toplama(2,3))
print("Dışarıdan",paket.__name__)
# from modul.paket import toplama
# print(toplama(2,3))
# import modul as m
# print(m.paket.toplama(2,3))
# from modul import * 
# prijçjşçjçşljlçljçjçnt(paket.toplama(2,3))
# from modul.paket import *
# print(toplama(2,3))
import modul
print(modul.modulFonk(300,20))