# coding: utf-8
#sypder
#zmienne
a = 2
b = 3
print(a)
print(b)
suma = a+b
print(sum)
print(suma)
print(a+b)
print('a+b')
#string, łańcuch
print(f' zmienna a = {a} , b = {b}, suma = a+b = {a+b}')
a,b
#krotka
a,b = b,a
a,b
tem = a
a = b
b = tem
a
b
a,b
c
c = 3
b
c
b ==3
c == 3
a == 3
c==b
0 and 1
0 or 1
bool(0 and 1)
0 and 1
bool(0 and 1)
bool(0 or 1)
#zmienne liczbowe
#inteer
2,3,4,5
2/3
#float
x = int(input('podaj liczbe całkowita  '))
x
y = float(input('podaj liczbę zmiennoprzecinkowa   '))
y
y = float(input('podaj liczbę zmiennoprzecinkowa   '))
y
x = int(input('podaj liczbe całkowita  '))
y
y = float(input('podaj liczbę zmiennoprzecinkowa   '))
y
int(y)
y = 3.56
y
int(y)
round(y,0)
('Janek', 'Małgosia', 'Zosia')
d = ('Janek', 'Małgosia', 'Zosia')
c = ('mechanik', 'sekretarka', 'kucharka')
c
zip(a,c)
zip(d,c)
for i, v in zip(d,c):
    print(f'{i}, {v})
for i, v in zip(d,c):
    print(f'{i}, {v}')
    
for i, v in zip(d,c):
    print(f'{i} jest naszym, {v}')
    
for i, v in zip(d,c):
    print(f'{i} jest naszym {v}')
    
#lista
numbers = [15,63,24,37,48,4,26,7,83,15,40,3,47,67,81,77,81,10,77,86]
numbers
c
d
imiona = list(d)
imiona
zawody = list(c)
zawody
#append
imiona.append('Dawid')
imiona
zawody.append('informatyk')
zawody
zawody.pop()
imona.pop()
imiona.pop()
imiona
numbers
max(numbers)
min(numbers)
sum(numbers)
imiona
imiona[0]
imiona[1]
len(imiona)
#długoośc listy len
imiona
imiona[-1]
imiona[-2]
imona[1]
imiona[1]
napis = 'Jedzie pociąg z daleka'
napis[::1]
#metody
napis.lower()
napis.upper()
napis.title()
napis[::-1]
napis[::2]
len(napis)
napis[1:10:1]
napis[1:10:1]
napis[1:20:2]
napis
napis.startswith('Jedzie')
napis.startswith('samochod')
napis.endswith('daleka')
#for
for i in range(1, 20,2):
    print(i)
    
for i in range(1, 20,3):
    print(i)
    
for i in range(20):
    print(i, end=', ')
    
#while
i = 1
while i<10:
    print(f'zmienna i = {i}')
    i = i+1
    
while i<=10:
    print(f'zmienna i = {i}')
    i = i+1
    
i = 0
while i<=10:
    print(f'zmienna i = {i}')
    i = i+1
    
