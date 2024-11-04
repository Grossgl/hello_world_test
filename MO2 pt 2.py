for x in range (3, 0):
    print (x)
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("Found it")
        break
    else:
        print("oops")
        number += 1
