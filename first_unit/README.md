# Manipulando pixels em uma imagem

1. Criando Região Negativa:

   O programa a seguir recebe como entrada uma imagem e coordenadas (x0,y0) e (x1,y1) para desenhar uma região dentro da qual as cores serão invertidas. Esse efeito é obtido através da substituição do valor de um pixel por seu complemento para 255 (se anteriormente o valor fosse 10, vira 245, por exemplo). A imagem abaixo foi colocada como entrada, juntamente com as coordenadas (50,250) e (250, 350).

   <h1 align="center">
   <img alt="Histogram" title="#Figure 1. Imagem de Entrada" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/biel.png"/>
   </h1>

   A imagem será varrida somente entre as linhas e colunas definidas na entrada pelos pontos (x0,y0) e (x1,y1), e somente entre essas que os valores serão substituídos pelo complemento. A imagem abaixo reflete a saída do exemplo acima.

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/negative.png"/>
   </h1>

2. Trocando Regiões:

   Este problema deve receber como entrada uma imagem, e ter como saída a imagem com os quatro quadrantes espelhados trocados. Para esse fim inicialmente declaramos na imagem de entrada 4 regiões de interesse por meio do código abaixo:

   ```
    part_0 = img[0:int(mid_x), 0:int(mid_x)]
    part_1 = img[0:int(mid_x), int(mid_y):data_img[1]]
    part_2 = img[int(mid_x):data_img[0], 0:int(mid_y)]
    part_3 = img[int(mid_x):data_img[0], int(mid_y):data_img[1]]

   ```

   então criamos uma imagem de saída como o clone da imagem de entrada, e colamos as regiões de interesse nas posições corretas, como visto no código abaixo

   ```
    img_modify[0:int(mid_x), 0:int(mid_y)] = part_3
    img_modify[0:int(mid_x), int(mid_y):data_img[1]] = part_2
    img_modify[int(mid_x):data_img[0], 0:int(mid_y)] = part_1
    img_modify[int(mid_x):data_img[0], int(mid_y):data_img[1]] = part_0
   ```

   E obtivemos a seguinte imagem como saída:

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/changeRegions.png"/>
   </h1>

# Preenchendo Regiões

1. Contando Acima de 256 Objetos:

   Considere a figura abaixom, há somente dois tons de cinza (0 e 255) presentes nela, na qual os objetos têm tom de cinza 255 e o fundo tem tom de cinza 0.

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/bolhas.png"/>
   </h1>

   Nesta questão fizemos uma busca por objetos percorrendo toda a imagem, da esquerda para direita e de cima para baixo, quando achamos um objeto na imagem executamos o algoritmo floodfill() e mudamos o tom de cinza dele para um que seja diferente de 0 e 255 e prechemos com o valor do contador de objetos. Assim ocorrerá para todos os objetos que tenham tom de cinza igual a 255. Quando terminar a varredura da imagem, o valor do contador será a quantidade de objetos presentes na imagem e os objetos contados ficarão com o tom de cinza diferentes. Na figura a seguir podemos ver o resultado do processamento da imagem.

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/labeling.png"/>
   </h1>

   Fixamos a rotulação em apenas um tom de cinza porque só existem 256 possibilidades de tons de cinza que um computador consegue distinguir, se houvesse mais de 255 objetos na imagem e o processo de rotulação continuasse como estava antes (quando achasse um novo objeto acrescentava a ele um tom de cinza a mais) o floodfill() iria ficar comprometido, pois quando a contagem chegasse em um valor cujo tom de cinza do objeto fosse igualado ou ultrapassasse 255 o mesmo objeto poderia ser contado mais de uma vez, pois valores de tons de cinza maiores do que 255 iriam ser automaticamente normalizados para 255, assim causando mais contagens do que objetos.

2. Contagem de Objetos com Buracos:

   O projeto a seguir recebe uma imagem binária como entrada, objetos sendo brancos e o fundo preto, e conta quantos desses objetos têm buracos (um ou mais) e quantos não têm. Uma vez que vamos estar contando dois tipos distintos de objetos, trocamos a rotulação por dois contadores. Um exemplo de entrada é a imagem a seguir:

    <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/bolhas.png"/>
   </h1>

   Para retirar os objetos que estão em contato com as bordas, inicialmente o programa percorre a borda e se achar uma pixel com 255, usa seedfill para preencher com 0, assim rirando os elementos das bordas

  <h1 align="center">
  <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/noEdge.png"/>
  </h1>

Uma vez que desejamos reconhecer os objetos com buracos, iremos usar o algoritmo de contagem, onde cada obejeto terá uma cor diferente, agora iremos as bolhas com buracos tera duas cores, cinca de acordo com a contagem e 0 no buraco da bolha.portando vamos fazer que a cor de fundo fazendo seedfill em 255 no ponto (0,0) da imagem., levando o fundo para 0. Agora a imagem será varrida em busca de objetos com buracos. Quando um pixel 0 ou seja preto for encontrado, iremos incrementar o contador pois esse objeto é uma bulha com buraco e aplicar seedfill para nesse ponto e no vizinho a direita, com 255, ou seja da cor de fundo, assim fazendo que ele não seja mais contado e tirado da imagem.

  <h1 align="center">
  <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/hobbesWhite.png"/>
  </h1>

  <h1 align="center">
  <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/bobbesHoles.png"/>
  </h1>

# Manipulação de Histograma

1. Equalização:

   Este exercício tem como objetivo equalizar imagens (frames) capturadas por uma câmera em tempo real e mostrar os seus respectivos histogramas. Para realizar este exercício temos que ter uma noção do que é a equalização de imagens. Equalização é um método que melhora significativamente o contraste da imagem, fazendo com que a visualização de imagens muito escuras ou muito claras se torne melhor. Ela faz a distribuição de ocorrências das cores no histograma, fazendo com que as cores que estão muito concentradas em uma região do histrograma sejas distribuídas por toda a faixa do histograma, fazendo com que certos locais da imagem que antes tinham difícil visualização possam ser destacadas. Temos um exemplo disso logo abaixo:

     <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/frame.png"/>
   </h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/histequ.png"/>
   </h1>

   Para realizar este exercício foi necessário utilizar a função split() para separar os canais e armazená-los nos vetores ‘planes[]’ (vetores das componentes R, G e B) para equalizá-los de forma separada através da função equalizeHist(), após a equalização ser feita em cada uma das componentes de cor, é feito o cálculo do histograma para cada uma delas através da função calcHist(). Logo depois, fazemos a operação reversa através da função merge() juntando os canais em uma única matriz. Depois disso é feito a normalização e o plot dos histogramas dos 3 canais no canto superior esquerdo do frame.

2. Detector de Movimentos:

   O projeto a seguir utiliza alterações no histograma dos frames de um vídeo para detectar movimentos na cena. Para um detector mais básico, utilizamos apenas uma das componentes de cor da imagem. As entradas para o programa são um valor que indica a sensibilidade do detector, e comparamos o histograma da cena atual com anterior se tiver uma diferença entre o histograma é tocado um alarme, esse dectctor é muito preciso, algo que para aplicação não é necessario.

# Filtros Espaciais

1. Concatenação de Filtros:

   O Programa fornecido como base possui uma série de filtros espaciais permitindo ao usuário trocar entre eles em tempo real, os filtros são os seguintes:

   - Média

   - Gauss

   - Bordas Verticais

   - Bordas Horizontais

   - Laplaciano

   A esses adicionamos uma opção para a aplicação encadeada dos filtros Gaussiano e Laplaciano, nessa ordem. Para acessar essa nova opção o usuário deve digitar 'x', o caractere digitado serve como input para uma instrução switch, o case x foi adicionado sobre o case g:, que trata a seleção do filtro Gaussiano. Para todos os efeitos o programa está executando uma filtragem com a máscara Gaussiana. Para acompanhar no código qual filtro havia sido selecionado, foi necessária a inclusão da variável char keys, uma vez que no runtime o único registro do filtro selecionado é a máscara em mask. Em cada case foi inserida uma instrução para registrar qual filtro foi selecionado em keys. Após a operação de filtragem foi inserido um condicional que testa se o filtro escolhido foi o 'x', se tiver sido, a segunda filtragem é executada na imagem de saída da primeira, observe o trexo de código:

     <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filtermedia.png"/>
   </h1>

     <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filtergauss.png"/>
   </h1>

     <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filterhorizontal.png"/>
   </h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filtervertical.png"/>
   </h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filterlaplacian.png"/>
   </h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/assets/filterboost.png"/>
   </h1>

   É possível observar nas imagens que naquela tratada inicialmente com o gaussiano, um filtro de borramento, as bordas da imagem são menos evidentes, mais apagadas.

   O código na íntegra pode ser encontrado [aqui](https://github.com/jhonatheberson/digital-image-processing/blob/master/first_unit/ipynb/spatialFilter.ipynb)

# Filtros Espaciais II

1. Tiltshift Estático:

   Tiltshift é um processo de edição de imagem (e de fotografia) que usa o borramento e a angulação da imagem para simular que uma paisagem seja, na verdade, uma miniatura. Esse efeito pode ser obtido pela associação de duas versões de uma mesma imagem, sendo uma com borramento e outra sem. A imagem com borramento é exibida nas margens superior e inferior para simular o efeito de distância, enquanto a imagem em foco aparece no centro, representando justamente o foco da imagem final. Esse programa tem como entrada uma imagem e em tempo de operação pede ao usuário mais 3 inputs. Em sliders que aparecem juntamente com a imagem de saída o usuário pode configurar a posição central da janela de foco, a largura da janela de foco, e a "agressividade" do decaimento entre as duas imagens. A ponderação entre as duas imagens é dada pela função alfa que é função do x, l1, l2 e d, onde x é a linha da imagem, d é o decaimento, e l1 e l2 são as linhas nas quais o alfa é 0.5. l1 pode ser encontrado como a posição da janela menos metade da largura, e l2 a posição da janela mais a metade da largura.

   $$
   alfa(x)=12⋅(tanh(x−l1d)−tanh(x−l2d))alfa(x)=12⋅(tanh(x-l1d)-tanh(x-l2d))
   $$

   As imagens abaixo tem o propósito de ilustrar como a alteração dos parâmetros posição e largura modificam a janela:

2. Tiltshift em Vídeo:
