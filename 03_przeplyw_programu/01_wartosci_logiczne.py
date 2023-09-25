# -*- coding: utf-8 -*-
# w pythonie mamy dwie wartosci logiczne

val_1 = True
val_2 = False

# %% koniunkcja jest prawdziwa tylko wtedy gdy obydwa elemnty są prawdziwe
True and True # tylko to nam zwróci True
True and False
False and True
False and False

# %% alternatywa jest prawdziwa wtedy kiedy tylko jeden element jest prawdziwy
True or True
True or False
False or True
False or False

# %% negacja zwraca nam wartosc przeciwną
True 
not True
False
not False

# %% przykłady wartosci jakie python interpetruje jako wartosci true or false
# funkcja bool wskazuje wartosci logiczne naszych obietkow
bool('python') # w str kazda litera wskazuje wartosc True
bool(0) # w liczbach wartosc zero wskaze nam False reszta True
bool({}) # pusty słownik zwróci nam false
bool(set()) # pusty zbior zwróci nam false
bool(list()) # pusta lista zwroci nam false
bool(tuple()) # pusta tupla zwroci nam false

bool({'key':'val'}) # zwroci nam true