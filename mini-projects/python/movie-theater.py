


snacks = [{ 

"Type": "Popcorn",
"Small": 5,
"Medium": 6.50,
"Large": 8}, 

{

"Type": "Soda",
"Medium": 5,
"Large": 7

}, 

{"Type": "Boxed Candy",
    "Skittles": 2,
    "M&M's": 3}, 
  
{"Type": "Others",
     "Hot Dog": 5,
     "Nachos": 7},
     
     
     {"Type": "Combos",
      "Large Popcorn + Large Drink": 12,
      "Popcorn + Drink + Candy": 15
      
      }]


print("-----MENU----")
for snack in snacks:
    print(snack["Type"])
    for key, value in snack.items():
        if key != "Type":
           print(key, ": ", value)
    print()