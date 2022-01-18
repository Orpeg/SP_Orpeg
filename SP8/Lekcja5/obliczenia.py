#Liczenie silni

# n = int(input('Podaj liczbę całkowita n = '))
def silnia(x):
    if x == 0: return 1
    if x == 1: return 1
    if x > 1: return x*silnia(x-1)

#print('Silnia ', n, '! = ', silnia(n))
#print('Dla n = ', n)
#obliczamy prawdopodobienstwo

def c(a,b):
    if a<b:
        return silnia(b)/silnia(a)/silnia(b-a)
    else: return 'błąd'
print('Liczymy proawdopodobieństwo totolotka')
a = int(input('ile liczb losujesz ?'))
b = int(input('z ilu luczb? '))

print('liczymy proadopodobieństwo')
print('to jest 1 / ', c(a,b))
print('to jest ',1/c(a,b))