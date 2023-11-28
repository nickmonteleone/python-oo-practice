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

        self.start = start
        self.current_number = None

    def generate(self):
        """add number to current number if not None and return
        for current number None (initial value) set to start and return"""

        if self.current_number is None:
            self.current_number = self.start
        else:
            self.current_number += 1

        return self.current_number

    def reset(self):
        """reset current number to None to restart at start """

        self.current_number = None

