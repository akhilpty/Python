import datetime
userName=input("Please entery you name:")
userAge=input("Please enter your age")
userAge=int(userAge)
today=(datetime.date.today())
year=today.year
yearOfB=year-userAge
print(yearOfB)
hundredYear=yearOfB+100
print('Hello',userName,'You will turn 100 in',hundredYear)