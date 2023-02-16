UserNumber=input("Enter your number:")
UserNumber=int(UserNumber)
if(UserNumber==0):
    print("Enter a value above zero")
elif(UserNumber%2==0):
    print("You have entered a Even number & the number is",UserNumber)
else:
    print("You have entered a odd number & the number is",UserNumber)
