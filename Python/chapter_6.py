# #Dictionary - key-value pairs

# #example
# person_1={'age':23,'gender':'female'}
# print(person_1['age'])

# #add key-value pairs to dictinary
# person_1['email']='person_1@email.com'
# print(person_1)

# #empty dictionay person_1={}, and then you can add key-value pairs in it 
# reassgin the value of the key-value pair
# person_1['age'] = 30
# print(person_1)#now age of person_1 is 30
# del person_1['age']#delete the key-value pair (age) from the dict
# print(person_1) 

# #6_1 make a dictionary of a person
# person_2={
# 	'first_name':'Betty',
# 	'last_name':'Bentley',
# 	'age':25,
# 	'city':'Wonderland',

# }

# for key, value in person_2.items():
# 	print(key + ": " + str(value))
# #add favorite numbers to a dictionary of person
# persons={
# 	'Amy':{
# 	'favorite_num': 5
# 	},
# 	'Betty':{
# 	'favorite_num': 100
# 	},
# 	'John':{
# 	'favorite_num':99
# 	}
# }
# print(persons.keys())# you get a list of keys in a list['Amy','John','Betty']
# print(persons.values())#you get a list of value in a list ['{favorite_num':5,...]

# #6-4 glossary,loop through key-value pairs, 
# glossary={
# 	'set()':'return a list without repetition',
# 	'.values()':'return a list of values from a dictionary without any keys without checking for repetition ',
# 	'.keys()':'return all the keys from a dictionary and store them in a list',
# 	'sorted()':'sotred the values temporarily, it can take more than one statement',
# 	'.items()':'returns a list of key-value pairs',
# 	'del':'used to remove the key-value pairs permantly',
# }
# for key,value in glossary.items():
# 	print('\n'+ key + ' : '+value )
# glossary['!=']='not equal'
# glossary['.sort()']='sort the list in order, can never be reversed'
# for key,value in glossary.items():
# 	print('\n'+ key + ' : '+value )

# #6-5make a dict containing theree major rivers and the country each river run through 
# rivers={
# 	'Nile':'Egypt',
# 	'Yellow':'China',
# 	'Amazon':'Peru',
# }
# # #use a loop to print a sentence about each river
# for river,country in rivers.items():
# 	print(river + 'runs through ' + country + '\n')
# #use a loop to print the name of each river
# for river in rivers.keys():
# 	print(river)
# #use a loop to print the name of each country
# for country in rivers.values():
# 	print(country)


# #6-6 Polling
# favorite_languages={
# 	'jen':'python',
# 	'sarah':'c',
# 	'edward':'ruby',
# 	'phil':'python'
# }
# #make a list of people who should tak the favorite languages poll, 
# #included some names that are already in the dict and some are  not
# should_take_poll=['jen','lucy','daisy','phil']
# #loop through the list of person who should take the poll, if they are alredy taking,
# #print a thanking message, else pinrt an invitation message
# for name in should_take_poll:
# 	if name in favorite_languages.keys():
# 		print(name + ', thank you for taking the poll')
# 	else:#you need the else statement here , otherwise when the name is not in the poll,
# 		#it will pirnt and then go throuhg the for loop again, so, it will print the repeated name twice
# 		print(name + ', please take the poll')

#6-7 make three dictionaries for 3 person, store them in a list
# person1={
# 	'first_name':'Amy',
# 	'last_name':'Andel',
# 	'age': 23,
# 	'city': 'far far away land'
# }
# person2={
# 	'first_name':'Betty',
# 	'last_name':'Dreamy',
# 	'age': 35 ,
# 	'city': 'dreamy land'
# }
# person3={
# 	'first_name':'cathy',
# 	'last_name':'candy',
# 	'age': 40 ,
# 	'city': 'candy land'
# }
# three_person=[person1,person2,person3]
# #loop through the list of person and print out their information
# for person in three_person:
# 	for key,value in person.items():
# 		print(key.title() + ': ' + str(value) )
# 	print('\n')

# #do the same thing for pet
# Meow = {
# 	'species': 'cat',
# 	'owner': 'John',
# }
# Bark = {
# 	'species':'dog',
# 	'owner':'Daisy'
# }
# Speachless = {
# 	'species':'sneak',
# 	'owner':'cathy'
# }
# Raphael = {
# 	'species': 'turtle',
# 	'owner': 'Ken'
# }
# pets=[Meow,Bark,Speachless,Raphael]
# for pet in pets:
# 	for key,value in pet.items():
# 		if key == 'species':
# 			print(pet['species'] + ' is owned by ' + pet['owner'])

#6-11 Cities dict
cities={
	'New York': {
	'country': 'U.S.A',
	'population': '8.34 Million'
	},
	'Paris': {
	'country': 'France',
	'population': '2.15 Million'
	},
	'Zurich': {
	'country': 'Switzerland',
	'population': '402,762'
	}
}
# cities_name = cities.keys() #after you extra the cities from the obejct , it is no longer an obj
# print(cities_name)
for key,value in cities.items():
	print ( key + ' is located in ' + value['country'] +' , it has a population of ' + value['population'] + '.' + '\n' )

cities['Beijing']={
	'country':'China',
	'population': '21.54 Million'
}

print(cities)
	

