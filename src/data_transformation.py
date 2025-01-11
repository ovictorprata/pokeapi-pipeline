from pandas import DataFrame

def categorize_base_experience(base_experinece):
    category =  None
    if base_experinece < 50:
        category = 'Fraco'
    elif base_experinece <= 100:
        category = 'Médio'
    else:
        category = 'Forte'
    return category


def get_df_pokemon_by_type(df_pokemons):
    exploded_types = df_pokemons['Tipos'].explode()
    df_type_count = exploded_types.value_counts().reset_index()
    df_type_count.columns = ['Tipos', 'Quantidade']
    return df_type_count
 