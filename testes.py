from sorting.bubble_sort import bubble_sort
from sorting.insertion_sort import insertion_sort
from sorting.selection_sort import selection_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from random import sample

lista_aleatoria = sample(range(1,1000),15)
print(lista_aleatoria)

lista1 = lista_aleatoria[:]
print(f"Lista  antes do bubble_sort: {lista1}")
bubble_sort(lista1)
print(f"Lista  depois do bubble_sort: {lista1}\n")

lista2 = lista_aleatoria[:]
print(f"Lista  antes do insertion_sort: {lista2}")
insertion_sort(lista2)
print(f"Lista  depois do insertion_sort: {lista2} \n")


lista3 = lista_aleatoria[:]
print(f"Lista  antes do selection_sort: {lista3}")
selection_sort(lista3)
print(f"Lista  depois do selection_sort: {lista3} \n")

lista4 = lista_aleatoria[:]
print(f"Lista  antes do merge_sort: {lista4}")
merge_sort(lista4)
print(f"Lista  depois do merge_sort: {lista4} \n")


lista5 = lista_aleatoria[:]
print(f"Lista  antes do quick_sort: {lista5}")
quick_sort(lista5)
print(f"Lista  depois do quick_sort: {lista5} \n")