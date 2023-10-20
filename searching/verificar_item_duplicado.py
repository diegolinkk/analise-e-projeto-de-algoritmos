def verificar_item_duplicado(lista):
    nova_lista = []
    for item in lista:
        if item in nova_lista:
            return True
        else:
            nova_lista.append(item)
    return False