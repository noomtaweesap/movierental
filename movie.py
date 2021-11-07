"""Movies information and details."""
from typing import List


class Movie:
    """A movie available for rent."""
    # The types of movies (price_code).
    def __init__(self, title: str, price_code, year: int, genre: List[str]):
        # Initialize a new movie.
        self._title = title
        self._price_code = price_code
        self._year = year
        self._genre = genre

    def get_price_code(self):
        """get price code."""
        return self._price_code

    def get_title(self):
        """get movie title."""
        return self._title

    def get_year(self):
        """get year."""
        return self._year

    def get_genre(self):
        """get movie genre."""
        return self._genre

    def is_genre(self, genre: str):
        """check movie genre."""
        return genre in self._genre

    def __str__(self):
        return self._title
