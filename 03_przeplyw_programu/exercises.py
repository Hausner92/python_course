# -*- coding: utf-8 -*-
# %% ćwiczenie 1

print(bool(' '))
print(bool(''))
print(bool('1'))
print(bool(['', '']))

# %% ćwiczenie 2

x = 3
y = 5
z = 0

print(bool(x > y and z < y))
print(bool(x > y or z < y))

# albo

result = (x > y) and (z < y)
print(result)
 
result = (x > y) or (z < y)
print(result)

# %% ćwiczenie 3

a = 5
b = 10

print(bool(a < b and b > 0))
print(bool(a == b or b != 0))
print(bool(not(a >= b)))

# albo

c = a < b and b > 0
d = a == b or b != 0
e = not (a >= b)
 
print(c)
print(d)
print(e)

# %% ćwiczenie 4

number = 10

if number > 0:
    print('The number is greater than zero.')

# %% ćwiczenie 5

number = 5

if number > 0:
    print(f'The number {number} is positive.')
elif number < 0:
    print(f'The number {number} is negative.')
elif number == 0:
    print(f'The number {number} is equal to zero.')
    
# %% ćwiczenie 6

number = 7

if number % 2 == 0:
    print('The number', number, 'is even')
else:
    print('The number', number, 'is odd.')
    
# %% ćwiczenie 7

year = 2024
# Jeśli rok jest podzielny przez 4 i nie jest podzielny przez 100, lub jest podzielny przez 400, to jest to rok przestępny.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('The year', year, 'is a leap year.')
else:
    print('The year', year, 'is not a leap year.')

# %% ćwiczenie 8

category = 'electronics'
price = 2000

if category == 'electronics':
    if price > 1000:
        VAT = price * 0.23
    else:
        VAT = price * 0.08
elif category == 'clothing':
    VAT = price * 0.23
else:
    VAT = price * 0.21
    
print('The VAT for a product is', VAT, 'PLN.')

# %% ćwiczenie 9

velocity = 55

if velocity > 50:
    print('Slow down!')
else:
    print('Keep it up!')
    
# %% ćwiczenie 10

category = 'crime'
quantity = 5
book_price = 100

if category == 'crime':
    if quantity >= 5:
        book_price = book_price - (book_price * 0.20)
    elif quantity >= 3:
        book_price = book_price - (book_price * 0.10)
    else:
        book_price
elif category == 'fantasy':
    if quantity >= 10:
        book_price = book_price - (book_price * 0.25)
    elif quantity >= 5:
        book_price = book_price - (book_price * 0.15)
    else:
        book_price
else:
    if quantity >= 20:
        book_price = book_price - (book_price * 0.10)
    elif quantity >= 10:
        book_price = book_price - (book_price * 0.05)
    else:
            book_price

    
print('The total price after the discount is', book_price, "PLN.")

# albo

category = 'crime'
quantity = 5
book_price = 100

if category == 'crime':
    if quantity >= 5:
        discount = 0.2
    elif quantity >= 3:
        discount = 0.1
    else:
        discount = 0
elif category == 'fantasy':
    if quantity >= 10:
        discount = 0.25
    elif quantity >= 5:
        discount = 0.15
    else:
        discount = 0
else:
    if quantity >= 20:
        discount = 0.1
    elif quantity >= 10:
        discount = 0.05
    else:
        discount = 0
 
final_price = book_price * (1 - discount)
print(f'The total price after the discount is {final_price} PLN.')

# %% ćwiczenie 11

fact = 'Python is easy and enjoyable'
unique_characters = set(fact)
number_of_unique_characters = len(unique_characters)

if number_of_unique_characters < 20:
    print('There are less than 20 unique characters.')
else:
    print('The number of unique characters is greater than or equal to 20.')
    
# %% ćwiczenie 12

text = 'sfdvjklncdnskjccbnksjdnckjsdsnckjnsdkjnckjsnkjlcnqdlknwsx'

if 'q' in text:
    print('The text contains the letter "q".')
else:
    print('The text does not contain the letter "q".')
    
# %% ćwiczenie 13

height = 1.85
weight = 85

BMI = weight / (height ** 2)
print(f'The patient\'s BMI is: {BMI:.2f}') # zaokraglenie BMI do dwoch miejsc po przecinku

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI < 25:
    print('Normal weight')
elif BMI >= 25 and BMI < 30:
    print('Overweight')
elif BMI >= 30:
    print('Obese')

# %% ćwiczenie 14

password = 'my_password_123'

if len(password) < 8:
    print('The password is too short.')
elif not any(char.isdigit() for char in password):
    print('The password must contain at least one digit.')
elif not any(char.isupper() for char in password):
    print('The password must contain at least one uppercase letter.')
elif not any(char.islower() for char in password):
    print('The password must contain at least one lowercase letter.')
else:
    print('The password is complex enough.')
        










