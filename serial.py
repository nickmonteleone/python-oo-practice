""" serial number generator """

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """initialize current number as None and record start"""

        self.start = self.current_number = start

    def generate(self):
        """add number to current number and return number -1"""

        self.current_number += 1

        return self.current_number - 1

    def reset(self):
        """reset current number to start"""

        self.current_number = self.start

