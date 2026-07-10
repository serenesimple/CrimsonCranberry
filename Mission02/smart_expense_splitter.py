
line="========================================"
print(line)
print("      Smart Expense Splitter        ")
print(line)
bill=float(input("Enter the totoal amount: "))
print("The totoal bill is: ", bill)
people=int(input("Enter the total no of people: "))
print("The total number of people are: ", people)

single_line="----------------------------------------"
print(single_line)
print("The totoal bill is: ", bill)
print("The total number of people is: ", people)
split_amount=bill/people
print(f"Each person should pay: ₹{split_amount:.2f}")

print(single_line)

print("Thank you for using CrimsonCranberry!")
print("Have a great day! 😊")