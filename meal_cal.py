# This program calculates a full restaurant bill by taking meal, appetizer, and drink orders and calculating the subtotal, sales tax, total, and change.

childs_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))

print("")

total_children = int(input("How many children are there? "))
total_adults = int(input("How many adults are there? "))

print("")

appetizer_price = float(input("What is the price of one appetizer? "))
total_appetizers = int(input("How many appetizers were ordered? "))

print("")

drink_price = float(input("What is the price of one drink? "))
total_drinks = int(input("How many drinks were ordered?"))

#subtotal calculation
child_subtotal = total_children * childs_meal
adult_subtotal = total_adults * adult_meal
appetizer_subtotal = total_appetizers * appetizer_price
drink_subtotal = total_drinks * drink_price

print("")

#main subtotal
main_subtotal = child_subtotal + adult_subtotal + appetizer_subtotal + drink_subtotal

print(f"Subtotal: ${main_subtotal:.2f}")

print("")

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = main_subtotal * sales_tax_rate / 100

print(f"Sales Tax: ${sales_tax:.2f}")

total = main_subtotal + sales_tax
print(f"Total: ${total:.2f}")

print("")
payment_amt = float(input("What is the payment amount? "))
change = payment_amt - total
print(f"Change: ${change:.2f}")