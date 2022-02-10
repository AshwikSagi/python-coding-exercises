# Input : list = [10, 11, 12, 13, 14, 15]
# Output : [15, 14, 13, 12, 11, 10]

# Input : list = [4, 5, 6, 7, 8, 9]
# Output : [9, 8, 7, 6, 5, 4]

l=[10, 11, 12, 13, 14, 15]
print(l[::-1])


def Reverse(lst):
    return [ele for ele in reversed(lst)]
      
# Driver Code
lst = [10, 11, 12, 13, 14, 15]
r=list(reversed(lst))
print(Reverse(lst))
print(r)
