price_to_find = 100
while True:
    user = int(input("Enter a number: "))
    if user > price_to_find:
        print("It's less.")
    elif user < price_to_find:
        print("It's more.")
    else:
        print("Well done, you won!")
        break

              