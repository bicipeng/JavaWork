#chapter 11 : testing your code, code
def city_country(city,country,population = ''):
	""" return a string with fomat city,country"""
	if population:
		output = city.title() + ", " + country.title() + " - population " + population + "."
	else:
		output = city.title() + ", " + country.title() + "."
	return output

print(city_country("Shanghai","China",'24.28 Million'))