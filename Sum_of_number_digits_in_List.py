# The original list is : [12, 67, 98, 34]
# List Integer Summation : [3, 13, 17, 7]



def IntegerSum(l):
    a=[]
    for i in range(len(l)):
        
        div=l[i]/10
        rem=l[i]%10
        result=div+rem
        a.append(result)
    return a
        

l=[12, 67, 98, 34]
k=IntegerSum(l)
print(list(k))