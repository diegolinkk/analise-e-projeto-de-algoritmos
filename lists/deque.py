class Deque:
    def __init__(self):
        pass
        self.items = {}
        self.count = 0
        self.lowest_count = None

    def add_front(self, element):
        if self.count == 0:
            self.add_back(element)
        else:
            n = self.count
            while n > self.lowest_count:
                self.items[n] = self.items[n - 1]
                n -= 1
            self.items[self.lowest_count] = element
            self.count +=1

    def add_back(self, element):
        if self.count == 0:
            self.lowest_count = 0
            self.items[self.lowest_count] = element
            self.count +=1
        else:
            self.items[self.count] = element
            self.count +=1

    def remove_front(self):
        if self.is_empty() == False:
            index = self.lowest_count
            while index < (self.count - 1):
                self.items[index] = self.items[index + 1]
                index +=1
            self.count -=1
            del self.items[self.count]
        else:
            return None

    def remove_back(self):
        if self.is_empty() == False:
            self.count -= 1
            elemento = self.items[self.count]
            del self.items[self.count]
            return elemento
        else:
            return None

    def peek_front(self):
        return self.items[self.lowest_count]

    def peek_back(self):
        return self.items[self.count -1]

    def is_empty(self):
        if self.count == 0:
            return True
        return False

    def clear(self):
        self.count = 0
        self.lowest_count = None
        self.items = {}

    def size(self):
        return self.count
    
    def to_string(self):

        if self.is_empty():
            print("O deque está vazio")
        else:
            print(f"Tamanho do deque: {self.size()}")
            print(f"Menor elemento do deque: {self.lowest_count}")
            print("Items: ")
            for key,value in self.items.items():
                print(f"{key} - {value}")