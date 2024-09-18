from main import *

def test_sum_two_numbers():
    assert sum_two_numbers(1,1) == 2
    assert sum_two_numbers(100,1) == 101
    assert sum_two_numbers(99,-1) == 98
    assert sum_two_numbers(-99,1) == -98

def test_is_even():
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(99) == False

def test_absolute_difference():
    assert absolute_difference(11,6) == 5
    assert absolute_difference(1,21) == 20
    assert absolute_difference(-2,-99) == 97
    assert absolute_difference(-33,3) == 36

def test_largest_of_three():
    assert largest_of_three(1,2,3) == 3
    assert largest_of_three(1,-2,-3) == 1
    assert largest_of_three(111,111,23) == 111
    assert largest_of_three(-91,-2,-2) == -2

def test_is_vowel():
    assert is_vowel("A") == True
    assert is_vowel("i") == True
    assert is_vowel("D") == False
    assert is_vowel("q") == False

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0

def test_is_leap_year():
    assert is_leap_year(1900) == False
    assert is_leap_year(2024) == True
    assert is_leap_year(2000) == True
    assert is_leap_year(2022) == False