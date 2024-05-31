import random 
mains = ["cauliflower", "tilapia fillet", "pork loin", "salmon"]
extras = ["with balsamico", "with garlic and olive oil", "with minted yogurt", "lemon and oil"]
main_prices = [8, 10, 7,7]
extra_prices = [9, 11, 8,8]

while True:
    try:
        number_of_items = int(input("How many items would you like? "))
        break
    except ValueError:
        print("please enter an integer!")
for i in range(number_of_items):
    main = random.choice(mains)
    print (f"{main} {random.choice(extras)}. The price for this item is {main_prices[mains.index(main)]}")
