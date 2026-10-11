# Program 7: Combining lists

list1 = [10, 11, 12, 13, 14, 15]
list2 = [20, 21, 22, 23, 24, 25]

combinedList =[]
for i in range(len(list1)):
    if(list1[i]%2 != 0):
        combinedList.append(list1[i])

for i in range(len(list2)):
    if(list2[i]%2 == 0):
        combinedList.append(list2[i])

print("List1: ", list1)
print("List2: ", list2)
print("Combined list: ", combinedList)        
