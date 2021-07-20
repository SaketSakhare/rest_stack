
from exceptions import NegativeStack, StackEmpty, StackFull

class stack:
    def __init__(self, size):
        if size <0:
            raise NegativeStack()
        self.size = size - 1
        self.stack = [None] * size
        self.top_index = -1
    
    def push(self, integer):
        if self.top_index == self.size:
            raise StackFull()
        self.top_index +=1
        self.stack[self.top_index] = integer

    def pop(self):
        if self.top_index != -1:
            top = self.stack[self.top_index]
            self.stack[self.top_index] = None
            self.top_index -= 1
            return top
        else:
            raise StackEmpty()
    
    def peak(self):
        if self.size > 0:
            return self.stack[self.top_index]
        else:
            raise NegativeStack()

