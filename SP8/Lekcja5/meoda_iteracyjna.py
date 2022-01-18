# zakłądamy, że liczymy silnię iteracyjne
n = int(input('podaj liczbe całkowitą n = '))

silnia = 1
for i in range(1, n+1):
    if n == 0: break
    else: silnia*=i
print('silnia ', n, '! = ', silnia)
