import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these : 
		1. Letters
		2. Digits
		3. Special characters''')
count=0
password = []
while(count<length):
	choice = int(input("Pick a number "))
	count=count+1
	if(choice == 1):
		password.append(random.choice(string.ascii_letters))
		
	elif(choice == 2):
		password.append(random.choice(string.digits))
		
	elif(choice == 3):
		password.append(random.choice(string.punctuation))
		
	else:
		print("Please pick a valid option!")
		count=count-1

print("The random password is " + "".join(password))
