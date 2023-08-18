def insertion_sort(lista):
    print(f'Lista de entrada: {lista}')
    for i in range(1,len(lista)):
        eleito = lista[i]
        j = i -1
        while(j >=0 and eleito < lista[j]):
            lista[j+1] = lista[j]
            j -=1
        lista[j+1] = eleito
    print(lista)


lista = [1, 93,22,33,1,15,9,9,9,17,42,88,34,2,12,3,4,1]
insertion_sort(lista)