""" serial number generator """

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate() == 100
    True

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

        self.start = self.next = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """add number to current number and return number -1"""

        self.next += 1

        return self.next - 1

    def reset(self):
        """reset current number to start"""

        self.next = self.start

