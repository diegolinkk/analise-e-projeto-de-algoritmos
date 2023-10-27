class Fila():
    def __init__(self):
        self.list = {}
        self.lowest_size = 0
        self.count = 0
    
    def enqueue(self,elem):
        self.list[self.count] = elem
        self.count +=1

    def dequeue(self):
        if self.count <= 0:
            return None
        
        elem = self.list[self.lowest_size]
        self.list.pop(self.lowest_size)
        self.lowest_size +=1
        self.count -= 1
        return elem

    def peek(self):
        if self.count < 0:
            return None
        
        return self.list[self.lowest_size]

    def isEmpty(self):
        if self.count < 1:
            return True
        return False

    def toString(self):
        text = ""
        for value in self.list.values():
            text += value + " "
        print(text)
    
    def size(self):
        return self.count

