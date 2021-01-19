# file to experience how to use module and import module
def make_pizza(size,*toppings):
	print("\n Making a " + str(size) +
		 "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)