# @title
import random

# Inicializa a posição do alvo aleatoriamente
alvo_linha = random.randint(0, 4)
alvo_coluna = random.randint(0, 4)

acertos = 0
tentativas = 0

print("Treinamento de Mira")
print("Tente acertar o alvo. Digite a posição do alvo no formato 'linha coluna'.")
print("Exemplo: '2 3' para linha 2 e coluna 3.")

while tentativas < 5:
    # Limpa a tela
    print("\n" * 5)

    # Exibe a tela com o alvo
    for i in range(5):
        for j in range(5):
            if i == alvo_linha and j == alvo_coluna:
                print(" X ", end="")  # Alvo
            else:
                print(" . ", end="")  # Espaço vazio
        print()

    tentativa = input("Digite a sua tentativa (linha coluna): ")

    try:
        linha, coluna = map(int, tentativa.split())
        if linha == alvo_linha and coluna == alvo_coluna:
            print("Parabéns! Você acertou o alvo!")
            acertos += 1
        else:
            print("Errou! Tente novamente.")

        tentativas += 1
        # Move o alvo para uma nova posição
        alvo_linha = random.randint(0, 4)
        alvo_coluna = random.randint(0, 4)
    except ValueError:
        print("Entrada inválida. Por favor, digite a linha e a coluna separadas por um espaço.")

print(f"\nSessão de treinamento concluída. Você acertou {acertos} de {tentativas} alvos.")
