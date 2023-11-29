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
            for line in file:
                line = line.replace("\n", "")
                converted_list.append(line)
        return converted_list

    def display_words_read(self):
        """prints out in a formatted string the number of words read
        in the file"""

        print(f"{len(self.word_list)} words read")

    def random(self):
        """utilizing the random library's choice method returns
        a random string from the instance's word list"""

        return choice(self.word_list)
