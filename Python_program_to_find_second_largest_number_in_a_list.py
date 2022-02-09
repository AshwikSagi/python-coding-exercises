# Input: list1 = [10, 20, 4]
# Output: 10

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70

l=[70, 11, 20, 4, 100]


largest=l[0]

for i in range(len(l)):
    if(l[i]>largest):
        largest=l[i]
second_largest=l[0]
for i in range(len(l)):
    if(l[i]>second_largest and l[i]<largest):
        second_largest=l[i]
print(second_largest)

