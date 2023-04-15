""" Importação das bibliotecas """
from tkinter import *
from random import choice
from tkinter import messagebox

# Lista de palavras
from src.data import words as PALAVRAS

app = Tk()

cores = {
    "azul_claro": '#153553',
    "nada": '#3b7bb6',
    "azul": '#2f6597',
    "branco": "#fff",
    "verde": "#309979",
    "amarelo": "#bd9f4f",
}

# Funções do aplicativo


def nova_palavra() -> list:
    palavra = choice(PALAVRAS)
    return palavra


class Application:
    def __init__(self) -> None:
        self.app = app

        self.chances = 0
        self.letras_clicadas: list = []

        self.palavra: list = nova_palavra()
        self.letras_palavra: list = list(self.palavra[0].upper())
        self.letras_adivinhadas: list = ["_" for letra in self.letras_palavra]

        self.janela()
        self.frames_do_app()
        self.lables_do_app()
        self.buttons_do_app()
        self.app.mainloop()

    def janela(self) -> None:
        self.app.title("Hangman")
        self.app.resizable(width=False, height=False)
        self.app.configure(background=cores["nada"])

        width = 420
        height = 545
        x_cordinate = int((self.app.winfo_screenwidth()/2) - (width/2))
        y_cordinate = int((self.app.winfo_screenheight()/2) -
                          (height/2)) - 15
        self.app.geometry(
            f"{width}x{height}+{x_cordinate}+{y_cordinate}")

    def frames_do_app(self) -> None:
        self.frame_1 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_claro"], highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.1)

        self.frame_2 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_claro"], highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.13, relwidth=0.96, relheight=0.35)

        self.frame_3 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_claro"], highlightthickness=2)
        self.frame_3.place(relx=0.02, rely=0.49, relwidth=0.96, relheight=0.12)

        self.frame_4 = Frame(self.app, bd=4, bg=cores["azul"],
                             highlightbackground=cores["azul_claro"], highlightthickness=2)
        self.frame_4.place(relx=0.02, rely=0.62, relwidth=0.96, relheight=0.36)

    def lables_do_app(self) -> None:
        lable_titulo = Label(
            self.frame_1, text="JOGO DA FORCA", bg=cores["azul"], fg="#fff",  font=("Arial", 28))
        lable_titulo.pack()

        self.hang = [
            PhotoImage(file='src/img/hang0.png', width=180, height=180),
            PhotoImage(file='src/img/hang1.png', width=180, height=180),
            PhotoImage(file='src/img/hang2.png', width=180, height=180),
            PhotoImage(file='src/img/hang3.png', width=180, height=180),
            PhotoImage(file='src/img/hang4.png', width=180, height=180),
            PhotoImage(file='src/img/hang5.png', width=180, height=180),
            PhotoImage(file='src/img/hang6.png', width=180, height=180),
        ]
        self.figura = Label(self.frame_2, image=self.hang[0], bg=cores["azul"])
        self.figura.pack()

        self.label_palavra = Label(
            self.frame_3, text=self.letras_adivinhadas, bg=cores["azul"], fg="#fff",  font=("Arial", 22))
        self.label_palavra.pack()

    def buttons_do_app(self) -> None:
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ?"

        self.botao = {}
        for i, letra in enumerate(alfabeto):
            self.botao[letra] = Button(self.frame_4, text=letra, bg=cores["azul_claro"], fg=cores["azul_claro"],
                                       foreground=cores["branco"], bd=0, highlightthickness=0,
                                       width=4, height=2, font=("Arial", 11))

            if i < 27:
                self.botao[letra]["command"] = lambda x=letra: self.letra_clicada(
                    x)
            else:
                self.botao[letra]["command"] = self.ajuda
                self.botao[letra]["bg"] = cores["verde"]
                self.botao[letra]["fg"] = cores["azul_claro"]
                self.botao[letra]["foreground"] = cores["branco"]

            if i < 7:
                self.botao[letra].grid(row=0, column=i)
            elif i < 14:
                self.botao[letra].grid(row=1, column=i-7)
            elif i < 21:
                self.botao[letra].grid(row=2, column=i-14)
            else:
                self.botao[letra].grid(row=3, column=i-21)

    def letra_clicada(self, letra) -> None:
        if not letra in self.letras_clicadas:
            self.letras_clicadas.append(letra)
            self.verificar_letra(letra)

    def verificar_letra(self, letra) -> None:

        self.botao[letra]["bg"] = cores["amarelo"]
        self.botao[letra]["fg"] = cores["amarelo"]
        self.botao[letra]["foreground"] = cores["branco"]

        if letra in self.letras_palavra:
            for i, l in enumerate(self.letras_palavra):
                if letra == l:
                    self.letras_adivinhadas[i] = letra

                self.label_palavra["text"] = self.letras_adivinhadas
        else:
            self.chances += 1
            self.figura["image"] = self.hang[self.chances]
            if self.chances == 6:
                mensagem = f"Poxa, você perdeu!\nA palavra era: {self.palavra[0].upper()}"
                messagebox.showinfo(message=mensagem, title="Hangman")
                self.reiniciar()

        if "_" not in self.letras_adivinhadas:
            mensagem = f"Parabéns, você acertou!\nA palavra era: {self.palavra[0].upper()}"
            messagebox.showinfo(message=mensagem, title="Hangman")
            self.reiniciar()

    def reiniciar(self) -> None:
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ?"
        for i, letra in enumerate(alfabeto):
            if i < 27:
                self.botao[letra]["bg"] = cores["azul_claro"]
                self.botao[letra]["fg"] = cores["azul_claro"]
                self.botao[letra]["foreground"] = cores["branco"]

        self.chances = 0
        self.letras_clicadas.clear()
        self.figura["image"] = self.hang[self.chances]
        self.palavra: list = nova_palavra()
        self.letras_palavra: list = list(self.palavra[0].upper())
        self.letras_adivinhadas: list = ["_" for letra in self.letras_palavra]
        self.label_palavra["text"] = self.letras_adivinhadas

    def ajuda(self) -> None:
        mensagem = self.palavra[1]
        messagebox.showinfo(message=mensagem, title="Hangman")
