# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]

# Input: list2 = [12, 14, 95, 3]
# Output: [12, 14]

l=[2, 7, 5, 64, 14]
res=[ele for ele in l if ele%2==0]
print(str(res))


