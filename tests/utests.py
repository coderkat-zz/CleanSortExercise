"""

Unittests to run for sort.py challenge.

Test:
- Can consume an empty file.
- I write what I expect I will to my array.
- clean_data removes ascii special characters
- all ints are cast to int
- alphasort works
- numsort works
- check that final_arr types follow og_array pattern
    (i.e. if type(og_pattern[n] == int, type(final_arr[n]) == int)
"""

import unittest

from sort import (
    clean_array,
)


# class TestFileMethods(unittest.TestCase):
#     """Tests for reading/writing to/from files."""

    # def test_file_empty_graceful(self):
    #     """Test that an empty file can be handled gracefully."""
    #     pass

    # def test_print_output(self):
    #     """Array prints as we'd expect to result.txt."""
    #     pass


class TestTextManipulationMethods(unittest.TestCase):
    """Tests for cleaning, type-manipulation, etc."""

    def setUp(self):
        """Create string and int for string manipulation testing."""
        input_string = "Hel&lo!"
        input_int = "~12#3@4"
        self.dirty_array = [input_string, input_int]
        self.expected_str = "Hello"
        self.expected_int = 1234

    def test_clean_data_does_not_change_arr_length(self):
        """Test that the array stays the same length after we clean it."""
        cleaned = clean_array(self.dirty_array)
        self.assertEqual(len(cleaned), len(self.dirty_array))

    def test_clean_data_removes_chars(self):
        """Test that special characters like "$" are removed."""
        cleaned = clean_array(self.dirty_array)
        self.assertEqual(cleaned[0], self.expected_str)
        self.assertEqual(cleaned[1], self.expected_int)

    def test_all_numbers_to_int(self):
        """Test that all strs containing numbers are cast to ints."""
        cleaned = clean_array(self.dirty_array)
        self.assertEqual(type(cleaned[1]), int)


class TestSortMethods(unittest.TestCase):
    """Test sorting of strings and ints."""

    # def test_alpha_sort(self):
    #     """Sort strings in alpha order correctly."""
    #     pass

    # def test_int_sort(self):
    #     """Sort ints correctly, smallest to largest."""
    #     pass


if __name__ == '__main__':
    unittest.main()
