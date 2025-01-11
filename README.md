# Pipeline Automatizado de Extração, Transformação e Relatório com PokeAPI

Este projeto foi desenvolvido como parte de um teste técnico para avaliar habilidades em extração, transformação e análise de dados utilizando Python e pandas. O objetivo é consumir dados da PokeAPI, processá-los, gerar relatórios e visualizações, e automatizar o processo em um pipeline eficiente.

## Estrutura de Diretórios

├── Dockerfile # Arquivo de configuração para a criação de imagem Docker

├── logs # Diretório de logs gerados pelo pipeline
└── pipeline.log # Log de execução do pipeline
├── README.md # Este arquivo de documentação
├── reports # Diretório onde os relatórios e gráficos são salvos
├── requirements.txt # Arquivo com as dependências do projeto
├── src # Código fonte do projeto
│├── analyze_data.py # Código para análise estatística e geração de relatórios │
├── data_extraction.py # Código para extração de dados da PokeAPI │
├── data_transformation.py # Código para transformação e categorização dos dados │
├── pipeline.py # Orquestração do pipeline │
└── pycache # Arquivos compilados do Python
└── utils # Funções auxiliares e utilitárias
├── pycache # Arquivos compilados do Python
└── utils.py # Funções auxiliares para o processo

## Requisitos

O projeto depende das seguintes bibliotecas Python:

- `pandas` - Para manipulação e transformação de dados.
- `matplotlib` ou `seaborn` - Para visualização de dados.
- `requests` - Para consumir dados da PokeAPI.
- `logging` - Para gerar logs do pipeline.

Instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Como Executar

- Extração de Dados: O script de extração irá consultar a PokeAPI para coletar dados dos Pokémon.
- Transformação de Dados: Os dados extraídos serão transformados, categorizados e organizados para análise.
- Análise e Relatório: O script gerará um relatório consolidado com tabelas e gráficos.
- Execução do Pipeline: Para rodar o pipeline completo, execute o script pipeline.py.

## Passo a Passo

Suba a imagem Docker (opcional):

Para construir e rodar o container Docker, use os seguintes comandos:

```bash
docker build -t pokemon-pipeline .
docker run pokemon-pipeline
```

Execute o script principal:

Se preferir rodar localmente, basta executar o script pipeline.py:

```bash
python src/pipeline.py
```

O script irá:

1. Extrair os dados da PokeAPI.
2. Transformar os dados com base na categorização de experiência.
3. Gerar um relatório contendo tabelas e gráficos.
4. Salvar o relatório em formato CSV e o gráfico em formato PNG na pasta reports.
5. Logs: Durante a execução do pipeline, os logs serão registrados no arquivo logs/pipeline.log. O uso da biblioteca logging permite o acompanhamento do progresso do pipeline, incluindo eventuais falhas ou erros no processo.

## Como Executar com Docker

#### Dockerfile

O Dockerfile está configurado para permitir que o pipeline seja executado de forma consistente em qualquer ambiente. Ele instala todas as dependências necessárias e configura o ambiente de execução.

Se preferir rodar o pipeline em um ambiente Docker, basta seguir os seguintes passos:

#### Passo 1: Construir a Imagem Docker

Primeiro, construa a imagem Docker utilizando o comando abaixo:

```bash
docker build -t pokemon-pipeline .
```

#### Passo 2: Rodar o Container Docker

Depois de construir a imagem, você pode executar o pipeline com o comando:

```bash
docker run -v $(pwd)/reports:/app/reports pokemon-pipeline
```

O comando acima usa a flag -v para mapear a pasta reports do seu sistema local para a pasta reports dentro do container Docker. Se a pasta reports não existir no seu sistema local, ela será criada automaticamente.

#### O que Acontece ao Rodar com Docker?

**Relatórios e Gráficos:** Ao rodar o pipeline no Docker, todos os relatórios gerados (em formato CSV) e gráficos (em formato PNG) serão salvos na pasta reports/ dentro do container. Graças ao mapeamento do volume (-v $(pwd)/reports:/app/reports), esses arquivos serão automaticamente transferidos para a pasta reports/ do seu sistema local, criando a pasta se necessário.

**Logs:** O progresso do pipeline e qualquer erro serão registrados no arquivo de log logs/pipeline.log dentro do container. Este arquivo também ficará acessível em seu sistema local, dentro da pasta logs/.

💡 Ao final da execução, você encontrará os seguintes arquivos:

- Relatório CSV gerado com as tabelas de Pokémon e análises.
- Gráfico gerado mostrando a distribuição dos Pokémon por tipo, salvo como PNG.

⚠️ **Observações**

- Não é necessário criar a pasta reports manualmente, pois ela será criada automaticamente se não existir no seu diretório local.
- Caso deseje rodar o pipeline sem Docker, basta executar o script src/pipeline.py diretamente, conforme instruções anteriores.

## Funcionalidades do Pipeline

### Extração de Dados:

Acessar a PokeAPI para obter informações sobre 100 Pokémons. Para cada Pokémon, o pipeline extrai detalhes adicionais de:

- ID
- Nome
- Experiência base
- Tipos
- HP
- Ataque

### Transformação de Dados:

1. **Categorização**
   Categorização dos Pokémon em três grupos: "Fraco", "Médio" e "Forte", baseado na experiência base.
   | Experiência base | Categoria |
   | ---------------- | --------- |
   | < 50 | Fraco |
   | Entre 50 e 100 | Médio |
   | > 100 | Forte |

2. **Transformações de Tipos**
   Gera a contagem de Pokémon por tipo e, em seguida, cria um gráfico de barras visualizando a distribuição de Pokémon em cada tipo.

3. **Análise Estatística**
   3.1. Cálculo da média de ataque, defesa e HP por tipo.
   3.2. Exibição dos 5 Pokémon com maior experiência base.

4. **Relatório e Exportação**
   4.1. Geração de relatório em formato CSV com as tabelas e gráficos de análise.
   4.2. Geração de gráfico de distribuição dos Pokémon por tipo.

## Notas Finais

- O pipeline é modularizado para facilitar a manutenção e adaptação.
- Caso ocorram falhas nas requisições à API, erros serão tratados e registrados nos logs.
- O relatório e os gráficos gerados podem ser encontrados na pasta reports.
