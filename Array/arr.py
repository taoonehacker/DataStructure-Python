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
