sports=['Cricket','Football','Baseball','Basketball','Tennis']
file=open('Names.txt','w')
for sport in sports:
    file.write(sport+"\n")
file.close    