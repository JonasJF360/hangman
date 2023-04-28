from random import choice
from src.data import words


class Palavra():
    ultima_palavra_acertada: list = []

    def nova_palavra(self) -> tuple:
        """ Essa função seleciona uma palavra da lista
        de palavras juntamente com sua menságem de ajuda. """
        self.remover_palavras_acertadas()
        return tuple(choice(words))

    def add_palavra_acertada(self, palavra: str, dica: str) -> None:
        """ Adiciona a palavra na lista de acertos. """
        self.ultima_palavra_acertada.append([palavra, dica])

    def remover_palavras_acertadas(self) -> None:
        """ Essa função remove a ultima palavra acertada pelo jogador
            da lista de palavras a serem sujeridas. """
        if len(self.ultima_palavra_acertada):
            words.remove(self.ultima_palavra_acertada.pop())

    def acabou_as_palavras(self) -> bool:
        """ Retorna quantas palavas ainda existem na lista. """
        return len(words) == 1
