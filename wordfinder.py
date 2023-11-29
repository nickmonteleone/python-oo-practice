"""class for creating instances of WordFinder"""

from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> word_finder = WordFinder('./words.txt')
    8 words read

    >>> word_finder.word_list
    ['cat', 'dog', 'porcupine', 'rithm', 'Eric', 'Nick', 'dark', 'learning']

    >>> word_finder.random() in word_finder.word_list
    True

    """

    def __init__(self, path):
        """initializes word_list to be a list of strings converted from
        the given filepath and invokes method to display number of words
        in file """

        self.word_list = self.convert_file_to_list(path)
        self.display_words_read()

    def convert_file_to_list(self, path):
        """reads the file given the path into a list of strings with the
        new line character removed from each string"""
        with open(path, "r") as file:
            converted_list = self.filter_file_to_words(file)
        return converted_list

    def filter_file_to_words(self, file):
        """filter text file line and return word.
        Remove new line chars only"""

        converted_list = []
        for line in file:
            word = line.strip("\n").strip("\r")
            converted_list.append(word)
        return converted_list

    def display_words_read(self):
        """prints out in a formatted string the number of words read
        in the file"""

        print(f"{len(self.word_list)} words read")

    def random(self):
        """utilizing the random library's choice method returns
        a random string from the instance's word list"""

        return choice(self.word_list)


class SpecialWordFinder(WordFinder):
    """Modified word finder sub class to also filter out comments
    and blank lines from file input"""

    def filter_file_to_words(self, file):
        """filter text file line and return word.
        Remove new line and any blank words or comments"""

        converted_list = []
        for line in file:
            word = line.strip("\n").strip("\r")
            if len(word) > 0 and word[0] != '#':
                converted_list.append(word)
        return converted_list

