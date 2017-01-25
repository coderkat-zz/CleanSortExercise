"""

Sort a list of integers and strings.

This program takes a list of strings containing integers and
words and returns a sorted version of the list.

All words must be in alphabetical order, all integerss sorted numberically.

This keeps element types in the same order (i.e. if the nth element of the
original list is an int, the final nth element must also be an int.)
"""
import sys
import string


def consume_input(filename):
    """Given filename, write to array of strings."""
    with open(filename) as f:
        input_array = f.read().split()
    return(input_array)


def write_to_output(filename, sorted_array):
    """Given our sorted list, convert to string and write to output file."""
    for i in range(len(sorted_array)):
        sorted_array[i] = str(sorted_array[i])
    stringified = ' '.join(sorted_array)

    try:
        with open(filename, 'w') as f:
            f.write(stringified)
    except IOError as e:
        print("IO error: {0}".format(e))


def clean_array(array):
    """Prepare array of given strings for sorting.

    - Remove all special ascii characters that are not letters or digits.
    - Cast any numeric strings to integers.
    - Return cleaned array, as well as arrays of cleaned ints and strs.
    """
    # Create a set of all ascii letters and digits
    # NB: union() like this doesn't work with Python 2.7 or earlier
    ascii_allowed = set().union(*[string.ascii_letters, string.digits])

    strs = []
    ints = []

    for i in range(len(array)):
        # Build new (clean) string as we go
        placeholder = ''

        # If starts with hyphen, might be a negative number: don't lose it.
        if array[i][0] == '-':
            placeholder += '-'

        # cast the word to a set & compare lengths! From the docs(Python3.5):
        # Two sets are equal if and only if every element of each set is
        # contained in the other (each is a subset of the other). A set is
        # less than another set if and only if the first set is a proper subset
        # of the second set (is a subset, but is not equal).
        # A set is greater than another set if and only if the first set is a
        # proper superset of the second set (is a superset, but is not equal).

        if set(array[i]) <= ascii_allowed:
            # we know it's all allowed characters: don't do anything
            placeholder += array[i]

        # Use python's .translate(), which returns a copy of the string in
        # which each character has been mapped through the translation table
        else:
            translation_table = dict.fromkeys(
                map(ord, string.punctuation), None
            )
            placeholder += array[i].translate(translation_table)

        # Check to see if the cleaned string is made of digits, cast to int()
        if placeholder[-1] in string.digits:
            array[i] = int(placeholder)
            ints.append(int(placeholder))
        else:
            # Check to make sure we don't have a erroneous '-' in a string.
            if placeholder[0] == '-':
                placeholder = placeholder[1:]
            array[i] = placeholder
            strs.append(placeholder)

    return(array, strs, ints)


def sort_array(array):
    """Given an array of strings and ints, sort."""
    # Clean string, also returns separated lists of integers and strings.
    cleaned, string_arr, int_arr = clean_array(array)

    # Sort strings and ints.
    string_arr.sort()
    int_arr.sort()

    # Update 'cleaned' in place with sorted ints and strings.
    int_tracker = 0
    str_tracker = 0
    for i in range(len(cleaned)):
        if type(cleaned[i]) == int:
            cleaned[i] = int_arr[int_tracker]
            int_tracker += 1
        else:
            cleaned[i] = string_arr[str_tracker]
            str_tracker += 1

    return(cleaned)


def clean_and_sort(input_file, output_file):
    """Main function to consume file, sort, and write to output."""
    # Read file to get array of strings. If file not found, or other
    # IO exception occurs, print error and gracefully exit.
    try:
        input_array = consume_input(input_file)
    except IOError as e:
        print("IO error: {0}".format(e))
        return

    # If we started with an empty file, don't waste time doing everything here.
    if len(input_array) == 0:
        write_to_output(output_file, input_array)
        return

    # Sort array, keeping types in place.
    sorted_array = sort_array(input_array)

    # Write sorted_array to file:
    write_to_output(output_file, sorted_array)


if __name__ == '__main__':
    # Handle missing args gracefully.
    if not len(sys.argv) == 3:
        print("""
            This program requires exactly two arguments, separated by a space:
            1) the path to the input.txt file, and
            2) the path to result.txt

            $ python3 sort.py path/to/input_file.txt path/to/output_file.txt

            Please try again!
        """)
    else:
        clean_and_sort(sys.argv[1], sys.argv[2])
