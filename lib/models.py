from lib.vector import Vector2
from random import randint

class Base():
    def __init__(self, scale=1, pos=Vector2(0, 0)):
        self.scale = scale
        self.pos = pos

class Movement():
    UP         = Vector2(0, -1)
    DOWN       = Vector2(0, 1)
    LEFT       = Vector2(-1, 0)
    RIGHT      = Vector2(1, 0)

    def __init__(self):
        self.direction = self.LEFT
        self.last_direction = self.LEFT

    def updateAllDir(self, vec, prev):
        self.direction = vec if Movement.getOpposite(vec) != self.direction and Movement.getOpposite(vec) != prev.last_direction else self.direction
        self.last_direction = vec if Movement.getOpposite(vec) != self.direction and Movement.getOpposite(vec) != prev.last_direction else self.direction

    @staticmethod
    def getOpposite(vec):
        return vec.vecxScalar(-1)


class Mesh(Base):
    def __init__(self, scale=1, pos=Vector2(0, 0), mesh=[], color = "black"):
        Base.__init__(self, scale, pos)
        self.mesh = mesh
        self.color = color

    def render(self, canvas, modifier=Vector2(0, 0)):
        tmp_mesh = list(self.mesh)
        x = True
        for i in range(len(tmp_mesh)):
            if x == True:
                tmp_mesh[i] = tmp_mesh[i] * self.scale + self.pos.x * self.scale + modifier.x * self.scale
                x = False
            else:
                tmp_mesh[i] = tmp_mesh[i] * self.scale + self.pos.y * self.scale + modifier.y * self.scale
                x = True
        canvas.create_polygon(tmp_mesh, fill=self.color)


class Block(Mesh, Movement):
    def __init__(self, scale=1, pos=Vector2(0, 0), color="black"):
        Mesh.__init__(self, scale, pos, [0, 0,  0, 1,  1, 1,  1, 0], color)
        Movement.__init__(self)

class Food(Block):
    def __init__(self, w, h, scale=1, color="red"):
        Block.__init__(self, scale, Vector2(0, 0), color)
        self.w = w
        self.h = h
        self.randomize()

    def randomize(self):
        local_w = int(self.w / self.scale) - 1
        local_h = int(self.h / self.scale) - 1
        self.pos = Vector2(randint(0, local_w), randint(0, local_h))

class SnakeObj(Base):
    def __init__(self, scale=1, pos=Vector2(0, 0), color="green"):
        Base.__init__(self, scale, pos)
        self.blocks = []
        self.color = color

    def addBlocks(self, count):
        for i in range(count):
            last_block = self.blocks[len(self.blocks) - 1] if len(self.blocks) - 1 != -1 else Block(1, Vector2(-1, 0))

            self.blocks.append(Block(self.scale, Vector2(last_block.pos.x - last_block.direction.x, last_block.pos.y - last_block.direction.y), self.color))
            self.blocks[len(self.blocks) - 1].last_direction = last_block.direction

    def render(self, canvas):
        for block in self.blocks:
            block.render(canvas, self.pos)

    def getScore(self):
        return len(self.blocks) - 3 if len(self.blocks) >= 3 else 0

    def move(self, w, h):
        local_w = int(w / self.scale) - 1
        local_h = int(h / self.scale) - 1

        last = self.blocks[0]

        for block in self.blocks:
            block.direction = block.last_direction
            block.pos += block.direction
            block.last_direction = last.direction

            last = block

            if block.pos.x < 0:
                block.pos.x = local_w
            elif block.pos.x > local_w:
                block.pos.x = 0

            if block.pos.y < 0:
                block.pos.y = local_h
            elif block.pos.y > local_h:
                block.pos.y = 0
