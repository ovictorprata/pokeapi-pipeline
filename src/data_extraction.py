import requests
from pandas import DataFrame
import logging

def fetch_pokemons_data(limit = 100, offset = 0):
    '''Function to fetch data of pokemons via PokeAPI'''
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'
    try:
        logging.info('Attempting to fetch Pokémon list from API...')
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        pokes_data = response.json()
        logging.info(f'{len(pokes_data["results"])} Pokémon fetched successfully.')
        return pokes_data.get('results')
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch Pokémon data: {e}')
        return []

def fetch_pokemon_details(poke_url):
    '''Function to fetch additional details of each Pokémon'''
    logging.info(f'Attempting to fetch details for Pokémon from {poke_url}')
    response = requests.get(poke_url)
    try:
        response = requests.get(poke_url, timeout=30)
        response.raise_for_status()
        poke_details = response.json()
        logging.info(f'Details fetched for Pokémon ID {poke_details.get("id")}.')
        return poke_details
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch Pokémon details: {e}')
        return None

def extract_stats(stats: dict):
    '''Extract HP, attack, and defense stats from pokemon's stats'''
    hp = attack = defense = None
    if stats:
        for stat in stats:
            if stat['stat']['name'] == 'hp':
                hp = stat['base_stat']
            elif stat['stat']['name'] == 'attack':
                attack = stat['base_stat']
            elif stat['stat']['name'] == 'defense':
                defense = stat['base_stat']
    else:
        logging.warning('Stats data is missing or empty.')
    return hp, attack, defense

def format_pokemon_necessary_data(poke_details):
    '''Formats a Pokémon's details into a structured dictionary with only necessary infos.'''
    if not poke_details:
        logging.error('Pokémon details are missing or empty.')
        return {}
    hp, attack, defense = extract_stats(poke_details['stats'])
    formatted_data = {
        'ID': poke_details['id'],
        'Nome': poke_details['name'].title(),
        'Experiência Base': poke_details['base_experience'],
        'Tipos': [type['type']['name'].title() for type in poke_details['types']],
        'HP': hp,
        'Ataque': attack,
        'Defesa': defense
    }
    return formatted_data   

def get_pokemons_dataframe(poke_qnt: int):
    '''
    Fetches Pokémon data and returns it as a DataFrame.
    '''
    logging.info(f'Starting the process to fetch {poke_qnt} Pokémon.')
    pokemons_list = fetch_pokemons_data(limit=poke_qnt)
    if not pokemons_list:
        logging.error('No Pokémon data fetched; returning an empty DataFrame.')
        return DataFrame()

    pokes_data = []
    for pokemon in pokemons_list:
        poke_details = fetch_pokemon_details(pokemon['url'])
        if poke_details:
            formatted_poke_data = format_pokemon_necessary_data(poke_details)
            if formatted_poke_data:
                pokes_data.append(formatted_poke_data)
            else:
                logging.warning(f'Formatted data for Pokémon {pokemon["name"]} is missing.')
    
    df = DataFrame(pokes_data)
    if df.empty:
        logging.warning('The resulting DataFrame is empty.')
    else:
        logging.info('Pokémon data successfully transformed into DataFrame.')
    return df
