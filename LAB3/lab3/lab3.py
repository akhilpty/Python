for_file=open("randomtext.txt","a")
for_file.write("Adding new content")
for_file.close()
for_file=open("randomtext.txt","r")
print(for_file.read())