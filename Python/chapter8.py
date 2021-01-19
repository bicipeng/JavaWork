#chapter 8 functions!!
#8_1 message:write a ft called display_message() that prints one sentence
#call the function
def what_i_learned():
	print("I learned how to define a function in python.")
what_i_learned()

# #8-2 favorite book: wrtie a function called f_b() that accepts one param
# #title, .and print a message when the ft is called
def favorite_book(title):
	print("My favorite book is " + title + '.')
favorite_book("Do Androids Dream of Eletric Sheep ?")

# #8-3 Write a function called make_shirt() that accepts a size and the text of
# # a message , print a message . call the function using a positional arguments 
# #call the function using keyword arguments
def make_shirt(size,message):
	print("You wear a size " + size + ', ' + "the message you want on the shirt is: " 
		+ message)
make_shirt("M","It's a good day.")#positional
make_shirt(message = "c'est la vie!", size = "xs")#keywor argument

# #8-4 Large Shirt : modify the previous fut s.t shirts are large by default
# #with default message "I love python"
# #make a large shirt and a medium shirt with the default message
# #a shirt of any size with a different message 

def make_shirt(size = "L" , message = "I love python."):
	print("The size of the shirt is: " + size + "." + "\n" 
		+ "The message on the shirt is: " + message)
make_shirt()
make_shirt("M")
make_shirt("xs", "Life is good")

# #8-5 cities: describe_city(), name and country. The ft should print a sentenct . 
#Give the param for the country a default value, call you ft for 3 diff cities
# at least one of which is not a default country
def describe_city(name, country= "Switzerland"):
	print(name + " is in " + country + ".")
describe_city("Zurich")
describe_city("Reykjavik", "Iceland")
describe_city("Shanghai", "China")


#8_6 city names: write a ft called city_country() that takes in the name of a city and its country.
#call your ft at least 3 time i.e. "Shangehai, China"
def city_country(city,country):
	output = "'" + city + ", " + country + "'"
	return output.title()
you_enter = city_country('Zurich', 'Switzerland')
print(you_enter)
print(city_country("Shangehai","china"))
print(city_country("paris",'france'))

#8-7 Album: ft that take in 3 params , artist name,album title, optiona param # of tracks
#return a dictionaries of the info , make sure to check if optional param is exist 
def make_album(artist,album_title,num_of_track = ''):
	album = {}
	album['Artist Name'] = artist
	album['Album Title'] = album_title
	if num_of_track:
		album['Number of Track'] = num_of_track
	return album
pink = make_album('P!nk', 'Beautiful Trauma')
print(pink)
taylor_swift = make_album ('Taylor Swift', 'Folklore' , 12)
print(taylor_swift)

#8-8 User_album : use the previous ft, wrtie a while loop that allows 
# users to enter an album's artist and title, once you have that info
#call maek_album() with user's input and print the tictionary that's
#created. Don't forget the quit value
while True:
	print("\n Enter the album information(enter q to quit).")
	your_input_name = input("Artist's Fullname: ")
	if your_input_name == 'q':
		break
	else:
		artist_name = your_input_name

	your_input_title = input("Aritst's Album Titile: ")
	if your_input_title == 'q':
		break
	else:
		artist_album_title = your_input_title

# your_artist = make_album (artist_name,artist_album_title)
# print(your_artist)

#8_9 Magicians: (passing a list to a ft )
def show_magicians(magicians):
	for magician in magicians:
		print(magician)
the_magicians = ['Mickey','Ken','Barbie','Belle','Emma']
output = show_magicians(the_magicians)

#8-10 Great Magicians : write a ft called ake_great() that modifies the list 
#of magicians by adding the prase the Great to each amgician's name
#Call show_magicians to see that the list has actualy been modified
def great_magicians(magicians):
	the_great_magicians = []
	for magician in magicians:
		great_magician = magician + " The Great"
		the_great_magicians.append(great_magician)
	return the_great_magicians
the_magicians = ["Mickey", "Minne", "Ken" ,"Barbie"]
output = great_magicians(the_magicians)
show_magicians(output) 
# Mickey The Great
# Minne The Great
# Ken The Great
# Barbie The Great

#8-11 Unchanged Magicians:call great_magician with a copy of the original list
#make sure you don't chagne the original list
copy_magicians = the_magicians[:]
output = great_magicians(copy_magicians)
show_magicians(output)
print(the_magicians) #make sure the original list didn't change

#8-12 sandwiches: wrtie a function accepts a list of items a person wants on a sandwich
#call the ft 3 times and use different number of arguments each time
def make_sandwiches(*eles):
	print("\n You sandwich is made with :")
	for ele in eles:
		print("- " + ele)
make_sandwiches("cheese")
make_sandwiches("cheese","tomato","beef")
make_sandwiches("chicken")

#8-13 User Proifle: built a profile about youself, use your first, last name and 3 key value paris
#to describe you
def make_profile(first, last, **user_info):
	info_profile = {}
	info_profile["First Name"] = first
	info_profile["Last Name"] = last
	for key,value in user_info.items():
		info_profile[key] = value
	return info_profile

# your_profile = make_profile("Belle" ,"Better", email = "belle@email.com" ,country = "Wonderland")
# print(your_profile)

#8-14 Cars :write a ft that stores info about a car in a dictionary
#should receive a manufacturer and a model name(skip , the same thing as the previous)



