import random


options = ["rock", "paper", "scissors"]

machine = random.choice(options)

def show_result(r):
    match r:
          case "l":
               print("You lost")
               print(f"Your choice: {user}")
               print(f"Computer's choice: {machine}")

          case "w":
               print("You won")
               print(f"Your choice: {user}")
               print(f"Computer's choice: {machine}")

          case "e":
               print("It's a tie")

while True: 
      user = input("Please choose one: rock, paper or scissors \n").lower()
      if user not in options:
         continue
      else:
           break
      
if user == machine:
   show_result("e")
elif user == "rock" and machine == "scissors":
     show_result("w")
elif user == "paper" and machine == "rock":
     show_result("w")
elif user == "scissors" and machine == "paper":
     show_result("w")
else:
     show_result("l")