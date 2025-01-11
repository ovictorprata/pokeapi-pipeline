import requests

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




pokemons = fetch_pokemons_data()

for pokemon in pokemons:
    print(fetch_pokemon_details(pokemon['url']))
    