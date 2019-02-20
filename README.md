# projetoIC

Este projeto tem por objetivo colocar de forma extruturada as informações contidas no site https://ftp.ncbi.nlm.nih.gov/geo/series/

Irei descrever brevemente os passos que estarei seguindo neste documento, como uma breve forma de documentos os passos seguidos


Etapas seguidas para extrair as senteças que serão analisadas

- Baixar os documentos
- Descomprimir os documentos baixados
- Limpando o texto para conter apenas informações relevantes
- Selecionando sentenças candidatas
    - Uma série de técnicas foram aplicadas para refinar a qualidade das sentenças: POS TAG, uso de grep para melhorar a precisão das palavras
- Indexando as sentenças usando lucene
- Treinando CRF para reconhecimento de sentenças relevantes




Pegando os dados que não foram pegos na primeira passada e adicionando eles ao conjunto de documentos
