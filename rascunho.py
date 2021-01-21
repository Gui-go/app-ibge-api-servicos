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


import geopandas as gpd
from shapely.geometry import Point, Polygon
p1 = Point(0,0)
p2 = {
    "type": "Point",
    "coordinates": [
        -73.9617,
        40.8067
        ]
}
print(p1)
polygon = Polygon([(38,38),(40,40),(47,47)])
import geojsonio
geojsonio.display(p2.to_json())
json.loads(p2)


res = requests.get(f'https://servicodados.ibge.gov.br/api/v2/censosss/nomes/guilherme')

res = requests.get(f'https://servicodados.ibge.gov.br/api/v3/agregados')
res1 = pd.json_normalize(json.loads(res.text))
res1.iloc[2][2]

res = requests.get(f'http://servicodados.ibge.gov.br/api/v3/malhas/municipios/4205407?formato=application/vnd.geo+json')
res.content.decode('utf-8')
gj = json.loads(res.content.decode('utf-8'))
type(gj)

json.load(res)
res.content.decode('utf-8').to_json()
json.loads(res.content.decode('utf-8')).to_json()
gj = gpd.read_file(res.text)

res1 = pd.json_normalize(json.loads(res.text))
res1.iloc[0]
