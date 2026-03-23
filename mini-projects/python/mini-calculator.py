


to_continue = True


print("-----MINI CALCULATOR-----")

while to_continue:
      
      try:
            a = int(input("Please enter the first number \n"))

            b = int(input("Please enter the second number \n"))

            operator = input("Please choose an operator: + - / * \n")

            match operator:
                  
                  case "+":
                        print(f"{a} plus {b} equals {a + b} \n")
                  
                  case "-":
                        print(f"{a} minus {b} equals {a - b} \n")

                  case "*":
                        print(f"{a} multiplied by {b} equals {a * b} \n")

                  case "/":
                        print(f"{a} divided by {b} equals {a / b} \n")
                  
                  case _: 
                        print("Please select a correct operator")
                        continue
            
            decision = input("Do you wish to continue? Y/N: \n").lower()

            if decision == "n" or decision == "no":
               to_continue = False

      except ValueError:
             
             print("Make sure to enter a number \n")

