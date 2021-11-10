def fac(n):
    f=1
    i = 0
    while i<n:
        f=f*n
        i = i+1
    return fac
print(fac(n=int(input("enetr you number"))))