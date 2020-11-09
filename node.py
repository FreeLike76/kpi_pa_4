import numpy as np


class Node:
    def __init__(self, field, xHist, yHist):
        self.field = field
        self.nextNode = []
        self.xHist = xHist
        self.yHist = yHist
        self.value = 0
#No alpha-beta
    def build1(self, depth):
        if depth != 0:
            if not self.nextNode:
                self.appendmoves(depth % 2)
            for child in self.nextNode:
                child.build(depth - 1)
        self.eval(depth)
#Optimized
    def build(self, depth):
        if depth != 0:
            if not self.nextNode:
                self.appendmoves(depth % 2)
            for child in self.nextNode:
                child.build(depth - 1)
                if depth % 2 and child.value > 0:
                    break
        self.eval(depth)

    def appendmoves(self, curId):
        # up
        if self.field[self.xHist[curId]][self.yHist[curId] - 1] == -1:
            fieldNext = self.field.copy()
            fieldNext[self.xHist[curId]][self.yHist[curId] - 1] = curId
            xHistNext = self.xHist.copy()
            yHistNext = self.yHist.copy()
            yHistNext[curId] -= 1
            self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
        # right
        if self.field[self.xHist[curId] + 1][self.yHist[curId]] == -1:
            fieldNext = self.field.copy()
            fieldNext[self.xHist[curId] + 1][self.yHist[curId]] = curId
            xHistNext = self.xHist.copy()
            yHistNext = self.yHist.copy()
            xHistNext[curId] += 1
            self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
        # down
        if self.field[self.xHist[curId]][self.yHist[curId] + 1] == -1:
            fieldNext = self.field.copy()
            fieldNext[self.xHist[curId]][self.yHist[curId] + 1] = curId
            xHistNext = self.xHist.copy()
            yHistNext = self.yHist.copy()
            yHistNext[curId] += 1
            self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
        # left
        if self.field[self.xHist[curId] - 1][self.yHist[curId]] == -1:
            fieldNext = self.field.copy()
            fieldNext[self.xHist[curId] - 1][self.yHist[curId]] = curId
            xHistNext = self.xHist.copy()
            yHistNext = self.yHist.copy()
            xHistNext[curId] -= 1
            self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))

    def eval(self, depth):
        id = depth % 2
        if not self.nextNode:
            self.getvalue(id)
        else:
            self.value = self.nextNode[0].value
            for child in self.nextNode:
                if id and child.value > self.value:
                    self.value = child.value
                elif not id and child.value < self.value:
                    self.value = child.value

    def getvalue(self, id):
        if self.field[self.xHist[id]][self.yHist[id] - 1] != -1 \
                and self.field[self.xHist[id] + 1][self.yHist[id]] != -1 \
                and self.field[self.xHist[id]][self.yHist[id] + 1] != -1 \
                and self.field[self.xHist[id] - 1][self.yHist[id]] != -1:
            if id:
                self.value = -36
            else:
                self.value = 36
        else:
            self.value = self.movediff()

    def movediff(self):
        playerview = self.field.copy()
        botview = self.field.copy()
        return countmoves(botview, self.xHist[1], self.yHist[1]) - countmoves(playerview, self.xHist[0], self.yHist[0])



def countmoves(fieldview, x, y):
    value = 0
    if fieldview[x][y - 1] == -1:
        fieldview[x][y - 1] = 0
        value += 1
        value += countmoves(fieldview, x, y - 1)
    if fieldview[x + 1][y] == -1:
        fieldview[x + 1][y] = 0
        value += 1
        value += countmoves(fieldview, x + 1, y)
    if fieldview[x][y + 1] == -1:
        fieldview[x][y + 1] = 0
        value += 1
        value += countmoves(fieldview, x, y + 1)
    if fieldview[x - 1][y] == -1:
        fieldview[x - 1][y] = 0
        value += 1
        value += countmoves(fieldview, x - 1, y)
    return value
