#testing the input() function
name = input("please enter your name to proceed:")
print("Hello " + name + " !" )

#chapter 7
#7_1 car rental
message=input("Please tell me what kind of car you are looking for: ")
print("Let me see if I can find you a " + message + '.')

#7_2 comparison:dont forget to convert input into a numerical value when you do comparison
guest = input("How many people are in your group? ")
number_of_guest = int(guest)
if number_of_guest > 8:
	print("Please wait for next available table.")
else:
	print("Your table is ready!")

#check if a num is a multiplle of 10
message = input("Please enter a num: ")
num = int(message)
if num % 10 == 0:
	print("The number you enter is a mutiple of 10.")
else:
	print("The number you enter is not a mutiple of 10.")


#7-4 pizza toppings 
prompt = "\n Please tell me what toppings you want for your pizza: "
prompt += "\n (Enter 'quit' when you are finished. )"

added_toppings = True
while added_toppings:
	toppings = input(prompt)
	if toppings == 'quit':
		added_toppings = False
	else:
		print(toppings + " is added to your pizza!")

#7-5 Movie Tickets: different tickt prices depending on a person's age.  age < 3 :free, 3 < age <12 : $10, age >12: $15. 
prompt = "\n Please enter your age to see the ticket price: "
prompt += "\n(Enter 'quit' to exit. )"

while True:
	age = input(prompt)
	if age == 'quit':
		break
	if age < str(3):
		print("It is free for you!")
	elif age >= str(3) and age < str(12):
		print("The ticket price is $10.")
	elif age >= str(12):
		print("The ticket price is $15.")

#7-6 three exits: rewrite 7-4 or 7-5 s.t. 
# Use a conditonal test in the while satemnet to stop the loop
prompt = "\n Please enter your age to see the ticket price: "
prompt += "\n(Enter 'quit' to exit. )"
while True:
	age = input(prompt)
	if age < str(3):
		print("It is free for you!")
		continue
	elif age >= str(3) and age < str(12):
		print("The ticket price is $10.")
		continue
	elif age >= str(12):
		print("The ticket price is $15.")
		continue
	else:
		break


#use an active variable to control how long the loop run
flag = True

while flag:
	age = input(prompt)
	if age == 'quit':
		flag = False
	elif int(age) < int(3):
		print("It's free for you.")
		continue
	elif int(age) >= int(3) and int(age) < int(12):
		print("The ticket price is $10.")
		continue
	elif int(age) >= int(12):
		print("The ticket price is $15.")
		continue
	
#7-8 Deli: Make a list called sanwich_orders and fill it with the name of various sandwiches. 
#make an empty list called finished_sandwiches. Loop through the list of the sandwich. As each 
#sandwich is amde, move it to the list of finished sandwiches. After all the sandwiches has been made
#print a message listing each sandwich that has been made
sandwich_orders = ['pastrami','cheesesteak','lobster' 'roll','pastrami','blt', 'barros' 'luco', 'club','pastrami']
finished_sandwiches = []
print("\n Sorry, we are out of pastrami!\n")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	finished_sandwiches.append(sandwich)
for sandwich_made in finished_sandwiches:
	print(sandwich_made + " has been made! \n")

#7-9 No pastrami: use the sandwich_orders list and make sure 'pastrami'appears
#in the list at least three thimes , then add message to say that there's no more
#pastrami. use a while loop to remove all the pastrami(see above)

#7-10
#Dream Vacation: write a program to poll users' dream vacation. 
dream_vacations = {}

poll_active = True

while poll_active:
	name = input("Please tell me your name: ")
	place = input ("Tell me where do you want to go for your dream vactaion: ")
	dream_vacations[name] = place
	next_poll = input("Next poll? (Yes/No) ")
	if next_poll == 'no':
		poll_active = False
print(dream_vacations)

for name,place in dream_vacations.items():
	print('\n' + name + "'s dream vactaion is " + place + ".")
	
#DONE!


	