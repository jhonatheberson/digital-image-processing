# Filtragem de domínio de frequência

1. Transformada Discreta de Fourier (DFT):

   Transformada de Fourier é transformada e expressar um sinal contínuo como uma conbinação de funções senoidais. A transformada Discreta de Fourier, é aplicada a sinais discretos por exemplo imagens digitais. Portanto DFT mostra uma nova representação da imagem no domínio da frequência. A DFT é muito aplicada para filtrar ruídos periodicos (repetições), assim podemos eliminar esse ruido com DFT. esse figura abaixo mostra isso acontecendo.

   <h1 align="center">
   <img alt="Histogram" title="#Figure 1. Imagem de Entrada" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/img_corrompida_cortina_de_pontos.png"/>
   </h1>

   A imagem a cima está comrrumpida por padrão senoidal (pontos presentes nessa imagem)

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/DFT_img_corrompida.png"/>
   </h1>

   Essa imagem é representação Discreta de Fourrier, da imagem comrrumpida, logo podemos isolar esse ruido e retirar da DFT, e realizar a Transformação Inversa de Fourier.

2. Filtro homomórfico:

   Este filto é usado para correção de luminozidade de uma imagem, onde a luminação não seja uniforme e tamvém é uma aplicação da DFT, com alguns processos antes:

   1. Normalizar a imagem
   2. Aplicar o logritmo a imagem
   3. Calcula DFT
   4. Cria o filtro
   5. Multiplica DFT por Filtro resultando no imagem com iluminação mais uniforme

   E obtivemos a seguinte imagem como saída:

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/filtro_homoformico.png"/>
   </h1>

# Detecção de borda com o algoritmo Canny

1. Algoritmo de Canny:

   O Algoritmo de Canny ou detector de bordas de Canny ele pode ser usado para varios aplicações de processamento de imagens e visão artificial, porque podemos utilizar para segmentação automatica e encontrar objetos em cenas e pontos, é mais rápidos e eficiêntes para encontrar discontinuidades em uma imagem. O objetivo do algoritmo é encontrar bordas situadas em máximos locais do gradiente podendo ser realizado com seguintes passos:

   1. Convolução com o filtro Gaussiano, cálculo da magnitude e ângulo do gradiente.
   2. Afinação das cristas largas do gradiente.
   3. Limiarização com histerese é usada para a quebra do contorno (borda tracejada).

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/biel.png"/>
   </h1>

   Essa imagem acima iremos aplicar a detector de bordas Cannyn resultando na imagem abaixo:

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/bordas_canny.png"/>
   </h1>

2. Algoritmo de pontilhismo:

   Nessa etapa iremos usar o algoritmo de Canny para realizar arte digital, usando pontilhismo, onde a imagem é pintada por pontos e foi usada muito essa técnica por [George Seurat](https://www.georgesseurat.org/):

    <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/pontilhismo.png"/>
   </h1>

   Efeitos pontilhistas interessantes podem ser criados com variantes simples dessa técnica. Exemplo: pular sequências de pixels na imagem de referência para dar a impressão de que os pontos estão separados na tela - isso é bastante comum na arte pontilhista. Outro efeito interessante é realizar deslocamentos aleatórios nos centros dos círculos, para que a imagem gerada permaneca menos artificial. Finalmente, é razoável percorrer a matriz de referência usando uma sequência aleatória, principalmente quando a técnica pontilhista realiza a sobreposição de círculos.

   Irei usar o a técnica de Canny com o pontilhismo para gerar uma minha arte digital:

  <h1 align="center">
  <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/pointillesm.png"/>
  </h1>

# Quantização vetorial com k-médias:

1. k-médias:

   Este exercício tem como objetivo equalizar imagens (frames) capturadas por uma câmera em tempo real e mostrar os seus respectivos histogramas. Para realizar este exercício temos que ter uma noção do que é a equalização de imagens. Equalização é um método que melhora significativamente o contraste da imagem, fazendo com que a visualização de imagens muito escuras ou muito claras se torne melhor. Ela faz a distribuição de ocorrências das cores no histograma, fazendo com que as cores que estão muito concentradas em uma região do histrograma sejas distribuídas por toda a faixa do histograma, fazendo com que certos locais da imagem que antes tinham difícil visualização possam ser destacadas. Temos um exemplo disso logo abaixo:

     <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/sushi.jpg"/>
   </h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/sushi_kmeans.png"/>
   </h1>

   Para realizar este exercício foi necessário utilizar a função split() para separar os canais e armazená-los nos vetores ‘planes[]’ (vetores das componentes R, G e B) para equalizá-los de forma separada através da função equalizeHist(), após a equalização ser feita em cada uma das componentes de cor, é feito o cálculo do histograma para cada uma delas através da função calcHist(). Logo depois, fazemos a operação reversa através da função merge() juntando os canais em uma única matriz. Depois disso é feito a normalização e o plot dos histogramas dos 3 canais no canto superior esquerdo do frame.

2. Kmeans random centers:

   O projeto a seguir utiliza alterações no histograma dos frames de um vídeo para detectar movimentos na cena. Para um detector mais básico, utilizamos apenas uma das componentes de cor da imagem. As entradas para o programa são um valor que indica a sensibilidade do detector, e comparamos o histograma da cena atual com anterior se tiver uma diferença entre o histograma é tocado um alarme, esse dectctor é muito preciso, algo que para aplicação não é necessario.
