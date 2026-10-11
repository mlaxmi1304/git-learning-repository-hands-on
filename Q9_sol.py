
listNums = []

for i in range(5):
    num = int(input("Enter a Number: "))
    listNums.append(num)

def calculateSum(numbers):
    totalSum = 0
    for num in numbers:
        totalSum += num
    return totalSum

print(calculateSum(listNums))   
