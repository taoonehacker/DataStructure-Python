import unittest
from array import Array

class ArrayTest(unittest.TestCase):

    def getCapacityTest(self):
        array = Array()
        self.assertEqual(array, 10, array.getCapacity())
