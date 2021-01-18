import requests
import json
import pandas as pd


def get_namestat(nome):
    res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        df = pd.json_normalize(json.loads(res.text))
        pp = {a['periodo']: a['frequencia'] for a in json.loads(df['res'].to_json())['0']}
        jj = [df['nome'][0], pp]
    else:
        print('Deu ruim no request  :/')
    
    return jj

# df = get_namestat('guilherme')
