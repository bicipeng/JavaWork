#chapter 11: Testing your code.tests
#11-1
import unittest
from city_function import city_country
class CityCountryTestCase(unittest.TestCase):
	def test_city_country(self):
		output = city_country("paris","france", "2.18 Million")
		self.assertEqual(output,"Paris, France - population 2.18 Million.")
unittest.main()