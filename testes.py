# from sorting.bubble_sort import bubble_sort
# from sorting.insertion_sort import insertion_sort
# from sorting.selection_sort import selection_sort
# from sorting.merge_sort import merge_sort
# from sorting.quick_sort import quick_sort
# from sorting.quick_sort_2 import quick_sort as quick_sort_2
# from random import sample
from sorting.reverse_sort import reverse_sort
from searching.verificar_item_duplicado import verificar_item_duplicado
from lists.pilha import Pilha

# lista_aleatoria = sample(range(1,1000),15)
# print(lista_aleatoria)

# lista1 = lista_aleatoria[:]
# print(f"Lista  antes do bubble_sort: {lista1}")
# bubble_sort(lista1)
# print(f"Lista  depois do bubble_sort: {lista1}\n")

# lista2 = lista_aleatoria[:]
# print(f"Lista  antes do insertion_sort: {lista2}")
# insertion_sort(lista2)
# print(f"Lista  depois do insertion_sort: {lista2} \n")


# lista3 = lista_aleatoria[:]
# print(f"Lista  antes do selection_sort: {lista3}")
# selection_sort(lista3)
# print(f"Lista  depois do selection_sort: {lista3} \n")

# lista4 = lista_aleatoria[:]
# print(f"Lista  antes do merge_sort: {lista4}")
# merge_sort(lista4)
# print(f"Lista  depois do merge_sort: {lista4} \n")


# lista5 = lista_aleatoria[:]
# print(f"Lista  antes do quick_sort: {lista5}")
# quick_sort(lista5)
# print(f"Lista  depois do quick_sort: {lista5} \n")


# lista6 = lista_aleatoria[:]
# lista6 = [5,3,2,1]
# print(f"Lista  antes do quick_sort 2: {lista6}")
# quick_sort_2(lista6)
# print(f"Lista  depois do quick_sort 2: {lista6} \n")

# TESTE DE INVERSÃO
lista = [3,3,3,3,3,4,5,1]
print(f"Lista ordenada {lista}")
reverse_sort(lista)
print(f"Lista invertida{lista}")

#TESTE DE VERIFICAR DUPLICADOS
lista = [1,2,3,4,5,6,7,8,9,10,4]
print(verificar_item_duplicado(lista))



p1 = Pilha()
print(p1.is_empty())
p1.push(1)
p1.push(3)
p1.push(5)
print(p1.size())
print(p1.is_empty())
print(p1.peek())
print(p1.peek())
print(p1.peek())
p1.clear()
p1.push(12)
print(p1.lista)
print(p1.size())