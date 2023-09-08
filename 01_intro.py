# -*- coding: utf-8 -*-

print ('Cześć, świecie')

imie = 'Jan'
print(imie)

imie = 'Jan'
wiek =30
print(imie, wiek)

# 'end' okresla co zostanie wydrukowane na końcu ostatniej linii tekstu
# domyślnie jest to znak nowej linii "\n"
# end='' zapobiega automatycznemu przechodzeniu do nowej linii po każdym wywołaniu funkcji print().

print('Cześć, ', end='') 
print ('świecie')

# argument "sep" pozwala zmienić separator używany pomiędzy elementami
# domyslne zachowanie argumentu "sep"nie oddziela argumentów przecinkami, ale dodaje spacje między nimi

print('Cześć', 'świecie!', sep='+')

# file, pozwala na przekierowanie wydruku do innego miejsca, zamiast domyślnie na konsolę. 
# Na przykład, można przekierować wydruk do pliku

with open ('plik.txt', 'w') as f:
    print('Cześć, świecie!', file=f)

# %% 
print(2 + 2)

# %%
print(3 * 3)

# %%
print(3 + 2 * 2)
print(4 - 2 * 2)

# %% wynikiem dzielenie będzie liczba zmienno przecinkowa
10 / 3
4 / 2 

# %% dzielenie całkowite (bez liczb po przecinku)
10 // 3
7 // 6

# %% potęgowanie
2 ** 5 

# %% operator modulo zwraca reszte dzielenia np. 10 / 3
# wynikiem będzie zbiór liczb od 0 do liczby o jeden mniejszej przez którą dzielimy 
10 % 3
12 % 5
11 % 2

# %% 
(10 - 2 ** 3) * 10

# %%
a = 10
b = 20

c = a * b 
print(c)

# %%
print('love python')
"love python"

# %%
print("It's the best!")

# %%
print('It\'s the best!')

# %%
print('Python3.7')

# %% "\n3" znak nowej lini
print('Python\n3.7')

# %% """ """ formatuje tekst tak jak został przez nas napisany
print("""Python
3.7""")

# %% "\t" tworzy nam wcięcie (tab) 
print('\tPython')
print('\t\t\tPython')


# %%
print('C:\path\to\something\new')
print('C:\path\\to\something\\new')
print(r'C:\path\to\something\new')
print('C:\\path\\to\\something\\new')

# %%
import os   # importowanie biblioteki os
os.getcwd() # wywołanie sciezki katalogu roboczego

# %%
print("""
Instrukcja uruchamiania pliku przyklad.py:

    --file [nazwa pliku]
        zapisuje output do pliku
        
    --quiet
        wycisza logi w konsoli
        
Koniec.""")

# %% znakiem mnożenia wskazujemy ilosc powtórzeń tekstu
text = 'I love Python. '
print(text)
print(text * 7)
print('hau...' * 8)

# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

# %%
age = 31
imie = 'Mateusz'

print(imie + ' ' + str(age)) # funkcja "str" konwertuje podaną wartosc na string
print(imie, age)
print('{} ma {} lat'.format(imie, age))
print(f'{imie} ma {age} lat')
# %%
saldo = 40
saldo += 30
saldo -= 10

print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny

print('Wartosc lokaty po roku:', lokata_po_roku)

# %%
pixel = 150
pixel /= 255

print(pixel)

# %%
base = 2
base **= 5

print(base)

# %%
x = 103
x %= 10

print(x)

# %%
imie = 'Mateusz '
nazwisko = 'Hausner'
imie += nazwisko 

# %%
name = 'Python '
version = '3.7'
name += version

print(name)