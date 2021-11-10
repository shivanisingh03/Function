# multiplication_table

def table(number,limit):
    while number<=limit:
	    j = 1
	    while j<=10:
	        print(number,"* ",j,"=",number*j)
	        j = j+1
	    number = number+1
table(number=int(input("enter a number")),limit=int(input("enter number")))







