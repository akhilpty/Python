import random 
import string
user_pre=int(input("How strong you want your password( 8 < prefered):"))
pass_letter=string.ascii_letters
pass_num=string.digits
pass_sym=string.punctuation
max_len=user_pre
password=""
if(max_len==1):
    print("More than one digit requird")
else:
    for x in range(max_len):
        pass_key=random.choice(pass_letter+pass_num+pass_sym)
        password = password+pass_key
print(password)