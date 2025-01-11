import requests
from pandas import DataFrame

def fetch_pokemons_data(limit = 100, offset = 0):
    '''Function to fetch data of pokemons via PokeAPI'''
    url = f'https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}'
    response = requests.get(url)
    if response.status_code == 200:
        pokes_data = response.json()
        return pokes_data['results']
    else:
        print(f'Failed to pokemons data {response.status_code}')

def fetch_pokemon_details(poke_url):
    '''Function to fetch additional details of each Pokémon'''
    response = requests.get(poke_url)
    if response.status_code == 200:
        poke_details = response.json()
        return poke_details
    else:
        print(f'Failed to pokemon details: {response.status_code}')

def extract_stats(stats: dict):
    '''Extract HP, attack, and defense stats from pokemon's stats'''
    hp = attack = defense = None
    for stat in stats:
        if stat['stat']['name'] == 'hp':
            hp = stat['base_stat']
        elif stat['stat']['name'] == 'attack':
            attack = stat['base_stat']
        elif stat['stat']['name'] == 'defense':
            defense = stat['base_stat']
    return hp, attack, defense

def format_pokemon_data(poke_details):
    '''Formats a Pokémon's details into a structured dictionary.'''
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
    pokemons_list = fetch_pokemons_data(limit=poke_qnt)

    pokes_data = []
    for pokemon in pokemons_list:
        poke_details = fetch_pokemon_details(pokemon['url'])
        if poke_details:
            formatted_poke_data = format_pokemon_data(poke_details)
            pokes_data.append(formatted_poke_data)
    
    return DataFrame(pokes_data)
