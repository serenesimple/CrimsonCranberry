
#header
line="========================================"
print(line)
print("    Multiplication Table Generator   ")
print(line)


#body
print()

num=int(input("Generate multiplication tables up to : :  "))
print()
print(line)
for i in range (1,num+1):
    print(f"\nTable for : {i} ")
    print()
    for j in range (1,16):
        print(" ",i ,"*",j, "=", i*j)
    print("------------------------")    
    


#footer
print()
print(line)
print("Thank you for using CrimsonCranberry!")
print("Have a great day! 😊")
print(line)