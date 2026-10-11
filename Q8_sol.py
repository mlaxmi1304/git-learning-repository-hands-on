# Program 8: Dict of a Fruit Shop

fruitPriceDict = {
    "Apple": 120,
    "Banana": 60,
    "Grapes" : 200,
    "Orange": 100
}

inputFruit = input("Enter a fruit name: ").capitalize()

if inputFruit in fruitPriceDict:
    print(inputFruit.capitalize(), "is available.")
    print("Price:", fruitPriceDict[inputFruit])
else:
    print("Fruit not available.")