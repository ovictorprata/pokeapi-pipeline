def get_top_5_highest_base_experience(df_pokemons):
    top_5 = df_pokemons.sort_values(by='Experiência Base', ascending=False).head(5)
    top_5_names = top_5[['Nome']].reset_index(drop=True)
    top_5_names.index += 1 
    top_5_names.columns = ['Pokemon']
    top_5_names['Posição'] = top_5_names.index
    top_5_names = top_5_names[['Posição', 'Pokemon']]
    return top_5_names

def get_attack_defense_hp_mean_per_type(df_pokemons):
    df_pokemons = df_pokemons.explode('Tipos')
    mean_values = df_pokemons.groupby('Tipos')[['HP', 'Ataque', 'Defesa']].mean()
    mean_values = mean_values.reset_index()
    mean_values.columns = ['Tipo', 'Média de HP', 'Média de Ataque', 'Média de Defesa']
    return mean_values