# Question 4
# Ek showNumbers() naam ka function define kijiye jo ki ek limit naam ka parameter lega aur 0 se limit tak ke beech ke sabhi even 
# aur odd numbers ko label ke saath print karega jaisa ki niche dikhaya gaya hai. For example :- Input:- Output :-


def showNumbers(limit):
    i=0
    a=[]
    b=[]
    while i<=limit:
        if i%2==0:
            print(i,"evrn")
            # a.append(i)
        else:
            print(i,"odd")
            # b.append(i)
        i+=1
    print(i)
    # print(a)
    # print(b)
showNumbers(100)


