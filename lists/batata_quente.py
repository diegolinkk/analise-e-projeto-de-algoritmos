from .deque import Deque
def batata_quente(participantes,numero):
    deque = Deque()
    eliminados = []

    #enfilera os nomes
    for participante in participantes:
        deque.add_back(participante)

    while(deque.count > 1):

    #rotaciona até o número recebido
        for _ in range(0,numero):
            deque.add_front(deque.remove_back())
        
    #quando chega no número, elimina e vai pra lista de eliminados
    #retorna a lista dos eliminados (aqui vou printar um a um)
        print(f"{deque.peek_front()} foi eliminado(a)")
        eliminados.append(deque.remove_front())
    
    #retorna o nome do vencedor
    print(f"{deque.peek_front()} venceu a partida")

