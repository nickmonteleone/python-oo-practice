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

    def __init__(self, start):
        """initialize current number as 1 before start input"""

        self.start = start
        self.current_number = None

    def generate(self):
        """add number to current number and return"""

        if self.current_number is None:
            self.current_number = self.start
        else:
            self.current_number += 1

        return self.current_number

    def reset(self):
        """return current number to starting position"""

        self.current_number = None

