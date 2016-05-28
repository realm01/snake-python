import tkinter as tk
import lib.models as models
from lib.models import SnakeObj, Movement, Food
from lib.vector import Vector2

import time

class Application(tk.Frame):
    def moveUp(self, event):
        self.my_snake.blocks[0].updateAllDir(Movement.UP)

    def moveDown(self, event):
        self.my_snake.blocks[0].updateAllDir(Movement.DOWN)

    def moveRight(self, event):
        self.my_snake.blocks[0].updateAllDir(Movement.RIGHT)

    def moveLeft(self, event):
        self.my_snake.blocks[0].updateAllDir(Movement.LEFT)

    def __init__(self, master=None):
        self.w=400
        self.h=400
        self.scale = 20

        tk.Frame.__init__(self, master)
        self.master.minsize(width=self.w, height=self.h)
        self.master.maxsize(width=self.w, height=self.h)
        self.canvas = tk.Canvas(master, height=self.h, width=self.w)
        self.canvas.pack()
        self.restart()
        self.renderAll()

        self.master.bind('<Left>', self.moveLeft)
        self.master.bind('<Right>', self.moveRight)
        self.master.bind('<Up>', self.moveUp)
        self.master.bind('<Down>', self.moveDown)

    def moveAll(self):
        self.my_snake.move(self.w, self.h)

    def calcCollision(self):
        if(self.my_snake.blocks[0].pos == self.food.pos):
            self.my_snake.addBlocks(1)
            self.food.randomize()

        for block in self.my_snake.blocks:
            if(self.my_snake.blocks[0].pos == block.pos and self.my_snake.blocks[0] is not block):
                self.restart()

    def renderAll(self):
        self.canvas.delete("all")
        self.my_snake.render(self.canvas)
        self.food.render(self.canvas)

    def loop(self):
        while(True):
            self.master.update_idletasks()
            self.master.update()
            self.moveAll()
            self.calcCollision()
            self.renderAll()
            time.sleep(0.14)


    def restart(self):
        self.my_snake = SnakeObj(self.scale)
        self.my_snake.addBlocks(3)
        self.food = Food(self.w, self.h, self.scale)
