from random import choice
from src.data import words


class Jogo:
    ultima_palavra_acertada: list = []

    def nova_palavra(self) -> tuple:
        """ Essa função seleciona uma palavra da lista
        de palavras juntamente com sua menságem de ajuda
        e retorna em uma tupla (var1, var2). """
        self.remover_palavras_acertadas()
        temp: list = choice(words)
        return tuple([temp[0].upper(), temp[1]])

    def add_palavra_acertada(self, palavra: str, dica: str) -> None:
        """ Adiciona a palavra na lista de acertos. """
        self.ultima_palavra_acertada.append([palavra.lower(), dica])

    def remover_palavras_acertadas(self) -> None:
        """ Essa função remove a ultima palavra acertada pelo jogador
            da lista de palavras a serem sujeridas. """
        if len(self.ultima_palavra_acertada):
            words.remove(self.ultima_palavra_acertada.pop())

    def acabou_as_palavras(self) -> bool:
        """ Retorna verdadeiro se só restar uma palavra tiver na lista. """
        return len(words) == 1