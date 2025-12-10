strng = str(input("Enter a String : "))

len = len(strng)
rev = strng[::-1]

if strng == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")