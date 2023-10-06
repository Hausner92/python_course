# -*- coding: utf-8 -*-

# Funkcja  open(file, mode) pozwala otworzyć plik i zwraca go jako obiekt.
#'r' - read - otwiera plik do odczytu, zwraca błąd jeśli plik nie istnieje
#'a' - append - otwiera plik do dopisania, tworzy plik jeśli nie istnieje
#'w' - write - otwiera plik do zapisu, tworzy plik jeśli nie istnieje
# pierwszy parametr jest nazwa pliku z ktorym bedziemy pracowac, drugi parametr okresla co chcemy zrobic

file = open('simple.txt', 'r') # otworzylismy plik, 'r' tryb odczytu

for line in file:              # odczytalismy wzystko z pliku
    print(line, end='')        # end= '' usuwa nam pustą linie miedzy tekstem
    
file.close()                   # zamykamy plik, nie ruszamy go dalej

# %%
with open('simple.txt', 'r') as file:   #otwarcie pliku i przypisanie go do zmiennej
    for line in file:
        print(line, end='')
        
# %% metoda 'readline()' pozowli nam przeczytac pierwsza linie naszego pliku
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)
    
# %% metoda 'readlines()' odczytuje wszystkie linie naszego pliku, i zwroci nam liste
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    
# %% tworzymy petle ktora przechodzi po liniach i je nam printuje
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
        
# %% do metody readline dodaje petle while
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# %%
with open('simple.txt', 'r') as file:
    lines = file.read() # metoda read pozowli nam odczytac wszystko co jest w naszym pliku
    print(lines)
