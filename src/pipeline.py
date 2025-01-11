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
        # tarefa 1.1 e 1.2: extraindo os dados e criando o dataframe
        df_pokemons = ext.get_pokemons_dataframe(10)

        # tarefa 2.1: categorizando os dados
        logging.info('Categorizing pokemons.')
        df_pokemons['Categoria'] = df_pokemons['Experiência Base'].apply(t.categorize_base_experience)
        
        # tarefa 2.2: 
        df_types = t.get_df_pokemon_by_type(df_pokemons)
        t.generate_chart_pokemon_type_distribution(df_types)
        # tarefa 3
        df_means = a.get_attack_defense_hp_mean_per_type(df_pokemons)
        df_means.to_csv('reports/means_attack_defense_hp.csv')
        print('\n Médias de HP, Ataque e Defesa')
        print('-' * 70)
        print(df_means)
        print('-' * 70)
        df_top_5 = a.get_top_5_highest_base_experience(df_pokemons)
        df_top_5.to_csv('reports/top_5_base_experience.csv')
        print('\nTop 5 pokemons com maiores experiências base')
        print('-' * 70)
        print(df_top_5)
        print('-' * 70)

        logging.info('Pipeline completed successfully.')
    except Exception as e:
        logging.error(f"Pipeline failed: {e}")

if __name__ == "__main__":
    run_pipeline()