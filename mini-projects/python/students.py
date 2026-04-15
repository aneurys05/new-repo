import os


marks = {
        
"English": 0,
"Math": 0,
"History": 0,
"Biology": 0

}


def restart(iterable):
    for item in iterable:
        iterable[item] = 0

print("-----Student registry-----")

while True:
            name = input("Please enter the students name \n")


            if name:
                    #Get marks 
                    for mark in marks:
                        
                        while True:           
                            try:
                                marks[mark] = int(input(f"Please enter the score for {mark} \n"))
                                if marks.get(mark) < 0 or marks.get(mark) > 100:
                                    print("Number must be between 0 and 100 \n")
                                    continue
                                else:
                                    break

                            except ValueError:
                                    print("Please make sure to enter a number \n")

                    os.mkdir(f"{name}")
                    with open(f"{name}/{name}-marks.txt", "x") as file:
                        file.write(f"{name} marks! \n")
                        file.write("\n")
                        for mark in marks:
                            file.write(f"{mark}: {marks.get(mark)} \n")          
            
            decision = input("Do you wish to register another student?: Y/N").lower()
            if decision == "y":
               restart(marks)
               continue
            else:
                break
               


            

