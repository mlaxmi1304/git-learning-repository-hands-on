# Program 3
print("--- ODD-EVEN NUMBER GAME ---")
wantToPlayAgain = 'yes'

while (wantToPlayAgain.lower() == 'yes'):
       
    num = int(input("Enter a number: "))

    if num%2 == 0:
        typeOfNumber = "Even"
    else:
        typeOfNumber = "Odd"
    print("Number is: ", typeOfNumber)   

    wantToPlayAgain = input("Do you want to play again? (yes/ no): ") 

print('Thanks for playing! Game Ended')