import unittest
import os
import sys
from Array import arr

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)


class ArrayTest(unittest.TestCase):
    __array = arr.Array(10)

    def setUp(self):
        __array = arr.Array(10)

    # def tearDown(self):
    #     print("Test End")

    def test_getCapacity(self):
        self.assertEqual(10, self.__array.getCapacity())

    def test_getSize(self):
        self.assertEqual(0, self.__array.getSize())

    def test_add(self):
        for i in range(5):
            self.__array.add(i, i)
        self.assertEqual(5, self.__array.getSize())

    def test_addFirst(self):
        for i in range(5):
            self.__array.addFirst(i)
        self.assertEqual(5, self.__array.getSize())

    def test_addLast(self):
        for i in range(5):
            self.__array.addLast(i)
        self.assertEqual(5, self.__array.getSize())


