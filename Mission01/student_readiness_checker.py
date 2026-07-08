print("---Crimson Cranberry Student Readiness checker----")
name=input("Enter your  name: ")
age=int(input("Enter your age: "))
hours=float(input("Enter how many hours did you study today: "))

print()
print("Hello", name)
print("You are",age,"years old")
print("You studied",hours," hours today")

if hours > 2:
    print("Excellent consistency, kepp it up ")
else:
    print("Try to study one hour more") 

print("------Exercise status-------")
exercise=input("Did you do your exercise today ")
if exercise == "yes":
  print("Great, keep taking care of your health ")
else:
   print("Try to get atleast a short walk tomorrow ")