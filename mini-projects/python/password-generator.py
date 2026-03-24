import random 
import string 

chars_list = [string.ascii_letters, string.digits, string.punctuation]

#function to create pool of characters
def add_to_pool(*args):
    pool = ""
    counter = 0
    for arg in args:
        pool += chars_list[counter] if arg == "y" else ""
        counter += 1
    
    return pool

print("-----Password Generator program-----")

while True: 
            try:
                
                how_many = int(input("How many passwords do you wish to generate? \n"))
                password_length = int(input("How many characters do you want for each password? \n"))
                break

            except ValueError:
                  print("Please enter a number \n")

add_letters = input("Do you wish to include letters?: Y/N \n").lower()
add_numbers = input("Do you wish to include numbers? Y/N \n")
add_symbols = input("Do you wish to include special symbols?: Y/N \n")
print()

pool = add_to_pool(add_letters, add_numbers, add_symbols)

#function to create passwords
def generate_password(quant, length, pool):
    for number in range(quant):
        if len(pool) == 0:
           print("Character pool is empty")
           break
        pasword = ""
        for _ in range(length):
             pasword += random.choice(pool)
        print(f"{number + 1}. {pasword}")

generate_password(how_many, password_length, pool)