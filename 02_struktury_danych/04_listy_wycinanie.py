# -*- coding: utf-8 -*-

index = [0, 1, 2, 3, 4, 5]
lista = [34, 23, 56, 24, 23, 76]
idx_n = [-6, -5, -4, -3, -2, -1]

# %%
# konwencja wycinania listy lista[start:stop]
# lista[nr indexu] wycięcie pojedynczego elemntu listy o wskazanym indexie
# lista [start:] wycinanie od wskazanego elemntu do końca
# lista [:stop] od początku do wskazanego indexu
# lista [::step] wartosc step okresla nam co który elemnt zostanie wycięty

lista[0]
lista[1]
lista[-1] # wycianine od końca
lista [-3]

# %% lista[start:stop] od do wskazango indexu
lista[1:5]
lista[-5:-1]
lista[::-1] # przechodzenie od końca listy

# %%
lista[:4]
lista[3:]

# jeżeli indeksujemy od lewej to zaczanmy od 0
# jeżeli indeksujemy od prawej (czyli z liczbami ujemnymi) zaczyanmy od -1