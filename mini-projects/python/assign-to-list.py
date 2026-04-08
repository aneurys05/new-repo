import random 


# Create list with a size of 10
numbers = [None] * 10

#Get a random number and if type (even, odd) matches with index, add that number to the index position
# otherwise keep looping until you get a number that matches

for number in range(10):
    randnum = random.randint(1, 100)
    while number % 2 != randnum % 2:
          randnum = random.randint(1, 100)
    numbers[number] = randnum
    

print(numbers)