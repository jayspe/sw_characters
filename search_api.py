import requests

def search(search_term='luke'):
  base_url = 'https://swapi.dev/api/people/?search='
  search_url = f'{base_url}{search_term}'
  resp = requests.get(search_url)
  resp_json = resp.json()
  if resp_json.get('results'):
    return resp.json()['results']
  else:
    return None

# Parsing the Name
def parse_name(person):
  name = person.get('name')
  return name

# Parsing the Planet
def parse_planet(person):
  planet_url = person.get('homeworld')
  resp = requests.get(planet_url)
  planet = resp.json().get('name')
  return planet

# Parsing Films
def parse_films(person):
  film_urls = person.get('films')
  films =[fetch_title(film_url) for film_url in film_urls]
  return films

# Fetching the titles
def fetch_title(url):
  film_json = requests.get(url).json()
  film_title = film_json.get('title')
  return film_title

# Formatting the Film Titles
def format_titles(titles):
  new_lines = [title + '\n' for title in titles]
  formatted_titles = '  * ' + '  * '.join(new_lines)
  return formatted_titles

# Building the Description
def person_description(name, planet, titles):
  description = f'{name} is from the planet {planet}. They appear in the following films:\n{titles}'
  return description


# Testing the Functions
if __name__ == '__main__':
  import pprint

  person = search()
  name = parse_name(person)
  planet= parse_planet(person)
  film_list = parse_films(person)
  titles = format_titles(film_list) 
  #description = person_description(name, planet, titles)
  
  
  #pprint.pprint(film_list)
  print(titles)
  #print(description)