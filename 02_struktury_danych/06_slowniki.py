# -*- coding: utf-8 -*-
# zdefinowanie pustego słownika
emply_dict = dict()
print(emply_dict)

# słownik możemy również zdefiniować po przez nawias "{}"
d = {}
print(type(d))

e = set()

# %% słownik jest struktrurą która jest nie uporządkowana
# klucze w słowniku nie mogą się powtarzać każdy klucz ma jedną wartosc
pol_to_eng = {'jeden':'one', 'dwa':'two', 'trzy':'three'}

name_to_digit = {'jeden':1, 'dwa':2, 'trzy':3}

# %%
name_to_digit = {0:1, 1:2, 2:3}
# len zwróci nam ilosc elementów w naszym słowniku
len(name_to_digit)

# %% struktura zapisu słownika
# dict = {'key1':'value1', 'key2':'value2'}

# %% wstawianie nowych elementów do słownika
pol_to_eng['cztery'] = 'four'

# %% metodą clear usuniemy wszystkie elementy ze słownika
pol_to_eng.clear()

# %% metodą copy kopiujemy słownik
pol_to_eng_copied = pol_to_eng.copy()

# %% metoda keys wyrzuci wszystkie klucze z naszego słownika
pol_to_eng.keys()
list(pol_to_eng.keys()) # przeformatowanie na listę
# %% values wyrzuci nam liste wartosci
pol_to_eng.values()
list(pol_to_eng.values())

# %%  items wydobywa zarówno klucze jak i ich wartosci
# dostaniemy dwie połączone struktry danych czyli listę tupli
# pary klucz wartosc nie możemy zmienić, 
# ale mozemy wyrzucic jeden element zawierający taką parę 
pol_to_eng.items()
list(pol_to_eng.items())

# %%
pol_to_eng['jeden']

# %% 
pol_to_eng.get('jeden')
pol_to_eng.get('zero', 'NaN')

# %% metoda pop wyrzuca wartosc dla podanego klucza i usuwa pare ze słownika
# pol_to_eng.pop('dwa')
pol_to_eng.popitem() # zwróci nam klucz i wartosc i usunie je ze słownika

# %% metoda update pozwoli nam nadać nowe wartosci dla kluczy
pol_to_eng.update({'dwa':2}) 