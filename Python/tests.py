#chapter 11: Testing your code.tests
#11-1
# import unittest
# from city_function import city_country
# class CityCountryTestCase(unittest.TestCase):
# 	def test_city_country(self):
# 		output = city_country("paris","france", "2.18 Million")
# 		self.assertEqual(output,"Paris, France - population 2.18 Million.")
# unittest.main()

#excercise test, testing a class
# import unittest
# from classSample import AnonymousSurvey
# class TestAnonymousSurvey(unittest.TestCase):
# 	'''test for the class AnonymousSurvey'''
# 	def test_store_three_responses(self):
# 		question = " What is your first language ?"
# 		my_survery = AnonymousSurvey(question)
# 		responses =['English' ,'Chinese', 'Spanish']
# 		for response in responses:
# 			my_survery.store_response(response)

# 		for response in responses:
# 			self.assertIn(response,my_survery.responses)
# unittest.main()

#excercse test, 11-3 test
import unittest
from classSample import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the class Employee"""

	def setUp(self):
		""" Create a new employee and print out their annual salary after raise
		 default raise is $5000, make sure if you change the default raise to other amount
		 the class still works
		 """
		first_name = "Ken"
		last_name = "Ginger"
		annual_salary = 70000
		self.employee_1 = Employee(first_name,last_name,annual_salary)
		self.salary_raise = 6000
	def test_default_raise(self):
		""" test if the method add 5000 to the annual salary if we don't enter a rasie amount"""
		self.employee_1.give_raise()
		final_salary = self.employee_1.annual_salary
		self.assertEqual(final_salary,75000)

	def test_raise_with_input_amount(self):
		""" if we enter salary raise = 6000, we should get 76000 for final salary"""
		self.employee_1.give_raise(self.salary_raise)
		final_salary = self.employee_1.annual_salary
		self.assertEqual(final_salary,76000)

unittest.main()
