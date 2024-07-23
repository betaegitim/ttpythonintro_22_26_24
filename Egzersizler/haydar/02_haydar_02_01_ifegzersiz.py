"""
 Kullanıcıdan yaş bilgisinin alınarak 18 yaşından büyük ise ekrana oy kullanabilir ifadesinin yazılmasını sağlayan python kodunu yazınız"

"""


yas=int(input("Yasiniz : "))

if yas>=18:
   print(yas," yaşındasınız, Oy Kullanabilirsiniz.")
else:
   print(yas,"yaşındasınız, 18 yaşından küçükler oy Kullanamaz!")

