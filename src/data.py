words = [
    ['python', 'Uma linguágem de programação cujo nome é uma homenagem a uma série.'],
    ['programaçao', 'O processo de criação de software ou scripts para direcionar o comportamento de um computador.'],
    ['linguagem', 'Qualquer meio compreensível usado como ferramenta para se comunicar.'],
    ['sistema', 'Uma coleção de elementos interconectados que trabalham juntos para alcançar um objetivo comum.'],
    ['desenvolvimento', 'Se refere a criação, modificação ou ajuste para criar algo novo ou melhorar o que já existe.'],
    ['algoritmo', 'Uma sequencia de instruções, um passo a passo não ambíguo.'],
    ['balisa', 'Para se preparar para enfrentar o transito enquanto apende a dirigir.'],
    ['agua', 'Um dos elementos mais abundantes no planeta Terra e uma base para a vida.'],
    ['banana', 'Fruta comprida e geralmente amarela, porém existe de outras cores.'],
    ['floresta', 'Local com muitos tipos de vegetações diferentes, abrigo de animais.'],
    ['jujuba', 'Doce redondo, geralmente colorido e com vários sabores.'],
    ['padaria', 'Local onde se faz uma grande variedade de massas para vender.'],
    ['cerveja', 'Bebida alcoolica ou não, derivada do trigo, milho ou cevada.'],
    ['lampiao', 'Espécie de lampada antiga alimentadas por liquidos inflamáveis, energia ou gases. muito comum até hoje.'],
    ['farinha', 'Um produto derivado da moagem ou molição de diferentes cereais, como trigo, milho, centeio, arroz ou mandioca.'],
    ['pimenta', 'Uma fruta muito comum em todo o mundo usada para temperar alimento, muito famosa por ter variações picantes.'],
    ['batata', 'Tubérculo que possui muitas espécies, porém é famoso por ser gostoso quando frito em tiras.'],
    ['caveira', 'O que resta de um ser vertebrado após o fim de sua decomposição.'],
    ['juiz', 'Aquele que aplica a lei de forma correta após a avaliação dos fatos.'],
    ['cachorro', 'O melhor amigo do ser humano segumdo as avaliacções populares.'],
    ['gato', 'O arquinimigo dos cahorros, ele é peludo e com temperamento estranho.'],
    ['periquito', 'Ave de pequeno porte da familia dos papagaios.'],
    ['janela', 'Parte de um edifício usada para ventilar ou permitir que a luz natural entre.'],
    ['caminhao', 'Veículo de grande porte geralmente utilizado para levar cargas.'],
    ['mosquito', 'Inseto voador de várias espécies, muito comum em áreas urbanas.'],
    ['legume', 'Vegetais que podem ter seus frutos desenvolvidos tanto na parte exterior da terra como abaixo da terra.'],
    ['raiz', 'Um órgão vegetal que apresenta como função principal a sustentação da planta e a absorção de água e sais minerais.'],
    ['computador', 'Máquina destinada ao processamento de dados, capaz de obedecer a instruções e alcançar um fim determinado.'],
    ['caloteiro', 'Aquele que por vontade própria ou não, não paga suas dívidas.'],
    ['salafrario', ' Indivíduo desonesto, desleal, sem escrúpulos, desprezível, reles, bisbórria, etc.'],
    ['abacaxi', 'Fruto tropical revestido por uma casca áspera, formada pela união das brácteas e sépalas das flores da planta.'],
    ['sapato', 'Item de vestuário utilizado para o conforto e proteção dos pés.'],
    ['sapo', 'Animal que vive em áeas alagadas, e se beijar "vira prícipe".'],
    ['capacete', 'Item de proteção utilizaso para proteger a cabeça.'],
    ['margarida', 'Nome de uma espécie de flor e um nome comum para mulheres.'],
    ['tijolo', 'Geralmente feito de barro e utilizado como base em construções de paredes.'],
    ['tapioca', 'Produto da fécula de mandioca feito para se comer geralmente no café da manhã.'],
    ['rolo', 'Qualquer utensílio e/ou objeto que possua o formato cilíndrico.'],
    ['geladeira', 'Eletrodoméstico onde se conserva os alimentos e produtos perecíveis.'],
    ['hospital', 'Local onde se trata as pessoas que estão com alguma enfermidade.'],
    ['margarina', 'Termo genérico para identificar gorduras alimentares de origem vegetal, substituto da manteiga.'],
    ['martelete', 'Servem para quebrar, cinzelar e demolir desde paredes de tijolo e superfícies de cerâmica, até colunas de concreto e pedras.'],
    ['gema', 'A parte amarela que fica no interior do ovo.'],
    ['berinjela', 'Frutos escuros com interior claro, com coloração roxa, pequenas variações de tonalidades e de formato alongados'],
    ['tomate', 'Fruto vermelho muito utilizado na culinária, de saladas a condimentos e sucos.'],
    ['navio', 'Uma grande embarcação, geralmente dotada de um ou mais conveses.'],
    ['favela', 'Área degradada de uma cidade, caracterizada por moradias precárias, miséria e falta de segurança de posse.'],
    ['calendario', 'sistema para contagem e agrupamento de dias que visa a atender principalmente às necessidades civis e religiosas de uma cultura.'],
    ['planilha',
        'Tabela composta por linhas (horizontais) e colunas (verticais) que tem como objetivo organizar dados.'],
    ['ervilha', 'Legume versátil, da família dos feijões, lentilha, grão-de-bico e soja. Também é rica em carboidratos, proteínas e fibras.'],
    ['onibus', 'Meio de transporte coletivo de grande porte sobe rodovías.'],
    ['carimbo',
        'Geralmente feito de madeira com uma borracha na ponta, uma marcação (impressão) de texto rápida.'],
    ['tela', 'Junções de arames entrelaçados que formam quadrados ou losangos de diversos tamanhos.'],
    ['bandido', 'Aquele que de forma direta ou indireta rouba bens alheios.'],
    ['espirito', 'Porção imaterial ou imortal do ser humano; alma.'],
    ['costela', 'Ossos planos e curvos que constituem a maior parte da caixa torácica.'],
    ['barracao', 'Abrigo, telheiro ou casa provisória, geralmente de madeira para guarda de utensílios.'],
    ['remedio', 'Substância ou recurso utilizado para combater uma dor, uma doença.'],
    ['espirro', 'expulsão reflexa, brusca e sonora do ar pelo nariz e pela boca, provocada por irritação da mucosa nasal; esternutação.'],
    ['grilo', 'Insetos ortópteros, produzem som através de aparelho musical formado pelas nervuras das asas.'],
    ['celular', 'Referente a célula. Espécie de telefone portátil.'],
    ['lençol', 'Se põem na cama para forrar o colchão e cobrir o corpo.'],
    ['parede', 'Fecha as partes externas de um edifício e estabelece suas divisões internas.'],
    ['parafuso', 'Peça cônica ou cilíndrica, estriada em hélice, que se embute girando para fixar outras partes.'],
    ['tesoura', 'Instrumento de corte utilizado para cortar papel ou tecido.'],
    ['cavalo', 'Animais quadrúpedes e apresentam um dedo em cada pata, sendo esse revestido, em sua última falange, por um casco único.'],
    ['zebra', 'Animal selvagem e listrado da família dos equinos.'],
    ['capivara', 'Mamíferos herbívoros que se destacam por levarem o título de maior roedor do mundo.'],
    ['muleta', 'Encosto na parte superior adaptado à axila, no qual se apoia quem tem dificuldade de caminhar.'],
    ['bispo', 'Peça do xadrêz que se move na diagonal. Chefe espiritual de uma diocese.'],
    ['conversa', 'Troca de palavras, de ideias entre pessoas sobre assunto vago ou específico.'],
    ['jantar', 'Uma das refeições diárias, geralmente acontece no fim do dia.'],
    ['anagrama', 'Transposição de letras de palavra ou frase para formar outra palavra ou frase diferente'],
    ['parabola', 'Narrativa alegórica que transmite uma mensagem indireta, por meio de comparação ou analogia.'],
    ['capacidade', 'Potencial para conter, acomodar ou guardar algo; volume. Execução ou rendimento máximo.'],
    ['menino', 'Criança ou adolescente do sexo masculino.'],
    ['zumbido', 'Som ou sensação de som percebido pelo indivíduo, independentemente de estímulo sonoro externo.'],
    ['dormir', 'Repousar para o corpo e a mente, nesse período a consciência está em inatividade.'],
    ['caminho', 'Porção mais ou menos estreita de terreno entre dois lugares por onde alguém pode seguir.'],
    ['estrada', 'Via mais larga que um caminho transitada por pessoas, animais e/ou veículos.'],
    ['passaro', 'Aves que voam.'],
    ['problema', 'Assunto controverso, que pode ser objeto de pesquisas científicas ou discussões acadêmicas.'],
    ['caligrafia', 'Arte ou técnica de escrever à mão, formando letras e outros sinais gráficos elegantes e harmônicos.'],
]


if __name__ == '__main__':
    print(len(words), 'palavras cadastradas.')
