from pandas import DataFrame


from data_extraction import get_pokemons_dataframe
import data_transformation as t

df_pokemons = get_pokemons_dataframe(10)
df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(t.categorize_base_experience)
df_types = t.get_df_pokemon_by_type(df_pokemons)
t.plot_pokemon_type_distribution(df_types)





