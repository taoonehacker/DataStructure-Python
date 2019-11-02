import unittest
import os
import sys
from Array import arr

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, path)


class ArrayTest(unittest.TestCase):

    def test_getCapacity(self):
        array = arr.Array(10)
        self.assertEqual(10, array.getCapacity())

    def test_getSize(self):
        array = arr.Array(10)
        self.assertEqual(0, array.getSize())

    def test_add(self):
        array = arr.Array(10)
        for i in range(5):
            array.add(i, i)
        self.assertEqual(5, array.getSize())

    def test_addFirst(self):
        array = arr.Array(10)
        for i in range(5):
            array.addFirst(i)
        self.assertEqual(5, array.getSize())

    def test_addLast(self):
        array = arr.Array(10)
        for i in range(5):
            array.addLast(i)
        self.assertEqual(5, array.getSize())

    def test_get(self):
        array = arr.Array(10)
        for i in range(5):
            array.addLast(i)
        self.assertEqual(3, array.get(3))

    def test_set(self):
        array = arr.Array(10)
        for i in range(5):
            array.addLast(i)
        array.set(3, 20)

        self.assertEqual(20, array.get(3))

    def test_contains(self):
        array = arr.Array(10)
        for i in range(10):
            array.addLast(i)
        self.assertTrue(array.contains(3))
        self.assertFalse(array.contains(20))

    def test_find(self):
        array = arr.Array(10)
        for i in range(10):
            array.addLast(i)
        self.assertEqual(3, array.find(3))
        self.assertEqual(-1, array.find(20))

    def test_remove(self):
        array = arr.Array(10)
        for i in range(10):
            array.addLast(i)

        array.remove(3)
        self.assertEqual(4, array.get(3))
