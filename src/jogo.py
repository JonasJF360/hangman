""" Importação da biblioteca MessageBox do Tkinter e
    da  classe  que  manipula  as  palavras do jogo. """
from tkinter import messagebox
from src.manipular_palavra import PalavrasJogo

substituir: dict = {
    "A": ['Á', 'À', 'Ã', 'Â'],
    "E": ['É', 'È', 'Ẽ', 'Ê'],
    "I": ['Í', 'Ì', 'Î', 'Ĩ'],
    "O": ['Ó', 'Ò', 'Ô', 'Õ'],
    "U": ['Ú', 'Ù', 'Û', 'Ũ'],
    "C": ['Ç'],
}


class Jogo:

    def __init__(self) -> None:
        self.palavra = PalavrasJogo()

    def acertou_a_palavra(self, letras_adivinhadas) -> bool:
        """ Função que verifica se a palavra já está completa
            e mostra  uma  menságem dizendo  que o usuário já
            adivinhou e irá iniciar um nova partida. """
        if "_" not in letras_adivinhadas:
            mensagem = f"Parabéns, você acertou!\nA palavra era: {self.palavra.palavra_atual}"
            messagebox.showinfo(message=mensagem, title="Hangman")

        return "_" not in letras_adivinhadas

    def contem_a_letra(self, letra_clicada) -> bool:
        """ Verifiva se a letra clicada existe na palavra corrente. """
        if letra_clicada in substituir.keys():
            letra_clicada = self.letra_correspondente(
                letra_clicada, self.palavra.palavra_atual)
        return letra_clicada in self.palavra.palavra_atual

    def letra_correspondente(self, letra_clicada, teste) -> str:
        """ Retorna a letra correspondente da palavra acentuada ou não """
        if letra_clicada in substituir.keys():
            for letra in substituir[letra_clicada]:
                if letra in teste:
                    return letra
        return letra_clicada

    def acabou_as_chances(self, chances_restantes) -> bool:
        """ Caso as imagem_atual tenhar  acabado  será  mostrada
            uma menságem dizendo que o jogador perdeu e irá
            iciar uma nova partida."""
        if chances_restantes == 0:
            mensagem = f"Poxa, você perdeu!\nA palavra era: {self.palavra.palavra_atual}"
            messagebox.showwarning(message=mensagem, title="Hangman")

        return chances_restantes == 0

    def zereu_o_jogo(self) -> None:
        """ Essa função será verdade caso o jogador acerte todas as 
            palavras contidas no jogo, após isso será exibida uma
            menságe e o jogo irá fechar. """
        if self.palavra.acabou_as_palavras():
            mensagem = "Parabéns, você acertou todas as palavras do jogo.\nParabéns por zerar o jogo."
            messagebox.showinfo(message=mensagem, title="Hangman")
            quit()

    def ajuda(self) -> None:
        """ Função mostra a dica da palavra que esta apresentada. """
        messagebox.showinfo(message=self.palavra.dica_atual, title="Hangman")

    def sobre(self) -> None:
        """ Função mostra a dica da palavra que esta apresentada. """
        mensagem: str = "Esse jogo foi criado por Jonas de Jesus Ferreira, " \
                        "e o seu objetivo é que você consiga adivinhar a " \
                        "palavra secreta clicando apenas nas letras do alfabeto.\n" \
                        "Espero que goste, e boa sorte!!!\n\n" \
                        "Código disponível em:\n" \
                        "github.com/JonasJF360/hangman"
        messagebox.showinfo(message=mensagem, title="Hangman")
