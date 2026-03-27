



snacks = {

"popcorn": 6.50, 
"soda": 5,
"skittles": 2, 
"m&m": 3,
"hot dog": 5,
"nachos": 7,

}


cart = []
total = 0

print("-----MENU-----")

for snack in snacks:
    print(f"{snack}: {snacks.get(snack)}")

while True:
      selection = input("Please select a product from the menu \n")

      if selection in snacks:
         cart.append(selection)
         total += snacks.get(selection)

      to_continue = input("Do you wish to add anything else?: Y/N \n").lower()
      if to_continue == "n":
         break
      
print(f"Your cart: \n")
for product in cart:
    print(f"{product}: {snacks.get(product)}")
print(f"Your total is : {total}")

