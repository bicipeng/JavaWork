#if statements
#alien colors
alien_color=['yellow','red']
if 'green' in alien_color:
	print("player earned 5 points!")
else:
	print("player just earned 10 points!")
#5_5

if 'green' in alien_color:
	print("player earned 5 points!")
elif 'yellow' in alien_color:
	print("player earned 10 points!")
elif 'red' in alien_color:
	print("player earned 15 points!")

#stages of life: using if-elif-else chain to determine a person's stage of life 

age=25
if age < 2:
	print("The person is a baby!")
elif age >= 2 and age < 4:
	print("The person is a toddler!") 
elif age >= 4 and age < 13:
	print("The person is a kid!")
elif age >= 13 and age < 20:
	print("The person is a teenager!")
elif age >= 20 and age < 65:
	print("The person is an adult")
elif age >= 65:
	print("The person is an elder!")

#An empty list evaluates to by 'False' after if statement 

test_list=[]
if test_list:
	print("This is not a empty list!")
print("This is a empty list!")

#5_8,_9
names=['Admin','Betty','Cathy','Daisy','Emma']
if names:
	for name in names:
		if name == 'Admin' or name == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print("Hello " + name + ", thank you for logging in again.")
else:
	print("we need to find some users!!")

#5_10
current_users=["Belle","Mula","Snow White","Sleeping Beauty","Rapunzel"]
new_users=["mula","rapunzel","Merida","Moana","Tiana"]
new_list=[]
for current_user in current_users:
	new_list.append(current_user.lower())
print(new_list)
for user in new_users:
	if user.lower() in new_list:
		print("This username is taken")
	else:
		print("This username is available")

#5_11
numbers=range(1,10)
print(numbers)
print(type(numbers))#make sure you  make the list

for num in numbers:
	if num >= 1 and num <= 3:
		print(str(num) + "rd")
	elif num > 3 and num <=9:
		print(str(num) + "th")

