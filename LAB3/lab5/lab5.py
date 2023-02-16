with open("Names.txt") as file:
    lines=file.readlines()
    lines=[line.rstrip() for line in lines]    
print(lines)    