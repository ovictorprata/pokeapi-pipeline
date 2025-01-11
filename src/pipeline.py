import data_extraction as ext
import data_transformation as t
import analyze_data as a
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.utils import setup_logging


def run_pipeline():
    setup_logging()
    logging.info('Pipeline started.')
    try:
        # tarefa 1
        df_pokemons = ext.get_pokemons_dataframe(10)
        # tarefa 2
        df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(t.categorize_base_experience)
        df_types = t.get_df_pokemon_by_type(df_pokemons)
        t.generate_chart_pokemon_type_distribution(df_types)
        # tarefa 3
        print('\n Médias de HP, Ataque e Defesa')
        print('-' * 70)
        print(a.get_attack_defense_hp_mean_per_type(df_pokemons))
        print('-' * 70)
        print('Top 5 pokemons com maiores experiências base')
        print('-' * 70)
        print(a.get_top_5_highest_base_experience(df_pokemons))
        print('-' * 70)

        a.get_attack_defense_hp_mean_per_type(df_pokemons).to_csv('reports/means_attack_defense_hp.csv')
        a.get_top_5_highest_base_experience(df_pokemons).to_csv('reports/top_5_base_experience.csv')
        logging.info('Pipeline completed successfully.')
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()