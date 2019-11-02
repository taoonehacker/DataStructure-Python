class Array(object):
    __data = []
    __size = 0

    def __init__(self, capacity=10):
        self.__data = [None] * capacity
        self.__size = 0

    def getCapacity(self):
        return self.__data.__len__()

    def getSize(self):
        return self.__size

    def add(self, index, e):
        if index < 0 or index > self.__size:
            raise IndexError("123123")
        for item in range(self.__size, index, -1):
            self.__data[item + 1] = self.__data[item]
        self.__data[index] = e
        self.__size += 1

    def addFirst(self, e):
        self.add(0, e)

    def addLast(self, e):
        self.add(self.__size, e)

    def get(self, index):
        if index < 0 or index > self.__size:
            raise IndexError("Index is required. Index >=0 and Index < size")
        return self.__data[index]

    def set(self, index, e):
        if index < 0 or index > self.__size:
            raise IndexError("Index is required. Index >=0 and Index < size")
        self.__data[index] = e

    def contains(self, e):
        for i in range(0, self.__size):
            if self.__data[i] == e:
                return True
        return False

    def find(self, e):
        for i in range(0, self.__size):
            if self.__data[i] == e:
                return i
        return -1

    def remove(self, index):
        if index < 0 or index > self.__size:
            raise IndexError("Index is required. Index >=0 and Index < size")
        res = self.get(index)
        for i in range(index + 1, self.__size):
            self.__data[i - 1] = self.__data[i]
        self.__size -= 1
        return res
