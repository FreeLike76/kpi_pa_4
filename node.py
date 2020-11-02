import numpy as np


class Node:
    def __init__(self, field, xHist, yHist):
        self.field = field
        self.nextNode = []
        self.xHist = xHist
        self.yHist = yHist
        self.value = 0

    def build(self, depth):
        if depth != 0:
            if not self.nextNode:
                curId = depth % 2
                #up
                if self.field[self.xHist[curId]][self.yHist[curId] - 1] == -1:
                    fieldNext = self.field.copy()
                    fieldNext[self.xHist[curId]][self.yHist[curId] - 1] = curId
                    xHistNext = self.xHist.copy()
                    yHistNext = self.yHist.copy()
                    yHistNext[curId] -= 1
                    self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
                #right
                if self.field[self.xHist[curId] + 1][self.yHist[curId]] == -1:
                    fieldNext = self.field.copy()
                    fieldNext[self.xHist[curId] + 1][self.yHist[curId]] = curId
                    xHistNext = self.xHist.copy()
                    yHistNext = self.yHist.copy()
                    xHistNext[curId] += 1
                    self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
                #down
                if self.field[self.xHist[curId]][self.yHist[curId] + 1] == -1:
                    fieldNext = self.field.copy()
                    fieldNext[self.xHist[curId]][self.yHist[curId] + 1] = curId
                    xHistNext = self.xHist.copy()
                    yHistNext = self.yHist.copy()
                    yHistNext[curId] += 1
                    self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
                #left
                if self.field[self.xHist[curId] - 1][self.yHist[curId]] == -1:
                    fieldNext = self.field.copy()
                    fieldNext[self.xHist[curId] - 1][self.yHist[curId]] = curId
                    xHistNext = self.xHist.copy()
                    yHistNext = self.yHist.copy()
                    xHistNext[curId] -= 1
                    self.nextNode.append(Node(fieldNext, xHistNext, yHistNext))
            for child in self.nextNode:
                child.build(depth - 1)
