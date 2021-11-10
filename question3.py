# Question 3
# Ek function banaiye jo 3 numbers ka sum aur average print kare.Hum user se 3 number input karwayenge aur fir unn 3 numbers ka sum 
# aur average print karwayenge jaisa ki niche output diya hua hain.

def sum_average():    
    i=0
    sum=0
    while i<3:
        num=int(input("ener the num"))
        sum=sum+num
        i+=1
    average=sum//3
    print(average)
    return(average)
sum_average()





def sum(*a):
    i=0
    sum=0
    while i<=3:
        sum=sum+i
        i+=1
    avrage=sum/3
    print(sum)
    print(avrage)
    return(sum,avrage)
sum(1,2,3)