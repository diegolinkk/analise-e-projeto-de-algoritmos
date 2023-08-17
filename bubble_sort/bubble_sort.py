def bubble_sort(lista):
    for i in range(len(lista),0,-1):
        print(lista)

        #aqui eu retiro 1 do índice da lista
        for j in range(i -1 ):
            current_index = j
            #que é recompensado aqui
            next_index = j+1
            if(lista[current_index] > lista[next_index]):
                lista[current_index],lista[next_index] = lista[next_index], lista[current_index]
    
    print(lista)


lista = [44,33,22,11]
bubble_sort(lista)