from random import choice
from src.data import words


class PalavrasJogo:

    def __init__(self) -> None:
        self.palavra_atual: str = ""
        self.dica_atual: str = ""

    def nova_palavra(self) -> None:
        """ Essa  função  seleciona  uma  palavra  da  lista de
            palavras juntamente com sua menságem de dica(ajuda) """
        temp: list = choice(words)
        self.palavra_atual = temp[0].upper()
        self.dica_atual = temp[1]

    def remover_palavras_acertadas(self) -> None:
        """ Essa função remove a ultima palavra acertada pelo
            jogador  da  lista de palavras a serem sujeridas. """
        words.remove([self.palavra_atual.lower(), self.dica_atual])

    def acabou_as_palavras(self) -> bool:
        """ Retorna verdadeiro se não tiver mais palavras na lista. """
        return not words
