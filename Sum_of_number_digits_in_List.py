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
result=list(map(lambda ele : sum(int(sub) for sub in str(ele)),l))
# res =list(map(lambda ele : sum(int(sub) for sub in str(ele)),l))

print(str(result))

# Input :  list1 = [1, 2, 3] 
# Output : 6 
# Explanation: 1*2*3=6 



