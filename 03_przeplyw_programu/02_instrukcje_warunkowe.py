# -*- coding: utf-8 -*-
# %%
version = 3.7

print(version)

# %% sprawdzamy warunek logiczny
version > 3
version <= 3

# %%
number = 1200
number > 1000
number == 1200
number == 1000 # operator porównania 
number != 1200 # sprawdza czy liczba jest różna od 1200
number != 1000 

# %% składnia instrukcji warunkowej
if [warunek]:
    [instrukcja]
    
# %%
if 8 < 10:
    print('Tak')
    
# %%
a = 15
if a > 10:
    print('a > 10')
    
# %%
a = 5
if a > 10:
    print('a > 10')
else:
    print('a <= 10')
    
# %%
age = 18
if age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostęp przyznany.')
    
# %% kilka testów logicznych w jednej instrukcji
age = 18
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
else:
    print ('Dostęp przyznany')
    
# %% 
# korzystamy z funkcji int w celu zmiany tekstu na liczbę ponieważ input przyjmuje nam tylko stringi
age = int(input('Podaj swój wiek: ')) 
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
elif age > 18:
    print ('Dostęp przyznany')
    


    
    
    
    
    
    
    
    
    
    
    