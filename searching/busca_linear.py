def busca_linear(lista,valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    
    return -1