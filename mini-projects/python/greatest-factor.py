


def check_number(number, divisor):
    if number % divisor != 0:
       return f"{divisor} is not a factor of {number} \n"
    
    for digit in range(divisor + 1, number):
        if number % digit == 0:
           return "incorrect"
    
    return f"correct, {divisor} is {number}'s greatest factor that is not itself \n"

value = 0
while True:
      try:
           if value == 0:
              value = int(input("Please enter a number \n"))
           factor = int(input(f"Please enter {value} greatest factor that is not itself \n"))
           break
          

      except ValueError:
          print("Invalid value")
          continue

print(check_number(value, factor))