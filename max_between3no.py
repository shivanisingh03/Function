# Write a Python function to find the Max of three numbers. 
def function(num1,num2,num3):
    if num1>=num2 and num2>=num3 and num1!=num2:
        print(num1,"is greatest")
    elif num2>=num3 and num2>=num1 and num2!=num3:
        print(num2,"is greatest")
    elif num3>=num1 and num3>=num2 and num3!=num1:
        print(num3,"is greatest")
    elif num1==num2==num3:
        print(num1,num2,num3,"is equal")
    return(num1,num1,num3)
num1=int(input("enetr number"))
num2=int(input("enetr number"))
num3=int(input("enetr number"))
function(num1,num2,num3)
# print(a)