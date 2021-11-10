# method 1
str="1234abcd"
rev=""
i=len(str)
while i>0:
    rev+=str[i-1]
    i=i-1
print(rev)




# method 2

str="1234abcd"
rev="".join(reversed(str))
print(rev)






# method 3

def reverse_str(str):
    string = ''
    lenght = len(str)
    while lenght > 0:
        string += str[ lenght - 1 ]
        lenght = lenght - 1
    return (string)
print(reverse_str('1234abcd'))


