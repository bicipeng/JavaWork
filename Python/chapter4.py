#4.1create list
pizzas=['Pepperoni',"Cheese","Greek","New York Style"]
for pizza in pizzas:
	print("I like "+ pizza + " pizza!")
print("I really Like pizza!!")
#4.2 animals
animals=['Rabbit','Cat','Fox','Flamingo','Turtle',"Whale"]
for animal in animals:
	print(animal + " is really cute!")
print("All of these animals are furry!!!")
#create numeric list
new_list=range(50,100,10)
print(new_list)# you get [1,2,3,4], 5 is not included
print(type(new_list))
print(2**3)
#4.3 for loop and list comprehensions
#count from 1 to 20 including 20 use for loop
for num in range(1,21):
	print(num)
#make a list of odd number from 1-20 , use a for loop to print each number
for num in range(1,20,2):
	print(num)
#make a list of the multiple of 3 from 3 to 30 , usring the for loop to print 
#the numbers in you list
for num in range(3,30,3):
	print(num)
#cubes : do the same as above
for cube in range(1,11):
	output=cube**3
	print(output)
#cubes:comprehension
cube_list=[num**3 for num in range(1,11)]
print(cube_list)
#4-10 slices
#print fist 3 ele in the list , I am using he animal list 
print("The first 3 animals are " + str(animals[:3]))
print("The last 3 animals are " + str(animals[-3:]))
#define a tuple using (), and make sure the type of the tuple is tuple
fist_tuple=('A','B','C')
print(type(fist_tuple))# we get <type 'tuple'>

