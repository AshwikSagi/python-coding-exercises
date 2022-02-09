# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

#G replace with e and e replace with G

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
result=[i.replace('G',"-").replace("e","G").replace("-","e") for i in test_list]
print(result)

res = ", ".join(test_list)
res = res.replace("G", "_").replace("e", "G").replace("_", "e").split(', ')
print(res)

