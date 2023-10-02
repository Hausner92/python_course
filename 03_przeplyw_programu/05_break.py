# -*- coding: utf-8 -*-
# funkcja break pozwala nam przerwac dzialanie peti w wybranym przez nas momencie

# %%
for i in '0123456789':
    i = int(i)
    
    print(i,type(i))
    
# %%
for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i)
        break
# %%
for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break
    
print ('Koniec')

# %% petla bedzie nam printowac znaki do momentu napotkania spacji
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

print('Koniec')

# %% laczenie petli for z komenda else pozwoli nam tp dodac kolejna instrukcje
for char in 'kowalskij@gmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
else:
    print('Adres email nie jest poprawny')