line="=================================="
print(line)
print("     Discount Calculator   ")
print(line)

amount=float(input("Enter the purchase amount: "))
print("Purchase Amount :",amount)
if amount>=5000:
  Discount="20%"
  print("Discount",Discount)
  saved_amount=amount*0.2
  print("You saved :",saved_amount)
  final_amount=amount-saved_amount
  print("Final Amount :",final_amount)

elif amount>=3000:
  Discount="10%"
  print("Discount",Discount)
  saved_amount=amount*0.1
  print("You saved :",saved_amount)
  final_amount=amount-saved_amount
  print("Final Amount :",final_amount)

elif amount>=1000:
  Discount="5%"
  print("Discount",Discount)
  saved_amount=amount*0.05
  print("You saved :",saved_amount)
  final_amount=amount-saved_amount
  print("Final Amount :",final_amount)

else:
   print("No discount")

print("Thank you for using CrimsonCranberry!")
print("Have a great day! 😊")