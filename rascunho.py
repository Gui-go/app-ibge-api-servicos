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

# def get_regions(uf):
#     res = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/distritos')
#     if res.status_code == 200:
#         print('Request realizado com sucesso!')
#         df = pd.json_normalize(json.loads(res.text))
#         df = df.rename(columns={
#             'municipio.id' : 'cd_mun', 
#             'municipio.nome' : 'nm_mun', 
#             'municipio.microrregiao.id' : 'cd_micro', 
#             'municipio.microrregiao.nome' : 'nm_micro', 
#             'municipio.microrregiao.mesorregiao.id' : 'cd_meso',
#             'municipio.microrregiao.mesorregiao.nome' : 'nm_meso',
#             'municipio.microrregiao.mesorregiao.UF.sigla' : 'uf',
#             'municipio.microrregiao.mesorregiao.UF.regiao.nome' : 'rg'})
#         df = df[['cd_mun', 'nm_mun', 'cd_micro', 'nm_micro', 'cd_meso', 'nm_meso', 'uf', 'rg']]
#         df = df.drop_duplicates()
#         # df = df.to_json()
#     else:
#         print('Deu ruim no request  :/')
    
#     return df






nome = 'guilherme'
res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
df = pd.json_normalize(json.loads(res.text))

def get_names(nome):
    res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        df = pd.json_normalize(json.loads(res.text))
    else:
        print('Deu ruim no request  :/')
    
    return df


df = get_names(nome)
str(df['res'])[5:]






res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censosss/nomes/guilherme')