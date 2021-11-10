
#  Question 7
# Ek function define karo jo ki input me 2 strings lega aur dono strings me se 
# jiski length jyaada hogi use print karega aur agar dono strings ki length equal 
# hui to dono ko line by line print karega . Hint :- use len() builtin function.. 
# Input:- Output :-
def sss(a,b):
    c=len(a)
    d=len(b)
    if c>d:
        print(a)
    if c<d:
        print(b)
    if c==d:
        print(a,b)
sss("hello","welcome")
sss("sonu","monu")
