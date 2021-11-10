

def string(str):
    # str=input("enetr the txt ")
    upper=0
    lower=0
    for i in str:
        if (i.islower()):
            lower+=1
        elif (i.isupper()):
            upper+=1
    print("the lower case letter :",lower)
    print("the upper case latter ;",upper)
st=input("enetr the txt ")
string(st)
