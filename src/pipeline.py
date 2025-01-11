from pandas import DataFrame

from data_extraction import get_pokemons_dataframe
from data_transformation import categorize_base_experience, get_df_pokemon_by_type

df_pokemons = get_pokemons_dataframe(10)
df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(categorize_base_experience)
print(get_df_pokemon_by_type(df_pokemons))

