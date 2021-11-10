def function(list):
    i=0
    sum=list[i]
    while i<len(list):
        j=list[i]
        if j>sum:
            sum=j
        i+=1
        # print(sum)
    return(sum)
a=function([2,4,8])
print(a)