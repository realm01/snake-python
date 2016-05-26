from lib.vector import Vector2

class Base():
    def __init__(self, scale=1, pos=Vector2(0, 0)):
        self.scale = scale
        self.pos = pos

class Movement():
    def __init__(self):
        self.direction = [ Vector2(-1, 0) ]

class Mesh(Base):
    def __init__(self, scale=1, pos=Vector2(0, 0), mesh=[]):
        Base.__init__(self, scale, pos)
        self.mesh = mesh

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
        print(tmp_mesh)
        canvas.create_polygon(tmp_mesh, outline="green")


class Block(Mesh, Movement):
    def __init__(self, scale=1, pos=Vector2(0, 0)):
        Mesh.__init__(self, scale, pos, [0, 0,  0, 1,  1, 1,  1, 0])
        Movement.__init__(self)

class SnakeObj(Base):
    def __init__(self, scale=1, pos=Vector2(0, 0)):
        Base.__init__(self, scale, pos)
        self.blocks = []

    def addBlocks(self, count):
        for i in range(count):
            pos_last = self.blocks[len(self.blocks) - 1].pos if len(self.blocks) - 1 != -1 else Vector2(-1, 0)
            self.blocks.append(Block(self.scale, Vector2(pos_last.x + 1, pos_last.y)))

    def render(self, canvas):
        for block in self.blocks:
            block.render(canvas, self.pos)

    def move(self, w, h):
        local_w = int(w / self.scale) - 1
        local_h = int(h / self.scale) - 1

        last = self.blocks[0]

        for block in self.blocks:
            block.direction.insert(0, last.direction[len(last.direction) - 1])
            last = block

            block.pos += block.direction.pop()

            if block.pos.x < 0:
                block.pos.x = local_w
            elif block.pos.x > local_w:
                block.pos.x = 0

            if block.pos.y < 0:
                block.pos.y = local_h
            elif block.pos.y > local_h:
                block.pos.y = 0
