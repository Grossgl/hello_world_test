def good():
  list_1 = ['Harry', 'Ron', 'Hermione']
  return list_1

def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

# Use the generator function in a for loop
count = 0
for num in get_odds():
    if count == 2:
        print(num)
        break
    count += 1