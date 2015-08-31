from common import make_request

# target site
pokemon_url = 'http://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_name'


if __name__ == '__main__':
    pokemons = []

    # get the html object
    html = make_request(pokemon_url)

    # access elements by css selector,
    # iterate over matches
    for link in html.cssselect('#mw-content-text a'):
        # some additional filtering
        if 'title' not in link.attrib:
            continue
        if ' (Pokémon)' in link.attrib['title']:
            pokemons.append(link.text)

    print('n pokemons', len(pokemons))

    # save to text file
    with open('pokemons.txt', 'w') as f:
        f.write('\n'.join(pokemons))