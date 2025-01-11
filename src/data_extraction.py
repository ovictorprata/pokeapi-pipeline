import requests
from pandas import DataFrame
import logging

def fetch_pokemons_data(limit = 100, offset = 0):
    '''
    Fetches a list of Pokémon data from the PokeAPI.

    Parameters:
    limit (int): The number of Pokémon to fetch (default is 100).
    offset (int): The starting point for the fetch (default is 0).

    Returns:
    list: A list of Pokémon data or an empty list if the request fails.
    '''
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'
    try:
        logging.info('Fetching Pokémon list from API...')
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        pokes_data = response.json()
        return pokes_data.get('results')
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch Pokémon data: {e}')
        return []

def fetch_pokemon_details(poke_url):
    '''
    Fetches detailed information for a specific Pokémon from its URL.

    Parameters:
    poke_url (str): The URL of the specific Pokémon to fetch.

    Returns:
    dict or None: The Pokémon's details in a dictionary or None if the request fails.
    '''
    logging.info(f'Fetching details for Pokémon from {poke_url}')
    try:
        response = requests.get(poke_url, timeout=30)
        response.raise_for_status()
        poke_details = response.json()
        return poke_details
    except requests.exceptions.RequestException as e:
        logging.error(f'Failed to fetch Pokémon details: {e}')
        return None

def extract_stats(stats: dict):
    '''
    Extracts HP, attack, and defense stats from a Pokémon's stat data.

    Parameters:
    stats (dict): A dictionary of the Pokémon's stat information.

    Returns:
    tuple: A tuple containing HP, attack, and defense values (or None if missing).
    '''
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
    '''
    Formats a Pokémon's details into a structured dictionary with necessary information.

    Parameters:
    poke_details (dict): A dictionary containing the Pokémon's full details.

    Returns:
    dict: A structured dictionary with ID, name, base experience, types, HP, attack, and defense.
    '''
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
    Fetches Pokémon data, extracts necessary information, and returns it as a DataFrame.

    Parameters:
    poke_qnt (int): The number of Pokémon to fetch and process.

    Returns:
    pandas.DataFrame: A DataFrame containing the Pokémon data or an empty DataFrame if no data is fetched.
    '''
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
    return df
