# -*- coding: utf-8 -*-

text = 'Witaj na kursie Pythona. \nPython jest wspaniały.'

print(text)

# %% wyrzucenie wszystkich dostępnych metod
dir(text)
help(str.count) #opis funkcji, jakie parametry przyjmuje

# %% zwrócenie tekstu z dużą literą tylko na początku
text.capitalize()

# %% zwrócenie tekstu z dużą literą tylko na początku każdego wyrazu
text.title()

# %% zwrócenie liczby danego ciągu w tekscie
text.count('Python')

# %% wskazuje od jakiego ciągu nasz tekst ma się zaczynać (zwrócenie wrt logicznej)
text.startswith('kurs')

# %% 
'python'.startswith('py')

# %%  wskazuje od jakiego ciągu nasz tekst ma się kończyć (zwrócenie wrt logicznej)
text.endswith('y.')

# %%
'sample.txt'.endswith('.py')

# %%
'sample.png'.endswith('.png')

# %% zwróci nam numer indeksu w którym dany ciąg się znajduje/zaczyna 
text.find('Python')
text[16:]

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %% sprwadza nam czy tekst ma znaki alfanumeryczne 
'Mateusz!'.isalnum()

# %% sprwadza nam czy wszystkie znaki są cyframi
'43434'.isdigit()

# %% sprawdzenie czy wszystkie litery są  małe lub duże
'python'.islower()

'MATEUSZ'.isupper()

# %% łączy tekst przy pomocy wskazanego znaku przy pomocy listy
' ' .join(['python', '3.7'])
'#'.join (['sport', 'gym', 'fit'])
','.join(['1','2', '3', '4'])

# %% pozwala zastpiąc dane w tekscie
'#good#time#mood'.replace('#', ' ')

# %%
'column name'.replace(' ', '_')

# %% wycinanie białych znaków w obrębie tekstu
'   python   '.strip()
'   python   '.rstrip() # wycięcie białych znaków po prawej stronie
'   python   '.lstrip() # wycięcie białych znaków po lewej stronie

# %% rozdzielenie łańcucha znaków na listę elementów według okreslonego separatora
'1,2,3,4,5'.split(',')

'python java php sql sas'.split()

'#gym#fit#mood'.split('#')

# %% wypełnia wartosci odpowiednią liczbą zer
'12'.zfill(5)

# %%
'hello'[1:]
