# Program 5
listNums = []

for i in range(5):
    listNums.append(int(input("Enter a number: ")))

totalSum = sum(listNums)

print("List: ", listNums)
print("Sum of list elements: ", totalSum)