import requests
import json
import pandas as pd


def get_namestat(nome):
    res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        df = pd.json_normalize(json.loads(res.text))
    else:
        print('Deu ruim no request  :/')
    
    return df