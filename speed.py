# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function 
# speed naam ka ek parameter lega. 1. Agar speed 70 se kam hai to ye “ok” print 
# karega.
# Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point 
# dega (ye 70 ko count nahi karega).
# example ke liye agar speed 80 hai to print karega “points:2” .
# Agar driver ko 12 points se jyaada points milte hai to , function “License 
# suspended” print karega.

def driver(speed):
    i=0
    a=speed-70
    b=(a//5)
    if b<0:
        print("ok")
    if b>0:
        print(b,"License suspended")
    i=i+1
    return(c)
c=int(input("ennter the speed "))
print(driver(c))
        