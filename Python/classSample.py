#chapter 11 :testing class
#exercise
# class AnonymousSurvey():
# 	""" Collect anoymous answers to a survey question"""
# 	def __init__(self,question):
# 		"""store a question and prepare to store responses."""
# 		self.question = question
# 		self.responses = []
# 	def show_question(self):
# 		"""show the survey question"""
# 		print(self.question)

# 	def store_response(self,new_response):
# 		""" store a single response to the survey"""
# 		self.responses.append(new_response)

# 	def show_results(self):
# 		""" Show all the responses that have been given"""
# 		print("Surver Results:")
# 		for response in self.responses:
# 			print("- " + response)
# question = "What is your first language?"
# my_survey = AnonymousSurvey(question)
# #show the question
# my_survey.show_question()
# print("Enter q at any time to quit.\n")
# while True:
# 	response = input("Language: ")
# 	if response != 'q' :
# 		my_survey.store_response(response)
# 	else:
# 		break
# print("\nThank you for taking the survey! ")
# my_survey.show_results()

#chapter 11-3
#employee: write a class calle demployee. the __init__() method 
#should take in a first name, a last name and an annual salary, and story each of
#these as attributes. 
#method give_raise(): addss$5000 to the anual salary by default but also accepts a diff raise
#test cast for employee, 2 test methods. test_give_default_raise() and test_give_custom_raise()
#use setUp() method so you don't have to create a new employee instance 
class Employee() :
	def __init__(self, first, last, annual_salary):
		self.first = first
		self.last = last
		self.annual_salary = annual_salary
	def give_raise(self,salary_raise = 5000):
		self.salary_raise = salary_raise
		self. annual_salary += self.salary_raise
	
		print(self.first + " " + self.last + "'s annual salary is " + str(self.annual_salary))
		
# employee1 = Employee("Ada", "Brook", 60000)
# employee1.give_raise()
# employee2 = Employee("Barbie", "Awanda",60000)
# employee2.give_raise(7000)