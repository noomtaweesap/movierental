import unittest
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.children_movie = Movie("Frozen", PriceCode.children)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
		rental = Rental(self.children_movie, 1)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_price(), 2.0)

	def test_rental_points(self):
		rental = Rental(self.new_movie, 2)
		self.assertEqual(rental.get_renter_points(), 2)
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.regular_movie, 7)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.children_movie, 3)
		self.assertEqual(rental.get_renter_points(), 1)
		rental = Rental(self.children_movie, 2)
		self.assertEqual(rental.get_renter_points(), 1)
