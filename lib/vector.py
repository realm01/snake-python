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
