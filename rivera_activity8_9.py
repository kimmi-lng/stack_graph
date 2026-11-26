class StackOverflowError(Exception):
    pass # when pushing on empty stack
class InvalidWeightError(Exception):
    pass #when a negative weight is passed

class BoundedStack:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError
        self.capacity = capacity
        self.items = []

    def push(self, item) -> None:
        if len(self.items) >= self.capacity:
            raise StackOverflowError
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError
        return self.items.pop()
    
    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item):
        return item in self.items

