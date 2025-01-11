# Pipeline Automatizado de Extração, Transformação e Relatório com PokeAPI

Este projeto implementa um pipeline automatizado utilizando Python para consumir dados da PokeAPI, realizar transformações e gerar relatórios e gráficos de análise. O pipeline inclui as etapas de extração, transformação e análise de dados, e pode ser executado localmente ou em um ambiente Docker.

## Estrutura de Diretórios

```
.
├── Dockerfile
├── logs/ --------------- Diretório de logs gerados pelo pipeline
│   └── pipeline.log
├── README.md
├── reports/ ------------ Diretório onde os relatórios e gráficos são salvos
│   ├── distribuicao_pokemon_tipo.png
│   ├── means_attack_defense_hp.csv
│   └── top_5_base_experience.csv
├── requirements.txt
├── src/ ---------------- Código fonte do projeto
│   ├── analyze_data.py
│   ├── data_extraction.py
│   ├── data_transformation.py
│   └── pipeline.py
└── utils/ --------------- Função com o setup de logging
    └── utils.py
```

## Requisitos

Este projeto requer Python 3.x e as seguintes dependências:

- pandas
- requests
- matplotlib
- numpy

Instale as dependências executando:

```bash
pip install -r requirements.txt
```

## Como Executar

### Opção 1) Execução sem Docker

Se preferir rodar o pipeline localmente (sem Docker), siga os passos abaixo:

1.  Certifique-se de que todas as dependências estejam instaladas:

    ```bash
    pip install -r requirements.txt
    ```

2.  Execute o script principal pipeline.py:

    ```bash
    python src/pipeline.py
    ```

    **O script irá:**

- Extrair dados da PokeAPI.
- Realizar as transformações necessárias.
- Gerar relatórios em formato CSV e gráficos em PNG, que serão salvos na pasta reports/.
- Registrar logs da execução no arquivo logs/pipeline.log.

### Opção 2) Execução com Docker

Se preferir rodar o pipeline dentro de um container Docker, siga os passos abaixo:

#### Construir a Imagem Docker:

Primeiro, construa a imagem Docker utilizando o comando abaixo:

```bash

docker build -t pokemon-pipeline .
```

#### Rodar o Container Docker:

Após construir a imagem, execute o pipeline com o comando:

```bash
docker run -v $(pwd)/reports:/app/reports -v $(pwd)/logs:/app/logs pokemon-pipeline
```

O comando acima usa a flag -v para mapear a pasta reports/ do seu sistema local para a pasta reports/ dentro do container. Se a pasta reports/ não existir em seu sistema local, ela será criada automaticamente.

#### O que Acontece ao Rodar com Docker?

- Relatórios em formato CSV e gráficos em PNG serão gerados dentro do container e automaticamente transferidos para a pasta reports/ no seu sistema local.
- Os logs da execução serão registrados no arquivo logs/pipeline.log dentro do container e também estarão acessíveis em seu sistema local.

- Extração de Dados: O script de extração irá consultar a PokeAPI para coletar dados dos Pokémon.
- Transformação de Dados: Os dados extraídos serão transformados, categorizados e organizados para análise.
- Análise e Relatório: O script gerará um relatório consolidado com tabelas e gráficos.
- Execução do Pipeline: Para rodar o pipeline completo, execute o script pipeline.py.

## Funcionalidades do Pipeline

### 1. Extração de Dados

O pipeline acessa a PokeAPI para obter informações sobre 100 Pokémon, extraindo os seguintes dados:

- ID
- Nome
- Experiência Base
- Tipos
- HP
- Ataque

### 2. Transformação de Dados

- **Categorização dos Pokémon:** A experiência base dos Pokémon é usada para categorizar em três grupos: "Fraco", "Médio" e "Forte".

  | Experiência Base | Categoria |
  | ---------------- | --------- |
  | < 50             | Fraco     |
  | Entre 50 e 100   | Médio     |
  | > 100            | Forte     |

- **Distribuição por Tipo:** O pipeline calcula a quantidade de Pokémon de cada tipo e gera um gráfico de barras visualizando essa distribuição.

### 3. Análise Estatística

- Cálculo da média de ataque, defesa e HP por tipo.
- Exibição dos 5 Pokémon com maior experiência base.

### 4. Relatório e Exportação

- Geração de relatório em formato CSV com os dados e análises.
- Geração de gráfico de distribuição dos Pokémon por tipo.

## Notas Finais

- O pipeline é modularizado para facilitar a manutenção e adaptação.
- Caso ocorram falhas nas requisições à API, erros serão tratados e registrados nos logs.
- O relatório e os gráficos gerados podem ser encontrados na pasta reports.
