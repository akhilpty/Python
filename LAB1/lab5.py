number_list1= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
number_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,21]
number_list3=[]

for x in number_list1:
    for y in number_list2:
        if(x==y and x not in number_list3):
            number_list3.append(x)
            
        
    
print(number_list3)
