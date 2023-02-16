string_entry=(input("Enter a string to check palindrome:"))

if(string_entry==string_entry[::-1]):
    print("Yes given string is palindrome")
else:
    print("No the given string is not a palindrome")    