
def calculater(x,y,z):
    if z=="+":
        return(x+y)
    elif z=="-":
        return(x-y)
    elif z=="*":
        return(x*y)
    elif z=="%":
        return(x%y)
    elif z=="/":
        return(x/y)
s=calculater(1,2,"+")
print(s)
b=calculater(40, 3, "-")
print(b)
c=calculater(10, 4, "*")
print(c)
d=calculater(40, 4, "/")
print(d)
e=calculater(40, 4, "%")
print(e)