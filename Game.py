from tkinter import *
import numpy as np

class Game:
    def __init__(self, size, firstplayer=True, coef=20):
        #Saving size and Gui coef
        self.root = Tk()
        self.size = size
        self.coef = coef

        #Player makes a move first
        if(firstplayer):
            self.turnId = 0
            self.color = "blue"
        else:
            self.turnId = 1
            self.color = "red"

        #Players coords
        self.xHist = [2, self.size - 1]
        self.yHist = [2, self.size - 1]

        # Inf field
        self.matrix = np.zeros((self.size + 2, self.size + 2))
        for i in range (1, self.size + 1):
            for j in range (1, self.size + 1):
                self.matrix[i][j] = -1

        self.matrix[2][2] = 0
        self.matrix[self.size - 1][self.size - 1] = 1
        # GUI creation
        self.canvas = Canvas(self.root, width=self.size * self.coef + 2 * self.coef, height=self.size * self.coef + 2 * self.coef)
        self.canvas.pack()
        frame = Frame(self.root)
        frame.pack(side=BOTTOM)
        self.btn = []
        self.btn.append(Button(frame, text="Up", command=self.moveUp, width=6, height=3))
        self.btn.append(Button(frame, text="Right", command=self.moveRight, width=6, height=3))
        self.btn.append(Button(frame, text="Down", command=self.moveDown, width=6, height=3))
        self.btn.append(Button(frame, text="Left", command=self.moveLeft, width=6, height=3))
        self.btn[0].pack()
        self.btn[1].pack(side=RIGHT)
        self.btn[3].pack(side=LEFT)
        self.btn[2].pack()
        #Drawing field lines
        for i in range(0, size):
            self.canvas.create_line(self.coef, i * self.coef + self.coef,
                             (size - 1) * self.coef + self.coef, i * self.coef + self.coef,
                             dash=(1, 1))
            self.canvas.create_line(i * self.coef + self.coef, self.coef,
                             i * self.coef + self.coef,(self.size - 1) * self.coef + self.coef,
                             dash=(1, 1))

    def changePlayer(self):
        if(self.turnId == 0):
            self.turnId = 1
            self.color = "red"
        else:
            self.turnId = 0
            self.color = "blue"

    def outcome(self, result):
        for button in self.btn:
            button.configure(state=DISABLED)

        window = Toplevel(self.root, width=300, height=200)
        if(result):
            windowl = Label(window, text="You Won")
        else:
            windowl = Label(window, text="You Lost")
        windowb = Button(window, text="Quit", command=self.destroy)
        windowl.pack()
        windowb.pack()

    def destroy(self):
        self.root.destroy()

    def drawLine(self, endx, endy, color):
        self.canvas.create_line(self.xHist[self.turnId] * self.coef,
                                self.yHist[self.turnId] * self.coef,
                                endx,
                                endy,
                                fill=color, width=5)

    def moveUp(self):
        if self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId] - 1] != -1:
            self.drawLine(self.xHist[self.turnId] * self.coef,
                          (self.yHist[self.turnId] - 1) * self.coef,
                          "yellow")
            self.outcome(False)
        else:
            self.drawLine(self.xHist[self.turnId] * self.coef,
                          (self.yHist[self.turnId] - 1) * self.coef,
                          self.color)
            self.yHist[self.turnId] -= 1
            self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId

    def moveRight(self):
        if self.matrix[self.xHist[self.turnId] + 1][self.yHist[self.turnId]] != -1:
            self.drawLine((self.xHist[self.turnId] + 1) * self.coef,
                          self.yHist[self.turnId] * self.coef,
                          "yellow")
            self.outcome(False)
        else:
            self.drawLine((self.xHist[self.turnId] + 1) * self.coef,
                          self.yHist[self.turnId] * self.coef,
                          self.color)
            self.xHist[self.turnId] += 1
            self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId

    def moveDown(self):
        if self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId] + 1] != -1:
            self.drawLine(self.xHist[self.turnId] * self.coef,
                          (self.yHist[self.turnId] + 1) * self.coef,
                          "yellow")
            self.outcome(False)
        else:
            self.drawLine(self.xHist[self.turnId] * self.coef,
                          (self.yHist[self.turnId] + 1) * self.coef,
                          self.color)
            self.yHist[self.turnId] += 1
            self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId

    def moveLeft(self):
        if self.matrix[self.xHist[self.turnId] - 1][self.yHist[self.turnId]] != -1:
            self.drawLine((self.xHist[self.turnId] - 1) * self.coef,
                          self.yHist[self.turnId] * self.coef,
                          "yellow")
            self.outcome(False)
        else:
            self.drawLine((self.xHist[self.turnId] - 1) * self.coef,
                          self.yHist[self.turnId] * self.coef,
                          self.color)
            self.xHist[self.turnId] -= 1
            self.matrix[self.xHist[self.turnId]][self.yHist[self.turnId]] = self.turnId
