import tkinter as tk
import lib.models as models
from lib.models import SnakeObj
from lib.vector import Vector2

import time

class Application(tk.Frame):
    def moveUp(self, event):
        self.my_snake.blocks[0].direction = Vector2(0, -1)

    def moveDown(self, event):
        self.my_snake.blocks[0].direction = Vector2(0, 1)

    def moveRight(self, event):
        self.my_snake.blocks[0].direction = Vector2(1, 0)

    def moveLeft(self, event):
        self.my_snake.blocks[0].direction = Vector2(-1, 0)

    def __init__(self, master=None):
        self.w=400
        self.h=400

        tk.Frame.__init__(self, master)
        self.master.minsize(width=self.w, height=self.h)
        self.master.maxsize(width=self.w, height=self.h)
        self.canvas = tk.Canvas(master, height=self.h, width=self.w)
        self.canvas.pack()
        self.my_snake = SnakeObj(20)
        self.my_snake.addBlocks(3)
        self.my_snake.render(self.canvas)

        self.master.bind('<Left>', self.moveLeft)
        self.master.bind('<Right>', self.moveRight)
        self.master.bind('<Up>', self.moveUp)
        self.master.bind('<Down>', self.moveDown)

    def moveAll(self):
        self.my_snake.move(self.w, self.h)

    def renderAll(self):
        self.canvas.delete("all")
        self.my_snake.render(self.canvas)

    def loop(self):
        while(True):
            self.master.update_idletasks()
            self.master.update()
            self.moveAll()
            self.renderAll()
            time.sleep(1)
