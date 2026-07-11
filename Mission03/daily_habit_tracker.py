
#header
line="========================================="
print(line)
print("    CrimsonCranberry Habit Tracker    ")
print(line)

#body
#questiionnaire
exr=input("Did you exercise today? (Y/N): ")
pyt=input("Did you study Python today? (Y/N): ")
dsa=input("Did you solve one DSA problem? (Y/N): ")
read=input("Did you read for at least 20 minutes? (Y/N):")
h2o=input("Did you drink 2.8L of water? (Y/N): ")
garden=input("Did you get sunlight / gardening? (Y/N): ")
sleep=input("Did you sleep at least 7 hours? (Y/N): ")


#display the input in checkbox format
print(line)
print("Today's Habit Report")
print(line)


#Score logic
score=0
if exr=='Y':
    print("Exercise : ✅")
    score=score+1
else:
    print("Exercise : ❌")

if pyt=='Y':
    print("Python   : ✅")
    score=score+1
else:
    print("Python   : ❌")
    
if dsa=='Y':
    print("DSA      : ✅")
    score=score+1
else:
    print("DSA      : ❌")


if read=='Y':
    print("Reading  : ✅")
    score=score+1
else:
    print("Reading  : ❌")


if h2o=='Y':
    print("Water    : ✅")
    score=score+1
else:
    print("Water    : ❌")

if garden=='Y':
    print("Garden   : ✅")
    score=score+1
else:
    print("Garden   : ❌")


if sleep=='Y':
    print("Sleep    : ✅")
    score=score+1
else:
    print("Sleep    : ❌")

print(line)
print(f"Score :{score}/7")
if score==7:
    print("⭐⭐⭐⭐⭐")
    print("🔥 Outstanding! Perfect day!")
elif score==6:
    print("⭐⭐⭐⭐☆")
    print("🌟 Excellent consistency!")
elif score==5:
    print("⭐⭐⭐☆☆")
    print("👍 Great job! Keep it up!")
elif score==4:
    print("⭐⭐☆☆☆")
    print("🙂 Good progress. Aim for one more habit tomorrow!")
elif score==2 or score==3:
    print("⭐☆☆☆☆ ")
    print("💪 Keep improving. Small consistent steps matter.")
elif score==1 or score==0:
    print("☆☆☆☆☆")
    print("🌱 Tomorrow is a fresh start!")

#footer
print(line)
print("Thank you for using CrimsonCranberry!")
print("Have a great day! 😊")
print(line)