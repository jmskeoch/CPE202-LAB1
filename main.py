from dataclasses import dataclass
from typing import *
import unittest
import math
# ==== 1. DATA DEFINITIONS ====

# 1) We will convert a given Celsius temperature to Fahrenheit
celsius: TypeAlias = float
fahrenheit: TypeAlias = float

# 2) We will represent a price record with its price and product
product_price: TypeAlias = float


# 3) We will represent a Price Record with a product name and its price
@dataclass
class PriceRecord:
    name: str
    price: float


# 4) We will represent a web browser Tab with its current URL and Access Date
@dataclass
class Tab:
    url: str
    access_date: str


# ==== 2. SIGNATURE, PURPOSE, HEADERS ====

# 1) This function takes a given price (float) as an input and returns the input with added sales tax (float)
"""
Returns the inputted price with added sales tax
:param price: the original input price (float)
:return: new price with added sales tax (float)
"""

# 2) This function takes the item and returns the corresponding price
"""
Finds the price for a inputted item
:param item_name: name of item we wish to get price info from (str)
:return: store price of item_name (float)
"""

# 3) Takes a given geographic_region object to and given database to find median incomes of all homes in region
"""
Finds the median household income for a given region
:param geographic_region: desired region for income calculations (str)
:param database: income database (Database)
:return: median household income (float)
"""

# 4) This function uses a given geographic region and database to find overlapping cities
"""
Finds any overlapping cities in a given region
:param geographic_region: desired region for calculations (str)
:param database: city region database (Database)
:return: overlapping cities (str[])
"""


# ==== 3. TEST CASES ====
class Section4TestCases(unittest.TestCase):
    """
    1) We will find the second largest of three unique numbers

    :param num1: a float unique from num2 and num3
    :param num2: a float unique from num1 and num3
    :param num3: a float unique from num2 and num1
    :return: the second-largest float that was inputted

    pre-condition: inputs are floats, num1!=num2!=num3
    post-condition: second largest is returned
    invariant: 1>0
    """
    def second_largest_of_three(self, num1, num2, num3):
        return
        
    def test_second_largest_of_three(self):
        result1 = self.second_largest_of_three(self, 1, 2, 3)
        self.assertEqual(result1, 2)

        result2 = self.second_largest_of_three(-1, 0, 1)
        self.assertEqual(result2, 0)

        with self.assertRaises(TypeError):
            self.second_largest_of_three(1, "two", 3)

        # with self.assertRaises(InvalidInputError): #InvalidInputError defined in second_largest_of_three
            # self.second_largest_of_three(1, 1, 1)

    """
    2) We will determine if a string contains capital letters

    :param my_string: a string representing a word or sentence to check for capitals
    :return: true if Input contains capital letters else false

    pre-condition: Input is a string
    post-condition: returns bool true or false if contains capitals or not
    """
    def caps_check(self, my_string: str):
        return

    def test_caps_check(self):
        result1 = self.caps_check("Ohio")
        self.assertEqual(result1, True)

        result2 = self.caps_check("two thousand and 4")
        self.assertEqual(result2, False)

        with self.assertRaises(TypeError):
            self.caps_check(45)

    """
    3) We will determine the northernmost of two states
        
    :param state1: string representing a US state
    :param state2: string representing a US state
    :return: string representing northernmost of the two states

    pre-condition: inputs are both strings and names of US states
    post-condition: will return northernmost of two states
    """
    def north_checker(self, state1: str, stat2: str):
        return

    def test_north_checker(self):
        result1 = self.north_checker("Washington", "Oregon")
        self.assertEqual(result1, "Washington")

        result2 = self.north_checker("Washington", "Alaska")
        self.assertEqual(result2, "Alaska")

        with self.assertRaises(TypeError):
            self.north_checker("Washington", 46)

        # with self.assertRaises(InvalidInputError):  # InvalidInputError defined in north_checker
            # self.north_checker("Washington", "canada")


# ==== 4. WHOLE FUNCTIONS ====
# 1) This function takes a length in feet (float) returns the value in meters (float)
def f2m(length: float):
   if length == 0:
       return 0
   return length * 0.3048

# This class represents a MusicalNote object with a pitch and duration attribute (float)
class MusicalNote:
    pitch: float
    duration: float

    # 2) This function initializes the MusicalNote object with a pitch and float value
    def __init__(self, p, d):
        if p <= 0 or d <= 0:
            print("Both pitch and duration must be positive")
            raise ValueError
        self.pitch = p
        self.duration = d

    # 3) This function returns the current note an octave higher
    def up_one_octave(self):
        return self.pitch * 2

    # 4) This function compares the two MusicalNote objects
    def frequency_diff(self, other):
        other: MusicalNote

        top = math.log(self.pitch / other.pitch, 10)
        bottom = math.log(1.05946309436, 10) # the twelfth root of two
        return abs(round(top / bottom, 0))


# ==== 5. WHOLE FUNCTIONS TEST CASES ====
class WholeFunctionTestCases(unittest.TestCase):
    # - F2M -
    def test_f2m_positive(self):
        # Test case for f2m with positive number
        result = f2m(2)
        self.assertEqual(result, 0.6096)

    def test_f2m_zero(self):
        # Test case for f2m with zero
        result = f2m(0)
        self.assertEqual(result, 0)

    def test_f2m_type(self):
        # Test case for f2m with wrong type input
        with self.assertRaises(TypeError):
            f2m(self, "two")

    # - Musical Note -
    def test_musicalNote_invalid_frequency(self):
        # Test case for musicalNote with invalid frequency
        with self.assertRaises(ValueError):
            bad_note = MusicalNote(-1, 1)

    def test_up_one_octave_positive(self):
        # Test case for up_one_octave with positive number
        middle_c = MusicalNote(261.63, 1)
        result = middle_c.up_one_octave()
        self.assertEqual(result, 523.26)

    def test_frequency_diff_positive(self):
        # Test case for frequency_diff with a positive number
        middle_c = MusicalNote(261.63, 1)
        middle_d = MusicalNote(293.665, 1)
        result = middle_c.frequency_diff(middle_d)
        self.assertEqual(result, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    None
