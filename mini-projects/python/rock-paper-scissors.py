import random


options = ["rock", "paper", "scissors"]

machine = random.choice(options)


while True: 
      user = input("Please choose one: rock, paper or scissors \n").lower()
      if user not in options:
         continue
      else:
           break
      
