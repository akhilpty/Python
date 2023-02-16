user_number=int(input("Enter the number:"))

divisor_list=[]

for x in range(1,1000):
    if user_number%x==0:
        divisor_list.append(x)
print(divisor_list)        