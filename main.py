def mov_valido(labirinto, m, n):
    linha, coluna = len(labirinto), len(labirinto[0])
    return 0 <= m < linha and 0 <= n < coluna and labirinto[m][n] == " "

class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pilha Vazia")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Pilha Vazia")

    def is_empty(self):
        return len(self.items) == 0

    

def eh_possivel_sair(labirinto):
    linha, coluna = len(labirinto), len(labirinto[0])
    p = Pilha()
    p.push((1, 0))  
    percorrido = set()

    while not p.is_empty():
        m, n = p.peek()
        if (m, n) == (linha - 2, coluna - 1):
            return True
        
        proximo_movimento = False
        for direcao_m, direcao_n in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            novo_m, novo_n = m + direcao_m, n + direcao_n
            if mov_valido(labirinto, novo_m, novo_n) and (novo_m, novo_n) not in percorrido:
                p.push((novo_m, novo_n))
                percorrido.add((novo_m, novo_n))
                labirinto[novo_m][novo_n] = "#"
                proximo_movimento = True
                break
        
        if not proximo_movimento:
            p.pop()
    
    return False

labirinto = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

if eh_possivel_sair(labirinto):
    print(True)
else:
    print(False)
