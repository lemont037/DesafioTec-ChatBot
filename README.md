# ChatBot voltado para Mercado Financeiro

## Pré-requisitos
1. Uma pasta chamada `ativos` contendo os PDFs a serem convertidos para o ChatBot.

## Instalação
1. Execute o comando:
> pip install -r requirements.txt
2. Execute então o algoritmo `main.py` para executar a pipeline.
> python main.py
3. Interaja com o Bot.

## Pipline
A pipeline consiste em três passos:
1. Converter os PDFs da pasta `ativos` para CSVs estruturados.
2. Treinar o ChatBot com os dados encontrados.
3. Carregar o modelo e executar o chat.

## Observações
Uma vez que a pipeline foi executada, você pode, na próxima vez, executar o bot diretamente com o comando:
> python bot.py
