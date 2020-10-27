from tkinter import *
import numpy as np

class Game:
    def __init__(self, root, size, firstplayer, coef=20):
        #Saving size and Gui coef
        self.size = size
        self.coef = coef

        #Player makes a move first
        if(firstplayer):
            self.turnId = 1
            self.color = "blue"
        else:
            self.turnId = 2
            self.color = "red"

        #Players coords
        self.xHist = ['x', 1, self.size - 2]
        self.yHist = ['y', 1, self.size - 2]

        # Inf field
        self.matrix = np.zeros((self.size, self.size))
        self.matrix[1][1] = 1
        self.matrix[self.size - 2][self.size - 2] = 2
        # GUI creation
        self.canvas = Canvas(root, width=self.size * self.coef + 2 * self.coef, height=self.size * self.coef + 2 * self.coef)
        self.canvas.pack()
        self.btn = []
        self.btn.append(Button(root, text="Up", command=self.moveUp))
        self.btn.append(Button(root, text="Right", command=self.moveRight))
        self.btn.append(Button(root, text="Down", command=self.moveDown))
        self.btn.append(Button(root, text="Left", command=self.moveLeft))
        for i in self.btn:
            i.pack()
        #Drawing field lines
        for i in range(0, size):
            self.canvas.create_line(self.coef, i * self.coef + self.coef,
                             (size - 1) * self.coef + self.coef, i * self.coef + self.coef,
                             dash=(1, 1))
            self.canvas.create_line(i * self.coef + self.coef, self.coef,
                             i * self.coef + self.coef,(self.size - 1) * self.coef + self.coef,
                             dash=(1, 1))

    def changePlayer(self):
        if(self.turnId == 1):
            self.turnId = 2
            self.color = "red"
        else:
            self.turnId = 1
            self.color = "blue"

    def moveUp(self):
        self.canvas.create_line(self.xHist[self.turnId] * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                self.xHist[self.turnId] * self.coef + self.coef,
                                (self.yHist[self.turnId] - 1) * self.coef + self.coef,
                                fill=self.color, width=5)
        self.yHist[self.turnId] = self.yHist[self.turnId] - 1
        self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId
        self.changePlayer()

    def moveRight(self):
        self.canvas.create_line(self.xHist[self.turnId] * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                (self.xHist[self.turnId] + 1) * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                fill=self.color, width=5)
        self.xHist[self.turnId] = self.xHist[self.turnId] + 1
        self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId
        self.changePlayer()

    def moveDown(self):
        self.canvas.create_line(self.xHist[self.turnId] * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                self.xHist[self.turnId] * self.coef + self.coef,
                                (self.yHist[self.turnId] + 1) * self.coef + self.coef,
                                fill=self.color, width=5)
        self.yHist[self.turnId] = self.yHist[self.turnId] + 1
        self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId
        self.changePlayer()

    def moveLeft(self):
        self.canvas.create_line(self.xHist[self.turnId] * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                (self.xHist[self.turnId] - 1) * self.coef + self.coef,
                                self.yHist[self.turnId] * self.coef + self.coef,
                                fill=self.color, width=5)
        self.xHist[self.turnId] = self.xHist[self.turnId] - 1
        self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId
        self.changePlayer()