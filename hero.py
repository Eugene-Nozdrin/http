import requests

url = " https://akabab.github.io/superhero-api/api/all.json"
res = requests.get(url=url)
hero_list = ['Hulk', 'Captain America', 'Thanos']
hero_dict = {}

for hero in res.json():
    if hero['name'] in hero_list:
        hero_dict[hero['name']] = hero['powerstats']['intelligence']

hero_dict = dict(sorted(hero_dict.items(), key=lambda item: item[1], reverse=True))
print(f'сымый умный супер герой {list(hero_dict.keys())[0]} с интелектом {list(hero_dict.values())[0]}')

