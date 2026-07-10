

line="==============================="
print(line)
print("    Student Grade Analyzer   ")
print(line)
no_of_subjects=int(input("How many subjects ? :"))
print()

total=0
avg=0
max=0
min=101


for i in range(1,no_of_subjects+1):
    marks=int(input(f"Enter marks for Subject {i}:"))
    
    total=total+marks
    
    if max < marks:
        max=marks
    else:
        max
    if marks < min:
        min=marks
    else:
        min
        
avg=total/no_of_subjects

print()

print(line)
print(f"Total marks: {total} ")
print(f"Average marks: {avg:.2f} ")
print(f"Highest marks: {max} ")
print(f"Lowest marks: {min} ")
print(line)
print()
print("Thank you for using CrimsonCranberry!")
print("Have a great day! 😊")
print(line)