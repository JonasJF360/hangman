""" Importação das bibliotecas """
import os
from random import choice

# Lista de palavras
from src.data import words as PALAVRAS


def adivinhar() -> None:
    """ Função para adivinhar palavras """

    # Seleciona uma palavra aleatória da lista e inicializa a lista de letras da palavra
    palavra: str = choice(PALAVRAS).upper()
    letras_palavra: list = list(palavra)

    # Inicializa a lista de letras adivinhadas
    letras_adivinhadas: list = ["_" for letra in letras_palavra]

    status: str = "Adivinhe a palavra secreta\n"
    max_tentativas: int = 6  # Número de tentativas permitidas
    while max_tentativas > 0:  # Loop principal do jogo
        os.system('clear')  # limpa o terminal (mude para 'cls' no windows)

        print(f"{status}Palavra: ", "".join(letras_adivinhadas))

        print("Dica: a palavra tem", len(palavra), "letras.")
        letra: str = input("Digite uma letra: ").upper()[0]

        # Verifica se a letra está na palavra
        if letra in letras_palavra:
            status = f'A letra "{letra.upper()}" está na palavra!\n'
            for i, l in enumerate(letras_palavra):
                if letra == l:
                    letras_adivinhadas[i] = letra
        else:
            status = f'A letra "{letra.upper()}" não está na palavra.\n'
            max_tentativas -= 1

        # Verifica se o usuário adivinhou a palavra
        if "_" not in letras_adivinhadas:
            print("Parabéns! Você adivinhou a palavra:", palavra)
            break

    # Se o usuário não acertar a palavra dentro do número de tentativas permitido
    if max_tentativas == 0:
        print("Você perdeu! A palavra era:", palavra)
