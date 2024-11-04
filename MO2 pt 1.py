secret = 1
guess = 5

if guess < secret:
    print("Too low")
elif guess > secret:
    print("Too high")
else:
    print("Your guess is equal to the secret!", secret)

small = True
green = True
if small:
        if green:
            print("pea")
        else:
            print("cherry")
else:
        if green:
            print("watermelon")
        else:
            print("pumpkin")