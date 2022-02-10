# Input: list1 = [12, -7, 5, 64, -14]
# Output: 12, 5, 64

# Input: list2 = [12, 14, -95, 3]
# Output: [12, 14, 3]


l=[12, -7, 5, 64, -14,-28]
positive_list=[ele for ele in l if ele>0]
positives=list(filter(lambda x:x>0 , l))
print(positives)
print(positive_list)


l=[12, -7, 5, 64, -14,-28]
negatives=list(filter(lambda x:x<0 , l))
negative_list=[ele for ele in range(-10,10,2) if ele<0]
print(negative_list)
print(len(negative_list))
print()
print(negatives)








