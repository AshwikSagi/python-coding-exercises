# Input: [12, 15, 3, 10]
# Output: Remove = [12, 3], New_List = [15, 10]

# Input: [11, 5, 17, 18, 23, 50]
# Output: Remove = [1:5], New_list = [11, 50]

l=[12, 15, 3, 10]
r=[12,3]
output=[ele for ele in l if ele not in r]
print(output)
