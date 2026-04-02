import random 


random_number = random.randint(1, 100)

print("----- Number guessing game-----")
while True: 
        
          try:
              user_guess = int(input("Enter a number between 1 and 100 \n"))
              if user_guess < 0 or user_guess > 100:
                 print("Number must be between 1 and 100 \n")
                 continue
              else:
                  
                   if user_guess == random_number:
                      print("Congratulations, you won!")
                      print(f"Number was {random_number}")
                      break
                   elif user_guess > random_number:
                      print("Too high, try again.")
                      continue
                   elif user_guess < random_number:
                       print("Too low, try again.")
                       continue
                   
          except ValueError:
                print("Please make sure to enter  a number \n")
                continue

              
         
