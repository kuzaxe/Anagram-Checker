import unittest
from anagram import *

words = open('dict.txt').read().split()


class AnagramTest(unittest.TestCase):
    """
    The following test cases test are sufficient to conclude that my implementation is correct because:
    ()- covers empty strings entered by user
    ()- covers string lengths of 1 and of 2+ entered by the user
    ()- covers if the result is printed out alphabetically
    ()- covers all possible cases around 0 for max (which include -1, 0, 1, 2)
    ()- covers trick cases such as:
     )(   - 'keykey' where the input has two same words
    - Along with these various boundary cases, a few other test cases are
      added that test helper functions and other factors to assure that the program works correctly.
    """

    def setUp(self):
        self.x = AnagramSolver(words)

    def test01_string_max_0(self):
        """ this is necessary to test when max = 0, does the function allow unlimited entries in an anagram list. """
        r = self.x.generateAnagrams('office key', 0)
        y = [['eke', 'icy', 'off'], ['eke', 'off', 'icy'], ['ice', 'key', 'off'], ['ice', 'off', 'key'], ['icy', 'eke', 'off'], ['icy', 'off', 'eke'], ['key', 'ice', 'off'], ['key', 'off', 'ice'], ['key', 'office'], ['off', 'eke', 'icy'], ['off', 'ice', 'key'], ['off', 'icy', 'eke'], ['off', 'key', 'ice'], ['office', 'key']]
        self.assertEqual(y, r, "Test 01 failed in class AnagramTest")

    def test02_string_max_1(self):
        """ this is necessary to test boundary cases of max. When max = 1,
        does the output only return answers of length 1"""
        r = self.x.generateAnagrams('office', 1)
        y = [['office']]
        self.assertEqual(y, r, "Test 02 failed in class AnagramTest")

    def test03_string_max_2(self):
        """ this is necessary to test boundary cases for max. When max > 1,
        does the output only contain max or less length anagram answers"""
        r = self.x.generateAnagrams('office key', 2)
        y = [['key', 'office'], ['office', 'key']]
        self.assertEqual(y, r, "Test 03 failed in class AnagramTest")

    def test04_string_max_minus1(self):
        """ this is necessary to test boundary case for max. When max < 0,
        does the output raise a ValueError indicating input is right type but not acceptable"""
        self.assertRaises(ValueError, lambda: self.x.generateAnagrams('office', -1))

    def test05_empty_string(self):
        """ this is to test boundary cases of s (user input). Testing if program returns empty list"""
        r = self.x.generateAnagrams('', 0)
        y = []
        self.assertEqual(y, r, "Test 05 failed in class AnagramTest")

    def test06_one_char_str(self):
        """ this is to test boundary cases of s (user input). Testing if program returns the character or an empty list
        depending on the given dictionary."""
        r = self.x.generateAnagrams('a', 0)
        y = []
        self.assertEqual(y, r, "Test 06 failed in class AnagramTest")

    def test07_multiple_same_words(self):
        """ this is to test the use of the helper function and check if an anagram part can be repeated again."""
        r = self.x.generateAnagrams('keykey', 0)
        y = [['key', 'key']]
        self.assertEqual(y, r, "Test 07 failed in class AnagramTest")

    def test08_fulldict_to_small(self):
        """ this is to test use of the helper function and check if it returns, alphabetically, a shortened list of
        possible anagrams to use for the given word."""
        r = self.x.word_choices(LetterManager('officekey'), self.x._letterManager)
        for i in range(len(r)):
            wrd = r.pop(i)
            r.insert(i, wrd.letters)
        y =['coffee', 'coke', 'coy', 'eke', 'eye', 'fee', 'fief', 'fife', 'foci','foe', 'ice', 'icky', 'icy', 'iffy', 'key', 'off', 'office', 'yoke']
        self.assertEqual(y, r, "Test 08 failed in class AnagramTest")

    def test09_fulldict_to_small_2(self):
        """ this is same as above but it calls the function twice to check if it
        efficiently creates smaller and smaller lists.
        """
        r = self.x.word_choices(LetterManager('officekey'), self.x._letterManager)
        s = self.x.word_choices(LetterManager('office'), r)
        for i in range(len(s)):
            wrd = s.pop(i)
            s.insert(i, wrd.letters)
        y = ['fief', 'fife', 'foci', 'foe', 'ice', 'off', 'office']
        self.assertEqual(y, s, "Test 09 failed in class AnagramTest")

if __name__ == "__main__":
    unittest.main()
