# -*- coding: utf-8 -*-

# %% petla while bedzie odtwarza póki nie zostanie spelniony wskazany warunek
i = 0
while i < 5:
    print(i)
    
# %%
i = 0
while i < 5:
    print(i)
    i = i + 1
    
# %%

n = 0
while True:
    print(n)
    if n >= 10:
        break
    n = n + 1
    
# %%
while True:
    name = input('Podaj swoje imie: ')
    if len(name) >= 3 and name.isalpha: # spr. czy dl. imienia jest wieksza badz rowna
        break                           # 3 i czy są to znaki alfanumeryczne(litery, cyfry)
print('Czesc {}' .format(name))

# %%
n = 0

while n < 20:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
    
# %% szukamy elementu czy wystepuje w naszym obiekcie
lista_do_przeszukania = [12, 53 ,13, 63, 34]
flaga = False

idx = 0 
while idx < len(lista_do_przeszukania):
    print(lista_do_przeszukania[idx])
    idx += 1
    
# %%
lista_do_przeszukania = [12, 53 ,13, 63, 34]
flaga = False
wartosc = 63

idx = 0 
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}' .format(wartosc))
    
# %% szukamy elementu w liscie a jak go nie ma to go dodamy
lista_do_przeszukania = [12, 53 ,13, 63, 34]
flaga = False
wartosc = 60

idx = 0 
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)

