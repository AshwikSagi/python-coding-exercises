# The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]]
# The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}

l=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
d={}
for ele in l:
    d[tuple(ele[:2])]= tuple(ele[2:])
    
print(str(d))
