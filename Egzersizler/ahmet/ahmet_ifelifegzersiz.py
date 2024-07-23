"""
Bir e-ticaret sitesinden alışveriş yapan bir kullanıcının sipariş tutarına göre kargo ücretini hesaplayan bir program yazınız.

Koşullar:

* 0 TL - 100 TL arası siparişler için 15 TL kargo ücreti
* 100 TL - 200 TL arası siparişler için 10 TL kargo ücreti
* 200 TL ve üzeri siparişler için ücretsiz kargo

"""

sip_tutari=input("sipariş tutarı=")
if sip_tutari.isdigit():
    sip_tutari=int(sip_tutari)
    if 0<sip_tutari<=100:
        print("kargo ücreti 15 TL ")
    elif 100<sip_tutari<=200:
        print("kargo ücreti 10 TL ")
    else: 
        print("ücretsiz kargo") 
else:
    print("hatalı giriş")
