# Question 1
# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote de sakta hai ya nahi. ( Consider minimum age of 
# voting to be 18. ) Example:- Agar user input me 18 se kam deta hai to “not eligible “ print kare aur agar user 18 ya 18 se jyaada 
# input kare to “you are eligible” print kare. Input:-  Output :-

def eligible_for_vote(a):
    if x<18:
        print("not eligible ")
    elif x>=18:
        print(" eligible")
x=int(input("enter the age"))
eligible_for_vote(x)
