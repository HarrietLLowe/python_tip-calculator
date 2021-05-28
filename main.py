#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))

per = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

percentage_1 = per / 100
percentage_2 = total_bill * percentage_1
bill_with_percent = total_bill + percentage_2

num_people = int(input("How many people to split the bill? "))

final_value = round(bill_with_percent / num_people, 2)
final_value = "{:.2f}".format(bill_with_percent)
print(f"Each person should pay: ${final_value}")