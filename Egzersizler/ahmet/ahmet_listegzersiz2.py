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
liste=[41, 63, 100, 34, 12, 62, 90, 47, 52]
liste.append(100) 
print(liste)
liste.pop(2)
liste[1]=100*liste[1]
print(liste)
liste.sort(reverse=True)
print(liste)
liste.reverse()
print(liste)