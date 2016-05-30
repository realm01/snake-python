'''
Created by: Anastassios Martakos

Copyright 2016 Anastassios Martakos

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
'''

class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

        return self

    def __str__(self):
        return str(self.x) + ", " + str(self.y)

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __ne__(self, other):
        return True if self.x != other.x or self.y != other.y else False

    def vecxScalar(self, scalar):
        return Vector2(self.x * scalar, self. y * scalar)
