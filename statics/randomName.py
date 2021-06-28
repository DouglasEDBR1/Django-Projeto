import requests


def RandomName():

    try:
        request = requests.get(f'https://gerador-nomes.herokuapp.com/nome/aleatorio')
        name = []
        name = request.json()
        return f'{name[0]} {name[1]} {name[2]}'
    except:
        name = []


