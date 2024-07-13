'''
A library to communicate with PokeAPI.
https://pokeapi.co/
'''
import requests
from sys import argv
import json

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = '4GLskhG47Uk55brq1r3NDKDsCX0M1UZV'

def main():
    if len(argv) < 2:
        return

    pokemonname = argv[1]
    
    # Get Pokémon information
    pokeinfo = get_pokemon_information(pokemonname)
    
    if pokeinfo:
        # Post Pokémon information to PasteBin
        paste_url = post_to_pastebin(pokemonname, pokeinfo)
        
        if paste_url:
            print(f"Getting information for {pokemonname}...success")
            print(f"Posting new paste to PasteBin...success")
            print(f"Paste URL: {paste_url}")
        else:
            print(f"Getting information for {pokemonname}...success")
            print(f"Posting new paste to PasteBin...failure")
    else:
        print(f"Getting information for {pokemonname}...failure")

def get_pokemon_information(pokemonname):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    name = str(pokemonname)
    name = name.strip().lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    respmessage = requests.get(url)

    if respmessage.ok:
        response = respmessage.json()
        return response
    else:
        print(f"Response code: {respmessage.status_code} ({respmessage.reason})")
        return None

def post_to_pastebin(pokemonname, pokemoninfo):
    """Posts the Pokemon information to PasteBin.

    Args:
        pokemon_name (str): Pokemon name
        pokemon_info (dict): Pokemon information as a dictionary

    Returns:
        str: URL of the newly created paste on PasteBin, if successful. Otherwise None.
    """
    print("Updating PasteBin with a fresh paste...", end='')
    pastetext = json.dumps(pokemoninfo)
    
    postparameters = {
        'API_NISH_KEY': API_DEV_KEY,
        'API_OPTION': 'PASTE',
        'API_PASTE_CODE': pastetext,
        'API_PASTE_NAME': f"{pokemonname}_info",
        'API_PASTE_PRIVATE': 0,  # Publicly listed
        'API_PASTE_EXPIREDDATE': '1M'  # 1 month expiration
    }
    
    respmessages = requests.post(PASTEBIN_API_POST_URL, data=postparameters)
    
    if respmessages.status_code == requests.codes.ok:
        print("Success!")
        return respmessages.text.strip()  # Assuming that the response contains just the paste URL
    else:
        print("Failure")
        print(f'Response code: {respmessages.status_code} ({respmessages.reason})')
        return None

if __name__ == '__main__':
    main()