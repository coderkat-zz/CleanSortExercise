# CleanSortExercise
A python program that cleans an input string of non-letter, non-digit characters and then sorts.

The challenge at hand is to sort a list of integers and strings.
* This program takes a list of strings (from a .txt file) containing integers and
words and returns a sorted version of the list.
* Input given may contain non-letter, non-digit characters. Remove any such characters
before sorting.
* All words must be in alphabetical order, all integerss sorted numberically.
* This keeps element types in the same order (i.e. if the nth element is an
int, the final nth element must also be an int.)
* Program prints cleaned/sorted list to a new text file

Example input: `20 cat bi?rd 12 do@g`
Desired output: `12 bird cat 20 dog`

## Instructions for running the code
To try this yourself:
Using Python3, simply
```
$ python sort.py path/to/inputfile.txt path/to/outputfile.txt
```

To run unit tests:
```
$ python -m unittest tests/utests.py
```

If your system isn't set up to use Python3 by default, you can spin
up a virtual environment to do so for this program! Follow this
[guide to virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
