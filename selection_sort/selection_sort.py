def selection_sort(lista):
    print(lista)
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        #aqui ele não percorre o ultimo laço pq o valor de j ultrapassa o valor do tamanho da lista
        for j in range(i + 1,tamanho_lista): 
            if(lista[j] < lista[i]):
                lista[i],lista[j] = lista[j], lista[i]
            print(f'i = {i} j = {j}')
    
    print(lista)



lista = [3,2,1,14,77,90123,3,45,6,25,3,4,1]
selection_sort(lista)