# -*- coding: utf-8 -*-
# tuple to uporządkowana struktura której nie można zmieniać
# raz wpisane wartosci do tupli pozostają niezmienione

empty_tuple = tuple()
print(empty_tuple)

# %% tuple można też zdefiniować za pomocą nawiasów okrągłuch 
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

# %%
name_google = google [0]

# %% tupla zagnieżdżona 
data = (amazon, google)
print(data)

# %%
a = ('Mateusz', 'Hausner')
print(a)

# %% 
imie = 'Mateusz'
nazwisko = 'Hausner'

# %%
imie, nazwisko, id_user = ('Mateusz', 'Hausner', '001')

# %% rozpakowywanie tupli
amazon_name, country, sector, rank = amazon

# %% tuple można zdefiniować w kolejny sposób 
stocks = 'Amazon', 'Apple', 'IBM'

print(type(stocks))

# %% 
nested = 'Europa', 'Polska', ('Warszawa', 'Krakow', 'Wroclaw')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b)

# %%
x, y = 10, 15
x, y = y, x
print(x ,y)