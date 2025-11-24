class stack:
    def __init__(self):
        self.items = [1,2,3,4,5]

    def is_empty(self):
        return len(self.items) == 0

    def push(self):
        self.items.append(10)

    def size(self):
        return len(self.items)
