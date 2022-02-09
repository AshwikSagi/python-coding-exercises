test_list = [ 1, 6, 3, 5, 3, 4 ]
a=4
# for i in range(len(test_list)):
#     if i==a:
#         print("Element Exists")

if a in test_list:
    print("Element Exists")



test_list = [10, 15, 20, 7, 46, 2808]
 
print("Checking if 15 exists in list")
 
# number of times element exists in list
exist_count = test_list.count(15)
 
# checking if it is more then 0
if exist_count > 0:
    print("Yes, 15 exists in list")