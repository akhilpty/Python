import random

randomnum=(random.randint(1,9))
for x in range(5):
    usernumber=input("Enter the number(1-9):")
    usernumber=int(usernumber)

    if(usernumber==randomnum):
        print(" Exactly right")
        break
    elif(usernumber>randomnum):
        print("Too high")
    else:
        print("Too low")        

