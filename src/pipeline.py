from pandas import DataFrame

import data_extraction as e
import data_transformation as t
import analyze_data as a

def run_pipeline():
    # tarefa 1
    df_pokemons = e.get_pokemons_dataframe(10)
    # tarefa 2
    df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(t.categorize_base_experience)
    df_types = t.get_df_pokemon_by_type(df_pokemons)
    t.generate_chart_pokemon_type_distribution(df_types)
    # tarefa 3
    print(a.get_attack_defense_hp_mean_per_type(df_pokemons))
    print(a.get_top_5_highest_base_experience(df_pokemons))
    a.get_attack_defense_hp_mean_per_type(df_pokemons).to_csv('reports/means_attack_defense_hp.csv')
    a.get_top_5_highest_base_experience(df_pokemons).to_csv('reports/top_5_base_experience.csv')

if __name__ == "__main__":
    run_pipeline()





