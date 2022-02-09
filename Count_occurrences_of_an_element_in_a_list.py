# Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
#          x = 10
# Output : 3 
# 10 appears three times in given list.

# Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
#         x = 16
# Output : 0

lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
lst2=[8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 10
x1=16

print(lst.count(x))
print(lst.count(x1))


from collections import Counter
 
# declaring the list
l = [1,1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
 
# driver program
x = 3
d = Counter(l)
print(d[x])
y=1
print(d[y])