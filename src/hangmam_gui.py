""" Importação das bibliotecas """
import platform
from tkinter import *
from tkinter import messagebox
from random import choice

# Lista de palavras
from src.data import words as PALAVRAS
palavras_jogadas: list = []

if str(platform.system()) == 'Windows':
    PATH: str = 'src\\img\\'
else:
    PATH: str = 'src/img/'

app = Tk()

cores = {
    "azul": '#2a7fff',
    "azul_claro": '#61a0ff',
    "azul_escuro": '#0653c7',
    "branco": "#ffffff",
    "vermelho": '#e69ca6',
    "verde": "#49dbb0",
    "amarelo": "#dac17c",
}


def nova_palavra() -> list:
    """ Essa função seleciona uma palavra da lista
    de palavras juntamente com sua menságem de ajuda. """
    palavra = choice(PALAVRAS)

    while palavra[0] in palavras_jogadas:
        palavra = choice(PALAVRAS)

    return palavra


class Application:
    def __init__(self) -> None:
        self.app = app

        self.chances = 0
        self.num_chances = IntVar()
        self.num_acertos = IntVar()
        self.num_erros = IntVar()
        self.letras_clicadas: list = []

        self.palavra: list = nova_palavra()
        self.letras_palavra: list = list(self.palavra[0].upper())
        self.letras_adivinhadas: list = ["_" for _ in self.letras_palavra]

        self.app_window()
        self.app_frames()
        self.app_lables()
        self.app_buttons()
        self.app.mainloop()

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

        self.hang = [PhotoImage(
            file=f'{PATH}hang{x}.png', width=176, height=176) for x in range(7)]
        self.figura = Label(
            self.frame_2_1, image=self.hang[0], bg=cores["azul"])
        self.figura.pack(expand=True)

        Label(self.frame_2_2, text="CHANCES", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_chances = Label(self.frame_2_2, textvariable=self.num_chances, bg=cores["azul"], fg=cores["branco"],
                                font=("Arial", 18, "bold")).pack(expand=True)

        Label(self.frame_2_2, text="ACERTOS", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_acertos = Label(self.frame_2_2, textvariable=self.num_acertos, bg=cores["azul"], fg=cores["branco"],
                                font=("Arial", 18, "bold")).pack(expand=True)

        Label(self.frame_2_2, text="ERROS", bg=cores["azul"], fg=cores["branco"],
              font=("Arial", 14)).pack(expand=True)
        self.lb_erros = Label(self.frame_2_2, textvariable=self.num_erros, bg=cores["azul"], fg=cores["branco"],
                              font=("Arial", 18, "bold")).pack(expand=True)

        self.num_chances.set((self.chances - 6) * -1)
        self.num_acertos.set(0)
        self.num_erros.set(0)

        self.label_palavra = Label(
            self.frame_3, text=self.letras_adivinhadas, bg=cores["azul"], fg=cores["branco"],
            font=("Arial", 22))
        self.label_palavra.pack(pady=6)

    def app_buttons(self) -> None:
        """ Definição dos botões do app com suas respectivas
        configurações e funcionalidades. """
        alfabeto: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ?"

        self.botao = {}
        for i, letra in enumerate(alfabeto):
            self.botao[letra] = Button(
                self.frame_4, text=letra, bg=cores["azul_escuro"], foreground=cores["branco"],
                bd=0, highlightthickness=0, width=4, height=2, font=("Arial", 11, "bold"))

            if i < 27:
                self.botao[letra]["command"] = lambda x=letra: self.letra_clicada(
                    x)
            else:
                self.botao[letra]["command"] = self.ajuda
                self.botao[letra]["bg"] = cores["verde"]
                self.botao[letra]["foreground"] = cores["azul_escuro"]

            if i < 7:
                self.botao[letra].grid(row=0, column=i)
            elif i < 14:
                self.botao[letra].grid(row=1, column=i-7)
            elif i < 21:
                self.botao[letra].grid(row=2, column=i-14)
            else:
                self.botao[letra].grid(row=3, column=i-21)

    def letra_clicada(self, letra) -> None:
        """ Essa função identifica a letra clicada a registra para ser
        inativada até que uma nova palavra seja criada. """
        if not letra in self.letras_clicadas:
            self.letras_clicadas.append(letra)
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
            self.chances += 1
            self.num_chances.set((self.chances - 6) * -1)
            self.figura["image"] = self.hang[self.chances]

        self.acertou_a_palavra()

    def acertou_a_palavra(self) -> None:
        """ Função que verifica se a palavra já está completa
            e mostra uma menságem dizendo que o usuário já adivinhou.
            caso as chances tenhar acabado também será mostrada uma
            menságem dizendo que o jogador perdeu.
            Ambas irão revelar a palavra secreta """
        if "_" not in self.letras_adivinhadas:
            mensagem = f"Parabéns, você acertou!\nA palavra era: {self.palavra[0].upper()}"
            messagebox.showinfo(message=mensagem, title="Hangman")
            self.num_acertos.set(int(self.num_acertos.get()) + 1)
            palavras_jogadas.append(self.palavra[0])
            self.reiniciar()

        if self.chances == 6:
            mensagem = f"Poxa, você perdeu!\nA palavra era: {self.palavra[0].upper()}"
            messagebox.showwarning(message=mensagem, title="Hangman")
            self.num_erros.set(int(self.num_erros.get()) + 1)
            self.reiniciar()

    def reiniciar(self) -> None:
        """ Essa função reinicia as configurações iniciais
            para que se possa jogar uma nova partida como
            se fosse a primeira novamente. """
        for i, letra in enumerate(self.botao):
            if i < 27:
                self.botao[letra]["bg"] = cores["azul_escuro"]

        self.chances = 0
        self.num_chances.set((self.chances - 6) * -1)
        self.letras_clicadas.clear()
        self.figura["image"] = self.hang[self.chances]
        self.palavra: list = nova_palavra()
        self.letras_palavra: list = list(self.palavra[0].upper())
        self.letras_adivinhadas: list = ["_" for _ in self.letras_palavra]
        self.label_palavra["text"] = self.letras_adivinhadas

    def ajuda(self) -> None:
        """ Função mostra a dica da palavra que esta apresentada. """
        mensagem = self.palavra[1]
        messagebox.showinfo(message=mensagem, title="Hangman")
