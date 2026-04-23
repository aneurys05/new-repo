import time

def display(num, message):
    for number in reversed(range(1, num + 1)):
        print(number)
        time.sleep(1)
    print(message)


while True:
      
      try:
           start = int(input("Please enter a number to start the countdown \n"))
           break
      
      except ValueError:
            continue
      
message = input("Please enter a message to display \n")

display(start, message)