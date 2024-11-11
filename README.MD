# Consumo de arquivo de forma paralela.

## Contexto
O arquivo cno.csv tem > 600 MBs com > 2 milhões de linhas e deve ser processado de forma segura e controlada.

## Objetivo
Permitir o consumo não linear tratando de forma individual cada linha.

## Considerações e obstáculos
O script está parametrizado para processar uma quantidade de linha de forma não blocante, paralelismo, isso permite multiplas execução em paralelo. Dessa forma é possível ajustar o processamento das linhas de acordo com a necessidade.

## Arquivo cno.csv
O arquivo contém informações sobre o Cadastro Nacional de Obras.
- Arquivo: ```cno.zip``` (*ex. Linux: unzip cno.zip*)
- Tamanho: ```231 MB```
- Hash MD5: ```34b1a873525bc570b329c6d9e66defc4```
- [Link do arquivo original](https://arquivos.receitafederal.gov.br/cno/cno.zip)
- Aquivo alvo: ```cno.csv```
- Quantidade de linhas:  ```2.669.957```

## Execução
Todo o arquivo iniciando da linha 1:
- ```python main.py --row-start 1```

As 10 primeira linhas:
- ```python main.py --row-start 1 --row-stop 10```

Somente a linha 1500
- ```python main.py --row-start 1500 --row-stop 1500```

## Log
A execução do script é registrada em log, exemplo:
- ```2024-11-09 16:57:27,542 - INFO - Finalizando: Script.```
- ```2024-11-09 16:57:27,543 - INFO - Linha inicial: 1.```
- ```2024-11-09 16:57:27,543 - INFO - Linha final: 2669957.```
- ```2024-11-09 16:57:27,544 - INFO - Total de linhas: 2669957.```
- ```2024-11-09 16:57:27,544 - INFO - Memória min: 13.89 MB.```
- ```2024-11-09 16:57:27,544 - INFO - Memória max: 13.89 MB.```
- ```2024-11-09 16:57:27,545 - INFO - Tempo de execução: 696.603 segundos.```
