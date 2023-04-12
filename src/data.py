from random import choice


words = [
    'python', 'programaçao', 'linguagem', 'sistema',
    'desenvolvimento', 'algoritmo', 'balisa', 'agua',
    'banana', 'floresta', 'jujuba', 'padaria', 'cerveja',
    'lampiao', 'farinha', 'pimenta', 'batata', 'caveira',
    'juiz', 'cachorro', 'gato', 'periquito', 'janela',
    'caminhao', 'mosquito', 'legume', 'raiz', 'computador',
    'caloteiro', 'salafrario', 'abacaxi', 'sapato', 'sapo',
    'capacete', 'margarida', 'tijolo', 'tapioca', 'rolo',
    'geladeira', 'hospital', 'margarina', 'martelete', 'gema',
    'berinjela', 'tomate', 'navio', 'favela', 'calendario',
    'planilha', 'ervilha', 'onibus', 'carimbo', 'tela',
    'bandido', 'espirito', 'costela', 'barracao', 'remedio',
    'espirro', 'grilo', 'celular', 'lençol', 'parede',
    'parafuso', 'tesoura', 'cavalo', 'zebra', 'capivara',
    'muleta', 'bispo', 'conversa', 'jantar', 'anagrama',
    'parabola', 'capacidade', 'menino', 'zumbido', 'dormir',
    'caminho', 'estrada', 'passaro', 'problema', 'caligrafia',
]

plvr = [ # Projeto futuro para o botão de interrogação.
    ['python', 'Linguágen de programaçao.'],
    ['programaçao', 'Agendar uma rotina ou tarefa.'],
    ['linguagem', 'O meio usago por um grupo para se comunicar.'],
    ['sistema', 'Uma aplicaçao de computador, ou um meio de organizaçao.'],
]


def nova_palavra() -> list:
    palavra = choice(plvr)
    return palavra


if __name__ == '__main__':
    # testes
    print(nova_palavra())
