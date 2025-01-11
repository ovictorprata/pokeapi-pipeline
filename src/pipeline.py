from data_extraction import get_pokemons_dataframe
from data_transformation import categorize_base_experience

df_pokemons = get_pokemons_dataframe(10)
df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(categorize_base_experience)
