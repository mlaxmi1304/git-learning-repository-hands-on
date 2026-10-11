# Program 6
listNums = []
for i in range(5):
    num = int(input("Enter a number: "))
    listNums.append(num)

def equalElements(num1, num2):
    return (num1 == num2)    

num1 = listNums[0]
num2 = listNums[4]
print("Are the first and last element same? ", equalElements(num1, num2))
