sercret_no=7
count=0
guess=int(input("Enter the guess number: "))
count+=1
while guess!=sercret_no:
    print("Wrong! Try again.")
    if guess>sercret_no:
     print("Too high!")
    elif guess<sercret_no:
     print("Too Low!")
    guess=int(input("Try guessing other number again: "))
    count+=1
print("🎉 Congratulations!")  
print("There were ",count,"tries")
   