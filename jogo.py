import os

# Função para limpar o console
def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro, pecas_coletadas, total_pecas):
    limpar_console()
    print(f"Peças coletadas: {pecas_coletadas}/{total_pecas}")
    print()
    for linha in tabuleiro:
        print(" ".join(linha))
    print()

# Função para encontrar a posição do R
def encontrar_posicao(tabuleiro, simbolo):
    for i in range(len(tabuleiro)):
        for j in range(len(tabuleiro[0])):
            if tabuleiro[i][j] == simbolo:
                return (i, j)
    return None

# Função principal do jogo
def jogar(tabuleiro):
    n = len(tabuleiro)
    
    # Conta quantas peças existem
    total_pecas = sum(linha.count("P") for linha in tabuleiro)
    
    pos_r = encontrar_posicao(tabuleiro, "R")
    
    movimentos = {
        "w": (-1, 0),  # cima
        "s": (1, 0),   # baixo
        "a": (0, -1),  # esquerda
        "d": (0, 1)    # direita
    }
    
    pecas_coletadas = 0
    
    imprimir_tabuleiro(tabuleiro, pecas_coletadas, total_pecas)
    
    while pecas_coletadas < total_pecas:
        comando = input("Digite movimento (w = cima, s = baixo, a = esquerda, d = direita): ").lower()
        
        if comando not in movimentos:
            print("Comando inválido! Use apenas w, s, a ou d.")
            continue
        
        dx, dy = movimentos[comando]
        novo_x = pos_r[0] + dx
        novo_y = pos_r[1] + dy
        
        # Verificar limites do tabuleiro
        if novo_x < 0 or novo_x >= n or novo_y < 0 or novo_y >= n:
            print("Movimento inválido! Fora do tabuleiro.")
            continue
        
        destino = tabuleiro[novo_x][novo_y]
        
        if destino == "X":
            print("Movimento bloqueado! Há um obstáculo (X).")
            continue
        elif destino == "P":
            pecas_coletadas += 1
            print(f"Você coletou uma peça! Total coletado: {pecas_coletadas}")
        
        # Atualiza posição do R no tabuleiro
        tabuleiro[pos_r[0]][pos_r[1]] = "."
        tabuleiro[novo_x][novo_y] = "R"
        pos_r = (novo_x, novo_y)
        
        imprimir_tabuleiro(tabuleiro, pecas_coletadas, total_pecas)
    
    print("Parabéns! Você coletou todas as peças!")

# Exemplo de tabuleiro
tabuleiro = [
    [".", ".", ".", "."],
    [".", "R", "X", "P"],
    [".", ".", ".", "."],
    ["P", "X", ".", "."]
]

jogar(tabuleiro)
