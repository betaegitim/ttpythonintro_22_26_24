"""
Bir e-ticaret sitesinden alışveriş yapan bir kullanıcının sipariş tutarına göre kargo ücretini hesaplayan bir program yazınız.

Koşullar:

* 0 TL - 100 TL arası siparişler için 15 TL kargo ücreti
* 100 TL - 200 TL arası siparişler için 10 TL kargo ücreti
* 200 TL ve üzeri siparişler için ücretsiz kargo

"""

tutar=input("Sipariş Tutarınız ? : ")

if tutar.isdigit():
    fiyat=int(tutar)
    if fiyat<=100: kb=15
    elif fiyat<=200: kb=10
    elif fiyat > 200: kb =0

else: print("Geçerli değer giriniz")

print("Kargo Bedeli: ",tutar," TL")


