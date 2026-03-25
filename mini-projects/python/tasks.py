
#Program to generate files for each month


months = {

"january": 31,
"february": 28,
"march": 31,
"april": 30,
"may": 31,
"june": 30,
"july": 31,
"august": 31,
"september": 30,
"october": 31,
"november": 30,
"december": 31

}


for month in months: 
    with open(f"{month}-tasks.txt", "x") as file:
         file.write(f"{month.capitalize()} tasks \n")
         file.write("\n")
         for number in range(months.get(month)):
             file.write(f"{number + 1}. \n")