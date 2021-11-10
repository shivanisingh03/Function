# Question 5
# Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke number jo ki 3 aur 5 ke multiples hain 
# unka sum print karega.jaisa ki niche dikhaya gya hai. Input:- 3 aur 5 ke multiples => 3, 5, 6, 9, 10 Output :-

# 3, 5, 6, 9, 10 Output :-
def function(limit):
    i=1
    sum=0
    while i<=limit:
        if i%3==0:
            sum=sum+i
            print("by 3 =",i)
        if i%5==0:
            print("by 5 =",i)
            sum=sum+i
        i+=1
    print("sum of the numbers",sum)
function(10)