from letterManager import *


class AnagramSolver:
    def __init__(self, list_of_words):
        self._words = list_of_words
        self._choices = []
        self._letters = ''
        self._answer = []
        self._max = 0
        self._letterManager = [LetterManager(i) for i in self._words]

    def generateAnagrams(self, s, max):     # -------------------------------------------------------------------------
        """ (string, int) -> list of lists
        Return all combinations of words from given dict that are anagrams of the
        String s and that include at most max words (unlimited words if max is 0).

        >>> words = open('dict.txt').read().split()
        >>> x = AnagramSolver(words)
        >>> x.generateAnagrams('office key', 0)
        [['eke', 'icy', 'off'], ['eke', 'off', 'icy'], ['ice', 'key', 'off'], ['ice', 'off', 'key'],\
 ['icy', 'eke', 'off'], ['icy', 'off', 'eke'], ['key', 'ice', 'off'], ['key', 'off', 'ice'],\
 ['key', 'office'], ['off', 'eke', 'icy'], ['off', 'ice', 'key'], ['off', 'icy', 'eke'],\
 ['off', 'key', 'ice'], ['office', 'key']]
        >>> x.generateAnagrams('office key', 2)
        [['key', 'office'], ['office', 'key']]
        >>> x.generateAnagrams('sunset', 1)
        [['sunset']]
        """
        # resets answers every time new phrase is given just in case if same object reference used.
        self._answer = []

        if max < 0:
            raise ValueError
        elif max == 0:
            self._max = len(s)
        else:
            self._max = max

        self._letters = LetterManager(s)
        self._choices = self.word_choices(self._letters, self._letterManager)

        for word in self._choices:
            remains = self._letters
            result = self.recursive(word, remains)
            #if result is str, then word == s, thus, append word into answers
            if isinstance(result, str):
                self._answer.append([result])
            else:
                for i in result:
                    if len(i) <= self._max:
                        self._answer += [i]


        self._letters == LetterManager('')
        self._choices = []
        return self._answer

    def recursive(self, word, remains):     # -------------------------------------------------------------------------
        """(LetterManager Object, LetterManager Object, integer) -> List
        Creates anagrams for new_letters and adds then to the master list(self._answer).

        p keeps track of what the last subtracted word was.
        base is to know whether the recursive is inside a recursive or has it been called only once.
        """
        result = []

        new_word = remains.Subtract(word)
        remains = new_word

        #BaseCase
        if str(new_word) == '':
            result = word.letters
        #RecursiveStep
        elif new_word is not None:
            # New set of words that are possible anagram bits
            new_list = self.word_choices(new_word, self._choices)
            for i in new_list:
                # call recursive function
                anagram = self.recursive(i, remains)
                if anagram == []:
                    pass
                elif isinstance(anagram, str):
                    result.append([word.letters] + [anagram])
                elif isinstance(anagram, list):
                    for j in anagram:
                        result += [[word.letters] + j]
        return result

    def word_choices(self, letters, lst):
        """(LetterManager Object) -> List of LetterManager Objects
        Returns a shortened list from provided lst with possible anagrams of letters.
        """
        choices = []
        for i in lst:
            if letters.Subtract(i) is not None:
                choices.append(i)
        return choices


# TEST PURPOSES ONLY. DO NOT MARK THE FOLLOWING.
words = open('dict.txt').read().split()
#
import time
x = AnagramSolver(words)
start_time = time.time()
anagrams = x.generateAnagrams('', 0)
print('Program took:', time.time() - start_time, 's to run')
print(x._answer)

