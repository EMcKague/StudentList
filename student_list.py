# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def append(self, val):
        # print("value being added", val)
        if self._capacity > self._size:
            storage_container = self._list[:]
            storage_container[self._size:self._size + 1] = [val]
            # print("storage_container after adding val", storage_container)
            self._size += 1
            self._list[:] = storage_container[:]

        else:
            storage_container = []
            self.move_list_to_storage(storage_container)
            storage_container.append(val)
            self._size += 1
            self.increase_capacity()
            self.move_storage_to_list(storage_container)

        return

    def pop(self):
        # remove the last element in the array
        storage_container = []
        self.move_list_to_storage(storage_container)
        for el in range(self._size):
          if el == self._size - 1:
            popped_num = storage_container[el]

        storage_container[:] = storage_container[:-1]
        # print(storage_container)
        self._size -= 1
        self.move_storage_to_list(storage_container)

        return popped_num

    def insert(self, index, val):

        storage_container = []
        self.create_storage_container(storage_container)

        if index == 0:
            storage_container[:index] = [val]
            # print("index was at 0, new container:", storage_container)
        elif index > self._size:
            storage_container[self._size:] = [val]
        else:
            storage_container[index + 1: len(storage_container) + 1] = storage_container[index:len(storage_container)]
            storage_container[index:index + 1] = [val]
        self._size += 1
        if self._size > self._capacity:
            self.increase_capacity()
        self.move_storage_to_list(storage_container)

    def remove(self, val):
        storage_container = []
        self.create_storage_container(storage_container)
        # print(self._size)
        for el in range(self._size):
            # print(el, storage_container[el])
            if storage_container[el] == val:
                # print("test1", storage_container[:el])
                # print("test2", storage_container[el+1:-1])
                storage_container = storage_container[:el] + storage_container[el+1:-1]
                # print("test3", storage_container)
                self._size -= 1
                self.move_storage_to_list(storage_container)
                return
        # print("removed "+ str(val) + ".", storage_container)

    def clear(self):
        # for el in self._list:
        #   self.remove(el)
        self._list = np.empty([0], np.int16)

    def count(self, val):
        i = 0
        for el in self._list:
            if el == val:
                i += 1
        return i

    def get(self, index):
        i = 0
        for el in self._list:
            if i == index:
                return self._list[i]
            else:
                i += 1

    def create_storage_container(self, some_list):
        for element in self._list:
            some_list.append(element)
        return some_list

    def increase_capacity(self):
        self._capacity = self._capacity * 2
        self._list = np.empty([self._capacity], np.int16)

    def decrease_capacity(self):
        self._capacity = self._capacity / 2
        self._list = np.empty([self._capacity], np.int16)

    def move_storage_to_list(self, some_list):
        for el in range(self._size):
            self._list[el] = some_list[el]

    def move_list_to_storage(self, somelist):
        for element in self._list:
            somelist.append(element)
        return somelist

# Slist = StudentList()
# Slist.append(238)
# print(Slist.get_list())
# Slist.append(60)
# print(Slist.get_list())
# Slist.append(20)
# print(Slist.get_list())
# Slist.append(20)
# print(Slist.get_list())
# Slist.append(20)
# print(Slist.get_list())
# Slist.append(20)
# print(Slist.get_list())
# Slist.append(40)
# print(Slist.get_list())
# Slist.append(500)
# print(Slist.get_list())
# Slist.append(600)
# print(Slist.get_list())
# Slist.pop()
# print(Slist.get_list())
# print("insert 10 @ 2")
# Slist.insert(2, 10)
# print(Slist.get_list())
# print("remove first 20")
# Slist.remove(20)
# print(Slist.get_list())
# Slist.clear()
# print("list should be cleared")
# print(Slist.get_list())
# print(Slist.count(20))
# print(Slist.get_list())
# print(Slist.get(6))