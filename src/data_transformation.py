from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
import logging

def categorize_base_experience(base_experience):
    """
    Categorizes Pokémon based on their base experience.

    This function assigns a category to a Pokémon based on its base experience:
    - 'Fraco' for base experience less than 50
    - 'Médio' for base experience between 50 and 100
    - 'Forte' for base experience greater than 100

    Parameters:
    base_experience (int or None): The base experience of the Pokémon. If None, returns None.

    Returns:
    str or None: The category of the Pokémon ('Fraco', 'Médio', 'Forte'), or None if base_experience is None.
    """
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
    """
    Generates a DataFrame with the count of Pokémon by type.

    Processes the 'Tipos' column of the Pokémon DataFrame and calculates the count of Pokémon for each type.

    Parameters:
    df_pokemons (pandas.DataFrame): DataFrame containing Pokémon data, with a 'Tipos' column.

    Returns:
    pandas.DataFrame: A DataFrame with two columns: 'Tipos' (Pokémon type) and 'Quantidade' (count of Pokémon).
    If an error occurs, returns an empty DataFrame.
    """
    logging.info('Generating Pokémon type count DataFrame.')
    try:
        exploded_types = df_pokemons['Tipos'].explode()
        df_type_count = exploded_types.value_counts().reset_index()
        df_type_count.columns = ['Tipos', 'Quantidade']
        return df_type_count
    except Exception as e:
        logging.error(f'Failed to generate Pokémon type count DataFrame: {e}')
        return DataFrame()

def generate_chart_pokemon_type_distribution(df_type_count):
    """
    Generates a column chart for the distribution of Pokémon by type.

    This function creates a bar chart visualizing the count of Pokémon for each type 
    using the input DataFrame, and saves the chart as an image file.

    Parameters:
    df_type_count (pandas.DataFrame): DataFrame with 'Tipos' (Pokémon type) and 'Quantidade' (count of Pokémon).

    Returns:
    None: The chart is saved as an image file in the 'reports' directory.
    """
    logging.info('Generating column chart Pokemon type.')
    ONFLY_COLOR = '#009efa'
    plt.figure(figsize=(12, 8)) 
    ax = sns.barplot(x='Tipos', y='Quantidade', data=df_type_count, err_kws={'linewidth': 0}, color=ONFLY_COLOR)
    for container in ax.containers:
        ax.bar_label(container)
    ax.set_title('Quantidade de pokemons por tipo', fontweight='bold', fontsize=16)
    ax.set_xlabel('Tipo', fontweight='bold') 
    ax.set_ylabel('Quantidade', fontweight='bold')
    plt.xticks(rotation=45, ha='right') 
    plt.savefig('reports/distribuicao_pokemon_tipo.png', bbox_inches='tight')