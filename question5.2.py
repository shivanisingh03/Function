# Question (Part 2)
# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare ki same index 
# waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo. Agar 
# aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:
def check_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print(list1[i],list2[i],"even")
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

def check_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        if list1[i]%2==0 and list2[i]%2==0:
            print(list1[i],list2[i],"even")
        else:
            print(list1[i],list2[i],"odd")
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])

