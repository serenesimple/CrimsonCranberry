import math

line="="*40
def display_heading():
       
        print(line)
        print("    Scientific Calculator   ")
        print(line)


def operation_list():
        print(f"\n 1. Addition \n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Power\n 6. Square Root\n 7. Modulus\n 8. Exit")


def add(a,b):
        return a+b
      

def subtract(a,b):
       return a-b
      

def multiply(a,b):
        return a*b
     

def divide (a,b):
       return a/b
  


def power(a,b):
        return a**b
      


def squareroot(a):
        return math.sqrt(a)


def modulo(a,b):
        return a%b


def get_choice():
      print()
      choice = int(input("Enter the choice: "))
      return choice
      

def get_one_number():
         print()
         fnum=int(input("Enter the number:  "))     
         return fnum    
      
      
              

def get_two_numbers():
        print()
       
        fnum=int(input("Enter first number:  "))
        snum=int(input("Enter second number: "))
        return  fnum, snum       
        print()
        


def display_footer():
    print("Thank you for using CrimsonCranberry!")
    print("Have a great day! 😊")
    print(line)



def main():
    display_heading()
    operation_list()
    choice=get_choice()
    one_number_operations=[6]


    if choice in one_number_operations:
     uno= get_one_number()
    else:
     fnum, snum = get_two_numbers()

    

    if choice==1:
        result = add(fnum, snum)
        print(result)
        
    elif choice==2:
        result = subtract(fnum, snum)
        print(result)
        
    elif choice==3:
        result = multiply(fnum, snum)
        print(result)
        
    elif choice==4:
        result = divide(fnum, snum)
        print(result)

    elif choice==5:
        result = power(fnum, snum)
        print(result)
            
    elif choice==6:
         result = squareroot(uno)
         print(result)
            
    elif choice==7:
        result = modulo(fnum, snum)
        print(result)
        
    elif choice==8:
          exit()
    else:
        print("Invalid option")
    display_footer()

main()



    