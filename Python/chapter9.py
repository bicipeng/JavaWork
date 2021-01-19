#class
#9-1 restaurant: make a class restaurant accepts two argu name and cuisine_type
#with methods : describe_restaurant() and open_restaurant() 
#make a specific restaurant instance using the class
# class Restaurant():
# 	""" a restaurant that tells you a little bit about the restaurant"""
# 	def __init__(self,restaurant_name,cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
# 	def describe_restaurant(self):
# 		print("\nThe restaurant's name is " + self.restaurant_name + "." +
# 			"\n It has great " + self.cuisine_type + " food.")
# 	def open_restaurant(self):
# 		print("\n The restaurant is now opened!")

# new_restaurant = Restaurant("Panda's","Chinese")#is a restarant instance
# print(new_restaurant.describe_restaurant())
# print(new_restaurant.open_restaurant())

# #9-2 three restaurant:use the code above and create 3 restaurant
# restaurant_two = Restaurant("Mama's Cook" ,"Italian")
# print(restaurant_two.describe_restaurant())
# print(restaurant_two.open_restaurant())

# restaurant_three = Restaurant("Fishman's" , "Japanese")
# print(restaurant_three.describe_restaurant())
# print(restaurant_three.open_restaurant())

#9-3 Users: do the same thing for Users
class Users():
	def __init__(self,first_name,last_name,gender,age,email):
		""" provide Users's general info"""
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.age = age
		self.email = email
	def describe_user(self):
		""" display Users' info"""
		user_profile = {}
		user_profile['First Name'] = self.first_name
		user_profile['Last Name'] = self.last_name
		user_profile['Gender'] = self.gender
		user_profile['Age'] = self.age
		user_profile['Email']= self.email
		print("Below is the user's profile : ") 
		print(user_profile)

	def greet_user(self):
		""" send a greating message to a user"""
		print("Hello, " + self.first_name + " " + self.last_name + ".")
user_one = Users("Annie","Albert","F",55,"annie@email.com")
user_two = Users("Betty", "Ben", "X", 24,"bb@email.com")
# user_three = Users("Daniel", "Black" ,"M" ,16 ,"dblack@email.com")
# print(user_one.describe_user())
# print(user_one.greet_user())
# print(user_two.greet_user())
# print(user_three.describe_user())

#9-4 Nmber Served: Use the code from 9-1,add attribute called nubmer_served
#with a default value =0, create an instance call restaurant form this class 
#print the number of customers the restorant has served and change the value
#and print it. 
#add method set_number_served() to set the numver of customer that have been servd
#add increment_number_served() to increate teh num of customer , call the method

class Restaurant():
	""" a restaurant that tells you a little bit about the restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.nubmer_served = 0
	def describe_restaurant(self):
		print("\nThe restaurant's name is " + self.restaurant_name + "." +
			"\n It has great " + self.cuisine_type + " food.")
	def open_restaurant(self):
		print("\n The restaurant is now opened!")
	def set_number_served(self,num_customer):
		self.nubmer_served = num_customer
		print("Num of customers that have been served: " + str(self.nubmer_served))
	def increment_num_served(self,customers):
		self.nubmer_served += customers
		print("Now, num of customers that have been served is: " + str(self.nubmer_served))




# new_restaurant = Restaurant ("Junkie's Cafe" ,"Hambergur")
# # print(new_restaurant.nubmer_served(10)) #we got 0 at the beginning
# # new_restaurant.set_number_served(23) #Num of customers that have been served: 23
# new_restaurant.increment_num_served(2)
# new_restaurant.increment_num_served(15)

#9-5 Login Attempts: Use code from 9-3, add attribute called login_attempts
#add a method called increment_login_attempts() that increments that value of login_attempts by 1
#add a method called rest_login_attempts() that resets the value of login_attempts to 0

class Users():
	def __init__(self,first_name,last_name):
		""" provide Users's general info"""
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0

	def greet_user(self):
		""" send a greating message to a user"""
		print("Hello, " + self.first_name + " " + self.last_name + ".")

	def increment_login_attempts(self):
		self.login_attempts += 1
		print( str(self.login_attempts) + " login attempts.")

	def reset_login_attempts(self):
		self.login_attempts = 0
		print("Login attempts after reset: " + str(self.login_attempts))

# new_user = Users("betty","black")
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.increment_login_attempts()
# new_user.reset_login_attempts()
# print(new_user.login_attempts)

#Inheritance
#9-6 Ice Cream Stand: a specific kind of restaurant. Write a calls called IceCreamStand
#that inherits from the Restaurant class you wrote in exercise9-4
#add attribute called flavors that stores a list of icecream flavor
#add method that displays these flavos , create an instance of IceCreamStand,and call this method

# class IceCreamStand(Restaurant):
# 	"""docstring for ClassName"""
# 	def __init__(self,restaurant_name,cuisine_type ):
# 		super().__init__(restaurant_name,cuisine_type)
# 		self.flavors = ["green tea","chocolate","pistachio", "vanilla"]
# 	def ice_cream_flavors(self):
# 		print("Here are all the icecream flavors: ")
# 		for flavor in self.flavors:
# 			print(flavor + "\n")
# icecream = IceCreamStand("Icy Nicy","Snack")
# icecream.ice_cream_flavors()
# icecream.describe_restaurant()

#9-7Admin: write a admin calss that inherits form the user calss you wrote
#add attribute -privileges that stores a list of strings like "can add post"
#method show_privileges() that lists the admin's privileges
#create an instanc eof admin and call your method

# class Admin(Users):
# 	def __init__(self,first_name,last_name):
# 		super().__init__(first_name,last_name)
# 		self.admin_privileges = Privileges()



# #9-8 Privileges class : have one attribute -privileges that store list of str
# #, move the show_privileges() to the privileges calss
# #make a privileges instance as an attribute in the admin class. Create a new 
# #instance of admin and use your method to show its privileges
class Privileges():
	def __init__(self):
		self.privileges = ["can add post" ,"can delete post", "can ban user"]
	def show_privileges(self):
		output = self.privileges
		return output
		
admin_one = Admin("Adaa" ,"Angelo")
print(admin_one.admin_privileges.show_privileges())

#9-9 skip for now...

import sys
print(sys.version)

