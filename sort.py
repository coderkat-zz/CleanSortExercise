"""

Sort a list of integers and strings.

Write a program that takes a list of strings containing integers and
words and returns a sorted version of the list.

All words must be in alphabetical order, all ints sorted numberically.

Keep element types in the same order (i.e. if the nth element is an int,
the final nth element must also be an int.)
"""
import sys
import string

# Create a set of all ascii letters and digits
ascii_allowed = set()
for x in [string.ascii_letters, string.digits]:
    ascii_allowed.update(x)

# NOTE TO SELF: union like this doesn't work with Python 2.7 or earlier
# ascii_allowed = set().union(*[string.ascii_letters, string.digits])


def sort_strings(s):
    """Sort strings into a-z order."""
    return()


def sort_ints(i):
    """Sort ints smallest to largest."""
    return()


def consume_input(f):
    """Given file f, write to array of strings."""
    input_array = []
    return(input_array)


def clean_array(dirty_array):
    """Prepare array for sorting.

    Remove all special ascii characters that are not letters or digits.
    Cast any number strings to int.
    Return cleaned array.
    """
    # TODO: do we need to have an exception for something that's just
    # unallowed chars?

    # given arr of strings
    # for each string in array:
    # look for ascii neither belonging to letter set nor digit set
    # if ascii there, remove it
    # if string remaining is just made of ints, cast to int

    clean_array = []
    for d in dirty_array:
        # Build new string as we go
        placeholder = ''
        # Initialize is_digit to false
        is_digit = False
        # Check each character in this string. If it is not in our allowed list
        # skip it. Otherwise, add to placeholder and check if it is a digit.
        # TODO: will I ever have a string that has a digit in it?????? re-read
        # directions.
        for character in d:
            if character in ascii_allowed:
                placeholder += character
                if character in string.digits:
                    is_digit = True
            else:
                continue
        if is_digit:
            clean_array.append(int(placeholder))
        else:
            clean_array.append(placeholder)

    return(clean_array)


def sort_array(array):
    """Given an array of strings and ints, sort."""
    # Get
    return()


def clean_and_sort(input_file, output_file):
    """Main function to consume file, sort, and write to output."""
    input_array = consume_input(input_file)
    cleaned_array = clean_array(input_array)
    sorted_array = sort_array(cleaned_array)
    return(sorted_array)


if __name__ == '__main__':
    # Handle missing args gracefully.
    if not len(sys.argv) == 3:
        print("""
            This program requires exactly two arguments:
            1) the path to the input.txt file, and
            2) the path to result.txt

            Please try again!
        """)
    else:
        clean_and_sort(sys.argv[1], sys.argv[2])
