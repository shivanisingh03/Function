 
def fun(n):
    i=2
    sum=0
    while i<n/2:
        if n%i==0:
            sum=sum+1
            break
        i=i+1
    if sum==0:
        print("prime number")
    else:
        print("not prime")
        
b=int(input("enter your number "))
fun(b)



