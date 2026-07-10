count = 1

while count <= 5:
    print(count)
    count = count + 1


sercret_no=7
guess=int(input("Enter the guess number: "))
while guess!=sercret_no:
    print("Wrong! Try again.")
    guess=int(input("Try guessing other number again: "))
print("🎉 Congratulations!")