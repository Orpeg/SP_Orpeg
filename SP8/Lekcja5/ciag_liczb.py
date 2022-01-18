# Liczymy sume wyrazow ciągu liczbowego

# Ciąg zdefiniowany jest wzrorem a(n) = n/(n+1), dla n>0, gdzie n jest liczbą całkowita

def a(n):
    return (n/(n+1))
k = int(input('podaj liczbe wrazow ciagu k ='))


def suma(k):
    s = 0
    for e in range(1,k+1):
        s+=a(e)
    return s
print('suma ', k, ' wyrazów ciągu a(n) = n/(n+1) = ', suma(k))