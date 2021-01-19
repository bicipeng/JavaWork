#3.4 guest list
guests=["Amy","Betty","Cathy"]
print(guests)
#3.5
not_coming="Amy"
guests[0]="Annie"
print(guests)
#3.6
#1
message="I find a bigger table"
for guest in guests:
    print(guest + " : "+ message)

print(str(guests) + " , " + message)# you get ["Amy","Betty","Cathy"] , I find a bigger table
#2add guest at the beginning of the list
new_guest="Daisy"
guests.insert(0,new_guest)
print(guests)
#add guest at the middle of list 
new_guest2="Mannie"
guests.insert(2,new_guest2)
print(guests)
#add guest to the end of the list
new_guest3="Daniel"
guests.append(new_guest3)
print(guests)
#for each guest, print an invitation message
for new_guest in guests:
    print("Welcome, " + new_guest +"!")
#3.7 remove the guests from the guest list untill there are two person left
while len(guests) > 2:
	removed_guest=guests.pop()
	print("Sorry, " + removed_guest + " there is not enough space.")
print(guests)
#for each guest , give a messsage 

for invited_guests in guests:
	print("Hi, " + invited_guests + ", " +"you are still invited!")

#use del to remove the last twon  name form you list, make sure the guest list is empty
while len(guests):
	del guests[0]
print(guests)