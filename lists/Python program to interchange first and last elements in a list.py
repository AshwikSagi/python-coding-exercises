# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

newList = [1, 2, 3]
def swapList(newList):
     
    newList[0], newList[-1] = newList[-1], newList[0]
 
    return newList
output=swapList(newList)
print(output)

