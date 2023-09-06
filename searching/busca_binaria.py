def busca_binaria(lista,valor, inicio = 0,fim = None):
    if fim is None:
        fim  = len(lista)
    
    meio = (inicio  + fim) // 2

    if meio >= len(lista) or (inicio == fim):
        return -1
 
    if lista[meio] == valor:
        return meio

    if valor > lista[meio]:
        return busca_binaria(lista,valor,meio + 1, fim)
    elif valor < lista[meio]:
        return busca_binaria(lista,valor,inicio,meio)
    


lista = [1,2,3,4,5]
print(busca_binaria(lista,4))