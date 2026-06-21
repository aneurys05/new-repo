


word = input("Please enter a word \n")

count = {}

for letter in word:
       count[letter] = count[letter] + 1 if letter in count else 1

most_frequent = ""
count2 = 0

for letter in word:
    if count.get(letter) > count2:
       most_frequent = letter 
       count2 = count.get(letter)
    elif count.get(letter) == count2:
         most_frequent += f", {letter}" if most_frequent.find(letter) == -1 else ""
   

print(count)
print(most_frequent)