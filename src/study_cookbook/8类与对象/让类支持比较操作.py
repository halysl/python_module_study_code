# -*- coding: utf-8 -*-
# 通过 functools.total_ordering 简化比较的操作
# python 的类 可以通过 __eq__ __lt__ __le__ __gt__ __ge__ 等魔术方法对类的某个属性做比较
# 但是全写显得复杂，可以简化

from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return "{}: {} square foot {}".format(self.name,
                                              self.living_space_footage,
                                              self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


def example_total_ordering():
    # Build a few houses, and add rooms to them
    h1 = House('h1', 'Cape')
    h1.add_room(Room('Master Bedroom', 14, 21))
    h1.add_room(Room('Living Room', 18, 20))
    h1.add_room(Room('Kitchen', 12, 16))
    h1.add_room(Room('Office', 12, 12))
    h2 = House('h2', 'Ranch')
    h2.add_room(Room('Master Bedroom', 14, 21))
    h2.add_room(Room('Living Room', 18, 20))
    h2.add_room(Room('Kitchen', 12, 16))
    h3 = House('h3', 'Split')
    h3.add_room(Room('Master Bedroom', 14, 21))
    h3.add_room(Room('Living Room', 18, 20))
    h3.add_room(Room('Office', 12, 16))
    h3.add_room(Room('Kitchen', 15, 17))
    houses = [h1, h2, h3]
    print('Is h1 bigger than h2?', h1 > h2)  # prints True
    print('Is h2 smaller than h3?', h2 < h3)  # prints True
    print('Is h2 greater than or equal to h1?', h2 >= h1)  # Prints False
    # Prints 'h3: 1101-square-foot Split'
    print('Which one is biggest?', max(houses))
    # Prints 'h2: 846-square-foot Ranch'
    print('Which is smallest?', min(houses))

if __name__ == "__main__":
    example_total_ordering()
