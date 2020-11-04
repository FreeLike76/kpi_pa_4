import node as nd
import numpy as np


class Tree:
    def __init__(self, field, xHist, yHist, mdepth):
        self.mdepth = mdepth
        self.root = nd.Node(field, xHist, yHist)

    def restructure(self):
        self.root.build(self.mdepth)