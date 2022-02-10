# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]

# Input: list2 = [12, 14, 95, 3]
# Output: [12, 14]

# l=[2, 7, 5, 64, 14]
# even=[ele for ele in l if ele%2==0]
# print(str(even))
# odd=[ele for ele in l if ele%2==1 ]
# print(str(odd))

n=10
even_list=[ele for ele in range(n) if ele%2==0]
print(even_list)

odd_list=[ele for ele in range(n) if ele%2==1]
print(odd_list)


even_count=0
even_count=[ele for ele in range(n) if ele%2==0]
print(len(even_count))
