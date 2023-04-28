""" Importação das bibliotecas """
import platform
from tkinter import *
from tkinter import messagebox
from random import choice

# Lista de palavras
from src.data import words
ultima_palavra_acertada: list = []

if str(platform.system()) == 'Windows':
    PATH: str = 'src\\img\\'
else:
    PATH: str = 'src/img/'


cores = {
    "azul": '#2a7fff',
    "azul_claro": '#61a0ff',
    "azul_escuro": '#0653c7',
    "branco": "#ffffff",
    "vermelho": '#e69ca6',
    "verde": "#49dbb0",
    "amarelo": "#dac17c",
}


def nova_palavra() -> tuple:
    """ Essa função seleciona uma palavra da lista
    de palavras juntamente com sua menságem de ajuda. """
    remover_palavras_acertadas()
    return tuple(choice(words))


def remover_palavras_acertadas() -> None:
    """ Essa função remove a ultima palavra acertada pelo jogador
        da lista de palavras a serem sujeridas. """
    if len(ultima_palavra_acertada):
        words.remove(ultima_palavra_acertada.pop())


class Application:
    def __init__(self) -> None:
        self.app = Tk()

        self.imagem_atual = 0
        self.chances_restantes = IntVar()
        self.num_acertos = IntVar()
        self.num_erros = IntVar()
        self.palavra = self.dica = ""
        self.letras_palavra: list = []
        self.letras_adivinhadas: list = []

        self.app_window()
        self.app_frames()
        self.app_lables()
        self.app_buttons()

        self.adicionar_funcionalidades()
        self.nova_partida()

        self.app.mainloop()

    ## Definição das partes visuais da aplicação (GUI) ##

    def app_window(self) -> None:
        """ Definição das configurações da janela do aplicativo """
        self.app.title("Hangman")
        self.app.resizable(width=False, height=False)
        self.app.configure(background=cores["azul_claro"])

        width, height = 420, 545
        x_cordinate = int((self.app.winfo_screenwidth()/2) - (width/2))
        y_cordinate = int((self.app.winfo_screenheight()/2) - (height/2)) - 15
        self.app.geometry(f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def app_frames(self) -> None:
        """ Definição dos frames(separações) da aplicação. """
        self.frame_1 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_escuro"], highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        self.frame_2 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_escuro"], highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.13, relwidth=0.96, relheight=0.35)

        self.frame_2_1 = Frame(
            self.frame_2, bd=4, bg=cores["azul"], highlightthickness=0)
        self.frame_2_2 = Frame(
            self.frame_2, bd=4, bg=cores["azul"], highlightthickness=0)
        self.frame_2_1.pack(side=LEFT, expand=True)
        self.frame_2_2.pack(side=RIGHT, expand=True)

        self.frame_3 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_escuro"], highlightthickness=2)
        self.frame_3.place(relx=0.02, rely=0.49, relwidth=0.96, relheight=0.12)

        self.frame_4 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_escuro"], highlightthickness=2)
        self.frame_4.place(relx=0.02, rely=0.62, relwidth=0.96, relheight=0.36)

    def app_lables(self) -> None:
        """ Definição das imagens e textos contidos no app. """
        Label(self.frame_1, text="JOGO DA FORCA", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 28)).pack()

        self.figura = Label(self.frame_2_1, bg=cores["azul"])
        self.figura.pack(expand=True)

        Label(self.frame_2_2, text="CHANCES", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_chances = Label(self.frame_2_2, textvariable=self.chances_restantes, bg=cores["azul"], fg=cores["branco"],
                                font=("Arial", 18, "bold")).pack(expand=True)

        Label(self.frame_2_2, text="ACERTOS", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_acertos = Label(self.frame_2_2, textvariable=self.num_acertos, bg=cores["azul"], fg=cores["branco"],
                                font=("Arial", 18, "bold")).pack(expand=True)

        Label(self.frame_2_2, text="ERROS", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_erros = Label(self.frame_2_2, textvariable=self.num_erros, bg=cores["azul"], fg=cores["branco"],
                              font=("Arial", 18, "bold")).pack(expand=True)

        self.label_palavra = Label(
            self.frame_3, text=self.letras_adivinhadas, bg=cores["azul"], fg=cores["branco"],
            font=("Arial", 20))
        self.label_palavra.pack(pady=7)

    def app_buttons(self) -> None:
        """ Definição dos botões do app com suas respectivas
            configurações e funcionalidades. """
        alfabeto: list = ["ABCDEFG", "HIJKLMN", "OPQRSTU", "VWXYZÇ?"]

        self.botao = {}
        for linha, dado in enumerate(alfabeto):
            self.frame_4.grid_rowconfigure(linha, weight=1, uniform="row")
            for coluna, letra in enumerate(dado):
                self.frame_4.grid_columnconfigure(
                    coluna, weight=1, uniform="column")
                self.botao[letra] = Button(
                    self.frame_4, text=letra, bg=cores["azul_escuro"], foreground=cores["branco"],
                    bd=0, highlightthickness=0, font=("Arial", 11, "bold"))

                self.botao[letra].grid(row=linha, column=coluna, sticky="NSEW")

    ## Definição das regras de negócio da aplicação ##

    def adicionar_funcionalidades(self) -> None:
        """ Essa função adiciona as funcionalidades da aplicação
            como o que acontece quando se clica em um botão ou
            a imágem que será apresentada ao iniciar. """
        # imagem
        self.imagen_hang = [PhotoImage(
            file=f'{PATH}hang{x}.png', width=176, height=176) for x in range(7)]

        self.figura["image"] = self.imagen_hang[self.imagem_atual]

        # botoes
        for letra in self.botao:
            if letra != '?':
                self.botao[letra]["command"] = lambda x=letra: self.letra_clicada(
                    x)
            else:
                self.botao[letra]["command"] = self.ajuda
                self.botao[letra]["bg"] = cores["verde"]
                self.botao[letra]["foreground"] = cores["azul_escuro"]

    def letra_clicada(self, letra) -> None:
        """ Essa função identifica a letra clicada a registra para ser
        inativada até que uma nova palavra seja criada. """
        if not letra in self.letras_adivinhadas:
            self.botao[letra]["state"] = DISABLED
            self.verificar_letra(letra)

    def verificar_letra(self, letra) -> None:
        """ Função que verifica se a letra clicada pertence a palavra corrente.
            Caso acerte aletra ela será mostrada na tela. """
        if letra in self.letras_palavra:
            self.botao[letra]["bg"] = cores["amarelo"]

            for i, l in enumerate(self.letras_palavra):
                if letra == l:
                    self.letras_adivinhadas[i] = letra

                self.label_palavra["text"] = self.letras_adivinhadas
        else:
            self.botao[letra]["bg"] = cores["vermelho"]
            self.imagem_atual += 1
            self.chances_restantes.set(self.chances_restantes.get() - 1)
            self.figura["image"] = self.imagen_hang[self.imagem_atual]

        self.acertou_a_palavra()
        self.acabou_as_chances()

    def acertou_a_palavra(self) -> None:
        """ Função que verifica se a palavra já está completa
            e mostra  uma  menságem dizendo  que o usuário já
            adivinhou e irá iniciar um nova partida. """
        if "_" not in self.letras_adivinhadas:
            mensagem = f"Parabéns, você acertou!\nA palavra era: {self.palavra.upper()}"
            messagebox.showinfo(message=mensagem, title="Hangman")
            self.num_acertos.set(int(self.num_acertos.get()) + 1)
            ultima_palavra_acertada.append([self.palavra, self.dica])
            self.nova_partida()

    def acabou_as_chances(self) -> None:
        """ Caso as imagem_atual tenhar  acabado  será  mostrada
            uma menságem dizendo que o jogador perdeu e irá
            iciar uma nova partida."""
        if self.chances_restantes.get() == 0:
            mensagem = f"Poxa, você perdeu!\nA palavra era: {self.palavra.upper()}"
            messagebox.showwarning(message=mensagem, title="Hangman")
            self.num_erros.set(int(self.num_erros.get()) + 1)
            self.nova_partida()

    def nova_partida(self) -> None:
        """ Essa função reinicia as configurações iniciais
            para que se possa  jogar uma nova partida como
            se fosse a primeira  novamente mantendo apenas
            os erros e acertos já obtidos. """
        self.zereu_o_jogo()

        for letra in self.botao:
            if letra != '?':
                self.botao[letra]["bg"] = cores["azul_escuro"]
                self.botao[letra]["state"] = NORMAL

        self.imagem_atual = 0
        self.chances_restantes.set(6)
        self.figura["image"] = self.imagen_hang[self.imagem_atual]
        self.palavra, self.dica = nova_palavra()
        self.letras_palavra: list = list(self.palavra.upper())
        self.letras_adivinhadas: list = ["_" for _ in self.letras_palavra]
        self.label_palavra["text"] = self.letras_adivinhadas

    def zereu_o_jogo(self) -> None:
        """ Essa função será verdade caso o jogador acerte todas as 
            palavras contidas no jogo, após isso será exibida uma
            menságe e o jogo irá fechar. """
        if len(words) == 1:
            mensagem = "Parabéns, você acertou todas as palavras do jogo.\nParabéns por zerar o jogo."
            messagebox.showinfo(message=mensagem, title="Hangman")
            self.app.destroy()
            quit()

    def ajuda(self) -> None:
        """ Função mostra a dica da palavra que esta apresentada. """
        mensagem = self.dica
        messagebox.showinfo(message=mensagem, title="Hangman")
