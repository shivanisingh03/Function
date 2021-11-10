# Question 2
# Ek perfect() naam ka function define kijiye jo ki ek parameter lega aur uss parameter ko hume check karana hai ki vo perfect number
#  hain ya nahi. Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print kare.
# [ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors ( including 1 & excluding itself) ka sum uss number 
# ke barabar hota hai. Example:- Expected Output :- 

def perfect_number(n):
    sum=0
    i=1
    while i<n:
        if n%i==0:
            sum=sum+i
        i+=1
    return sum==n
a=int(input("enter the number"))
print(perfect_number(a))



