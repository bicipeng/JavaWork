#chaper 10. files and exceptions
with open('pi_digit.txt') as file_object:
	contents = file_object.read()
	print(contents)

#10-1: read a file pirnts what you wrote 3 times
#reading in the entire file,loopint over the file obj, and 
#storing the lines in a list and then working with them outside the with block
file_name = 'learning_chapter10.txt'
with open(file_name) as file_object:
	contents = file_object.read()
	print(contents.strip())
loop over the file obj
with open(file_name) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

#storig the lines in a list
file_str = ''
for line in lines:
	file_str += line.strip()
print(file_str)

#10-3 guest: write a program that prompts theuser for their name. when they respond
#write their name to a file called guest.txt
guest_name = input("Please tell me your first and lastname: ")
filename='guest.txt'

with open('guest.txt','w') as file_object:
	file_object.write(guest_name)
	file_object.write("\nSucceed!")

#10-4 Guest Book: write a while loop that prompts users for their name. when they enter their
#name, print a greeting to the screen and add a line recording their visit in a file called 
#guest_book.txt. Make sure each entry appears on anew line in the file
guests_visited = 'guest_book.txt'

while True:
	guest = input("Please tell me your full name(enter 'q' to exit): ")
	if guest != 'q':
		print("Hello, " + guest + ". " + "\n")
		with open('guests_visited.txt','a') as file_obj:
			file_obj.write(guest + '\n')
	else:
		break
#10-5 Programing Poll: write a while loop that asks people why they like programing, 
#each tie someone enters a reason, add their reason to a file that stores all the responses
programming_lover = 'programming_lover.txt'

while True:
	reasons = input("Why do you like programming? (Enter 'q' to exit)")
	if reasons != 'q':
		with open('programming_lover.txt','a') as pl_obj:
			pl_obj.write("It's because " + reasons + '\n')
	else:
		break

#10-6 Addition: when you provide text instead of num,you should get valueError
while True:
	nums = input("Please enter two numbers with space (enter 'q' to exit):")
	if nums != 'q':
		num_list = nums.split()
		total = 0
		try:
			for num in num_list:
				total += int(num)
		except ValueError:
			pass
		else:
			print("The sum of the two nums is: " + str(total) )
	else:
		break

#10-7 addition calculator: use a while loop so the user can contiue entering numbers even if
#they enter a text (see above: it is the alternative version o f10-6)

#10-8 cats and dogs : make two files :cats.txt and dogs.txt . store at least three names of 
#cats in the first file and the same for the dogs file. write a program to read these files and print 
#the contents of the file to the screen. wrap your code in the try-except to catch the filenotfound error
filenames =['dogs.txt', 'cats.txt']
for file in filenames:
	try:
		with open(file) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		# message = "Sorry, the file is not found!"
		# print(message) 
		pass #10-9
	else:
		print(contents + '\n')

#10-9 Silent Cats and Dogs:modify your except block to fail silently 

#10-10 Common Words : write a program that reads the files you found at Project Gutenberg and determines how many 
#times the word 'the' appear in each text
filenames = ['walden.txt','Pride_and_Prejudice.txt','gg.txt']
for file in filenames:
	try:
		with open(file) as file_object:
			contents = file_object.read()#displays the whole file in str
	except FileNotFoundError:
		msg = "File not found!"
		print(msg)
	else:
		print(contents.lower().count('the'))

# using jason.dump() and jason.load() to read and store files
#examples
import json
numbers =[1,2,3,4,56,6]
filename = 'number.json'
with open(filename, 'w') as file_object:
	json.dump(numbers,file_object)

#read files using json.load()
with open(filename,) as file_obj:
	nums = json.load(file_obj)
print(nums)

#examle : use function to store user generated data
#it is important to check if the file you try to load is empty
#if it is empty , you will get mistake 
import json
import os # check if the file is empty
filename = 'username.json'


def get_stored_username():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None #return None and pass has the same result
	else:
		return username 


def get_new_user():
	"""prompt for a new user"""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username,f_obj)
	return username

def greet_user():
	""" Greet the user by name"""
	if os.stat(filename).st_size == 0:
		new_user = get_new_user()
	else:
		user_name = get_stored_username()
		check_current_user = input("Is this your username ? (Y/N) " + user_name + ": ")
		if check_current_user.lower() == 'y':
			print("Welcome back, " + user_name + "!")
		else:
			current_user = get_new_user()
			print("We will remember you when you come back, " + current_user + ".")
	
greet_user()

#10-11 Favorite number:write a program to prompt for a user's favorite number
#use json.dump() to store and a seperated program to read the num and print the msg
import json
import os
file_name = "fav_num.json"
def get_fav_num():
	fav_num = input('Enter your favorite number: ')
	try:
		with open(file_name,'w') as file_obj:
			json.dump(fav_num,file_obj)
	except FileNotFoundError:
		return None
	else:
		return fav_num

def display_fav_num():
	try:
		with open(file_name) as file_obj:
			fav_num = json.load(file_obj)
	except FileNotFoundError:
		return None
	else:
		return fav_num
#10-12 favorite number remembered
def fav_num_remembered():
	if os.stat(file_name).st_size == 0:
		favorite_num = get_fav_num()
		with open(file_name,'w') as new_obj:
			json.dump(favorite_num,new_obj)
		return favorite_num
	else:
		your_favor_num = display_fav_num()
		print("I know your favotie number! It's " + str(your_favor_num))

fav_num_remembered()

#modify example code to check if the user is a return user
#done

