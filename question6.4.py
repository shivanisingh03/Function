# Question 6
# Ek function define kijiye jo ki drivers ki speed check karega. Aur ye function speed naam ka ek parameter lega. 1. Agar speed 70 se 
# kam hai to ye “ok” print karega.
# Agar driver ki speed 70 se jyaada hai to function use har 5 km ke liye 1 point dega (ye 70 ko count nahi karega).
# example ke liye agar speed 80 hai to print karega “points:2” .
# Agar driver ko 12 points se jyaada points milte hai to , function “License suspended” print karega.

def function(speed):
    i=0
    while i<=250:
        if speed<70:
            print("ok")
        if speed>70:
            print("high")
        i+=1
        return(i)
function()

