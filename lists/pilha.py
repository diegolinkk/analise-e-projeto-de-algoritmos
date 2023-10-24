class Pilha:
    def __init__(self):
        self.lista = []

    def push(self, elemento):
        self.lista.append(elemento)

    def pop(self):
        if(len(self.lista) > 0):
            topo = self.lista[-1]
            del self.lista[-1]
            return topo
        return None

    def peek(self):
        return self.lista[-1]

    def is_empty(self):
        if len(self.lista) > 0:
            return False
        return True

    def clear(self):
        self.lista = []

    def size(self):
        return len(self.lista)