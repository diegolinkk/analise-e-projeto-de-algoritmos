def reverse_sort(lista):
    start = 0
    if(len(lista) == 2):
        lista[0],lista[1] = lista[1],lista[0]
    else:
        for end in range(len(lista) -1 ,len(lista) //2,-1):
            lista[start],lista[end] = lista[end],lista[start]
            start +=1

# 1 2 3 4 5
# 5 2 3 4 1
# 5 4 3 2 1