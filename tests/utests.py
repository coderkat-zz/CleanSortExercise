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
    sort_array,
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
        input_string = 'Hel&lo!'
        input_int = '~12#3@4'
        self.dirty_array = [input_string, input_int]
        self.expected_str = 'Hello'
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

    def setUp(self):
        """Create a string_lists to sort and int_lists to sort."""
        self.original_list = ['hello', 1, 4, 0, 'banana', 'a', -30, 'zed', 2]
        self.sorted_list = ['a', -30, 0, 1, 'banana', 'hello', 2, 'zed', 4]
        self.just_ints = [1, 5, 0, -2, 3, -20, 400]
        self.just_strs = ['hello', 'a', 'zed', 'banana', 'cats', 'aaa']

    def test_sort_array_does_not_change_len(self):
        """Make sure we aren't losing or adding anything."""
        sorted_arr = sort_array(self.original_list)
        self.assertEqual(len(sorted_arr), len(self.original_list))

    def test_sort_array_honors_type_at_index(self):
        """Each index should honor type of original array at that index."""
        sorted_arr = sort_array(self.original_list)
        for i in range(len(self.original_list)):
            self.assertEqual(type(self.original_list[i]), type(sorted_arr[i]))

    def test_sort_array_only_ints(self):
        """Test that method works if only ints in original array."""
        sorted_ints = sort_array(self.just_ints)
        self.assertEqual(sorted_ints, sorted(self.just_ints))

    def test_sort_array_only_strs(self):
        """Test that method works if only strings in original array."""
        sorted_strs = sort_array(self.just_strs)
        self.assertEqual(sorted_strs, sorted(self.just_strs))

    def test_sort_array_handles_empty_list(self):
        """Handle case of an empty file, aka empty list."""
        sorted_arr = sort_array([])
        self.assertEqual(sorted_arr, [])


if __name__ == '__main__':
    unittest.main()
