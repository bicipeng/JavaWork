#create a list, not in alphabetical order
places=['Paris','Switzerland','Denmark','Turkey','China']
print(places)
#temperory sorted the list
sorted_list=sorted(places)
print(sorted_list)
print(places)
#reverse the order of the temporary sorted list,sorted can accept more than one argument
print(sorted(places,reverse=True))
print(places)
#permanatly reverse the order of the list, don't assign it to a new val since it change the original list and dont return a new list
places.reverse()
print(places)
#reverse back, can not do print(places.reverse()) since reverse method doesn't return a new list, so you are basically printing nothing
places.reverse()
print(places)
#sort the list
places.sort()
print(places)
#use sort to change the order of the list
places.sort(reverse=True)
print(places)

#find the lenght of the list
length=len(places)
print("There are "+ str(length)+" places I want to visit!")
