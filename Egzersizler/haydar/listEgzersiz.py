"""
`liste = [41, 63, 100, 34, 12, 62, 90, 47, 52]`<br>
yukarıda yer alan liste için;<br>
1. listenin sonuna 1000 sayısını ekleyiniz
2. listenin 2. indisinde yer alan sayıyı siliniz
3. listenin 1. indisinde yer alan sayıyı 100 katı ile güncelleyiniz
4. listeyi büyükten küçüğe sıralayınız.
5. listeyi tersine çevirerek ekrana yazdırınız
Beklenen sonuç:
[]
"""

liste = [41, 63, 100, 34, 12, 62, 90, 47, 52]
liste2=liste
liste3=[1000]
print("Orijinal Liste: ",liste)
liste.append(1000)
print("1. cevap      : ",liste)
liste.pop(2)
print("2. cevap      : ",liste)
liste[1]=liste[1]*100
print("3. cevap      : ",liste)
liste.sort(reverse=True)
print("4. cevap      : ",liste)
liste2.reverse()
print("5. cevap      : ",liste2)