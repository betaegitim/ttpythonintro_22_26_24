
# with open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/datasrc.csv","r+") as dosya,\
#     open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data1.csv","a") as d1,\
#         open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data2.csv","a") as d2: 
#     liste = dosya.readlines()
#     for i in range(len(liste)):
#         print(liste[i])
#         a,b,c,d = liste[i].split(",")
#         print(",".join((a,c,d)),file=d1,end="")
#         print(",".join((a,b,c)),file=d2)

import string


def dogru_email_mi(email):
  if "@" not in email:
    return False
  kullanici_adi, alan_adi = email.split("@")
  if len(kullanici_adi) < 1 or len(alan_adi) < 3:
    return False
  if "." not in alan_adi:
    return False
  alan_adi_parcalari = alan_adi.split(".")
  for parca in alan_adi_parcalari:
    if not parca or len(parca) > 63:
      return False
  return True

def turkce_cep_telefonu_mu(numara):
  # Numaranın boş olup olmadığını kontrol edin.
  if not numara:
    return False
  numara  = numara.replace(" ","")
  # Numaranın sadece sayısal karakterlerden ve + sembolünden oluşup oluşmadığını kontrol edin.
  gecerli_karakterler = string.digits + "+"
  for karakter in numara:
    if karakter not in gecerli_karakterler:
      return False
  # Numaranın uzunluğunun 10 olup olmadığını kontrol edin.
  if len(numara) > 15:
    return False
  # Numaranın başında 5 veya 9 olup olmadığını kontrol edin.
  if numara[0] not in ["5", "9","+"]:
    return False
  return True
  # Numaranın formatını kontrol edin (5xx xxx xxxx veya 9xx xxx xxxx)
#   if numara[1:4].isdigit() and numara[5:].isdigit():
#     return True
#   else:
#     return False

d1 = open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data1.csv","r+")
d2 = open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data2.csv","r+")

l1 = d1.readlines()
l2 = d2.readlines()
baslik = (l1[0],l2[0])
l1 = l1[1:]
l2 = l2[1:]
result = []
for item in l1:
    a,b,c = item.split(",")
    if not dogru_email_mi(c):
        c = "NaN\n"
    result.append(",".join((a,b,c)))
result.insert(0,baslik[0])
d1.seek(0)
d1.truncate()
d1.writelines(result)
d1.close()


result = []
for item in l2:
    a,b,c = item.split(",")
    if not turkce_cep_telefonu_mu(b):
        b = "_"
    result.append(",".join((a,b,c)))
result.insert(0,baslik[1])
d2.seek(0)
d2.truncate()
d2.writelines(result)
d2.close()


with  open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data1.csv","r+") as d1,\
    open("/workspace/ttpythonintro_22_26_24/Workshop/25072024/data2.csv","r+") as d2:
    l1 = d1.readlines()
    l2 = d2.readlines()
    baslik = (l1[0],l2[0])
    l1 = l1[1:]
    l2 = l2[1:]
    for i in range(len(l1)):
        a1,b1,c1 =l1[i].split(",")
        a2,b2,c2 =l2[i].split(",")
        if b1 == c2.replace("\n",""):
            rec = [a1,b1,c2.replace("\n",""),c1]
            print(";".join(rec),file=open("datasonuc.csv","a+"),end="")
        else:
            print(b1,c2)
