test_list = [5, 6, [], 3, [], [], 9]
output=[ele for ele in test_list if ele!=[]]
print(output)
result=list(filter(lambda x:x!=[] ,test_list))
print(result)