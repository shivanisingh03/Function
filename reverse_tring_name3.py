srting = "shahnaaz Naazmeen"
i = 0
b=srting.split()
print(b)
rev="  "
l=len(b)-1
while i <= l:
    rev=rev+b[l]+" "
    l-=1
print(rev)