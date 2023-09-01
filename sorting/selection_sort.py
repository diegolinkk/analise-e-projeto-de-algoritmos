def selection_sort(lista):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        #aqui ele não percorre o ultimo laço pq o valor de j ultrapassa o valor do tamanho da lista
        for j in range(i + 1,tamanho_lista): 
            if(lista[j] < lista[i]):
                lista[i],lista[j] = lista[j], lista[i]