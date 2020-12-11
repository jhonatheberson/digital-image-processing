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

   Dá-se o nome de quantização ao grupo de técnicas usadas para mapear os dados presentes em um conjunto grande em um conjunto menor de elementos. É normalmente usada para fins de compressão de dados. Quando um grande conjunto de pontos (vetores) é dividido em em grupos de tamanho menor, diz-se que tem uma quantização vetorial, onde cada grupo é representado por um centróide.

Dos vários algoritmos de quantização vetorial que podem ser encontrados na literatura, o k-means está entre os mais populares. É um algoritmo simples que particiona o espaço N-dimensional em células de Voronoi, onde cada célula é determinada por um centro. O conjunto de todos os pontos no espaço cuja distância para um dado centro é menor que para todos os outros centros define a célula.

O algoritmo k-means funciona conforme os seguintes passos:

1. Escolha k como o número de classes para os vetores xi de N amostras, i=1,2,⋯,N.

2. Escolha m1,m2,⋯,mk como aproximações iniciais para os centros das classes.

3. Classifique cada amostra xi usando, por exemplo, um classificador de distância mínima (distância euclideana).

4. Recalcule as médias mj usando o resultado do passo anterior.

5. Se as novas médias são consistentes (não mudam consideravelmente), finalize o algoritmo. Caso contrário, recalcule os centros e refaça a classificação.

  <h1 align="center">
<img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/sushi.jpg"/>
</h1>

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/sushi_kmeans.png"/>
   </h1>

2. Kmeans random centers:

   Algo que se percebe do algoritmo k-means é que cada execução leva a um resultado diferente do resultado anterior. Embora o algoritmo normalmente estabilize, algumas execuções podem criar aglomerações melhores que outras. Logo, é comum executar o algoritmo algumas vezes e verificar qual execução gera melhor compactação dos dados. Uma das medidas de compactação - a usada pelo OpenCV - verifica a soma dos quadrados das distâncias dos pontos da amostra para seus respectivos centros.

   <h1 align="center">
   <img alt="Imagem de Saída" title="#Figure 2. Imagem de Saída" src="https://github.com/jhonatheberson/digital-image-processing/blob/master/second_unit/assets/kmens_10.png"/>
   </h1>
