from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def categorize_base_experience(base_experience):
    if base_experience is None:
        return None
    if base_experience < 50:
        category = 'Fraco'
    elif base_experience <= 100:
        category = 'Médio'
    else:
        category = 'Forte'
    return category


def get_df_pokemon_by_type(df_pokemons):
    try:
        exploded_types = df_pokemons['Tipos'].explode()
        df_type_count = exploded_types.value_counts().reset_index()
        df_type_count.columns = ['Tipos', 'Quantidade']
        return df_type_count
    except Exception as e:
        logging.error(f'Failed to generate Pokémon type count DataFrame: {e}')
        return DataFrame()

def generate_chart_pokemon_type_distribution(df_type_count):
    ONFLY_COLOR = '#009efa'
    ax = sns.barplot(x='Tipos', y='Quantidade', data=df_type_count, err_kws={'linewidth': 0}, color=ONFLY_COLOR)
    for container in ax.containers:
        ax.bar_label(container)
    ax.set_title('Quantidade de pokemons por tipo', fontweight='bold', fontsize=16)
    ax.set_xlabel('Tipo', fontweight='bold') 
    ax.set_ylabel('Quantidade', fontweight='bold')
    plt.savefig('reports/distribuicao_pokemon_tipo.png')