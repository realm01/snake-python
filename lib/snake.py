import tkinter as tk
import lib.models as models
from lib.models import SnakeObj, Movement, Food
from lib.vector import Vector2

import time

class Application(tk.Frame):
    STARTED = 0
    PAUSED = 1
    MAINMENU = 2

    def moveUp(self, event):
        if self.game_stat != self.MAINMENU:
            self.my_snake.blocks[0].updateAllDir(Movement.UP, self.my_snake.blocks[1])

    def moveDown(self, event):
        if self.game_stat != self.MAINMENU:
            self.my_snake.blocks[0].updateAllDir(Movement.DOWN, self.my_snake.blocks[1])

    def moveRight(self, event):
        if self.game_stat != self.MAINMENU:
            self.my_snake.blocks[0].updateAllDir(Movement.RIGHT, self.my_snake.blocks[1])

    def moveLeft(self, event):
        if self.game_stat != self.MAINMENU:
            self.my_snake.blocks[0].updateAllDir(Movement.LEFT, self.my_snake.blocks[1])

    def startGame(self, event):
        if self.game_stat == self.MAINMENU:
            self.restart()

    def __init__(self, master=None):
        self.w=400
        self.h=400
        self.scale = 20
        self.start_speed = 0.14
        self.speed = self.start_speed

        tk.Frame.__init__(self, master)
        self.game_stat = self.MAINMENU
        self.master.minsize(width=self.w, height=self.h)
        self.master.maxsize(width=self.w, height=self.h)
        self.canvas = tk.Canvas(master, height=self.h, width=self.w)
        self.canvas.pack()
        self.my_snake = SnakeObj(self.scale)
        self.displayStart()

        self.master.bind('<Left>', self.moveLeft)
        self.master.bind('<Right>', self.moveRight)
        self.master.bind('<Up>', self.moveUp)
        self.master.bind('<Down>', self.moveDown)

        self.master.bind('<space>', self.startGame)

    def moveAll(self):
        if self.game_stat != self.STARTED:
            return 0
        self.my_snake.move(self.w, self.h)

    def calcCollision(self):
        if self.game_stat != self.STARTED:
            return 0

        if(self.my_snake.blocks[0].pos == self.food.pos):
            self.speed *= 0.96
            self.my_snake.addBlocks(1)
            self.food.randomize(self.my_snake.blocks)

        for block in self.my_snake.blocks:
            if(self.my_snake.blocks[0].pos == block.pos and self.my_snake.blocks[0] is not block):
                self.canvas.delete("all")
                self.canvas.create_text(self.w/2, self.h/3, font=("Arial", 15), text="Game Over")
                self.displayStart()

    def renderAll(self):
        if self.game_stat == self.MAINMENU:
            return 0
        self.canvas.delete("all")
        self.my_snake.render(self.canvas)
        self.food.render(self.canvas)

        self.canvas.create_text(30, 10, text="Score: " + str(self.my_snake.getScore()))

    def loop(self):
        while(True):
            self.moveAll()
            self.calcCollision()
            self.renderAll()
            waittime = 400
            for i in range(waittime):
                time.sleep(self.speed / waittime)
                self.master.update_idletasks()
                self.master.update()


    def displayStart(self):
        self.game_stat = self.MAINMENU
        self.canvas.create_text(self.w /2, self.h/2, font=("Arial", 20), text="Press Space to start")
        self.canvas.create_text(self.w /2, self.h - self.h/2.4, font=("Arial", 15), text="Score: " + str(self.my_snake.getScore()))

    def restart(self):
        self.game_stat = self.STARTED
        self.speed = self.start_speed
        self.my_snake = SnakeObj(self.scale)
        self.my_snake.addBlocks(3)
        self.food = Food(self.w, self.h, self.scale)
