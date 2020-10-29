import numpy as np

class node:

    def __init__(self, field):
        self.field = field.copy()
        self.nextNode = ['', '', '', '']
        self.nextVal = [0, 0, 0, 0]