"""class for creating instances of WordFinder"""

from random import choice

class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """initializes word_list to be a list of strings converted from
        the given filepath and invokes method to display number of words
        in file """

        self.word_list = self.convert_file_to_list(path)
        self.display_words_read()

    def convert_file_to_list(self, path):
        """reads the file given the path into a list of strings with the
        new line character removed from each string"""

        converted_list = []
        with open(path, "r") as file:
            # TODO: break parse file into separate function
            for line in file:
                word = self.filter_line_to_word(line)
                if word is not None:
                    converted_list.append(word)
        return converted_list

    def filter_line_to_word(self, line):
        """filter text file line and return word.
        Remove new line chars only"""

        # TODO: use .strip() - takes care of any white space
        word = line.replace("\n", "")
        return word

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

    def filter_line_to_word(self, line):
        """filter text file line and return word.
        Remove new line and any blank words or comments"""

        word = line.replace("\n", "")
        if len(word) > 0 and word[0] != '#':
            return word
        else:
            return None

