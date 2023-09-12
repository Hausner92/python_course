# -*- coding: utf-8 -*-

imie = 'Mateusz'
_imie = 'Olek' # zmienna która się nie zapisze w "variable explorer" nie ruszać

imie_3 = 'Ala'

# %%
a = 8
b = 20
c = a * b
print(c)

# %%
przepracowane_godziny = 8
stawka_godzinowa = 20

dzienna_pensja = przepracowane_godziny * stawka_godzinowa
print(dzienna_pensja)

# %% style pisowni kodu
camelCase = 'Python 3.7'   # każdy nowy wyraz z dużej liter (poza pierwszym)
PascalCase = 'Python 3.7'  # pierwsze litery duże
snake_case = 'Python 3.7'  # wyrazy oddzielone "_" używamy do nazywania metod i zmiennych
kebab-case = 'Python 3.7'  # wyrazy oddzielone "-"
UPPER = 'Python'           # wszystkie duże litery, używany do przechowywania stałych (wartosci które się nie zmieniają podczas uruchamiania programu)

# %% lista nazw któruch nie należy nazywac jako nazwy zmiennych (zarezerwowane dla Pythona)
import keyword
keyword.kwlist

