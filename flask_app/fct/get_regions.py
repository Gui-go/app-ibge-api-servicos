import requests
import json
import pandas as pd


def get_regions(uf):
    list_uf = {
        'RO': ['11', 'Rondônia'],
        'AC': ['12', 'Acre'],
        'AM': ['13', 'Amazonas'],
        'RR': ['14', 'Roraima'],
        'PA': ['15', 'Pará'],
        'AP': ['16', 'Amapá'],
        'TO': ['17', 'Tocantins'],
        'MA': ['21', 'Maranhão'],
        'PI': ['22', 'Piauí'],
        'CE': ['23', 'Ceará'],
        'RN': ['24', 'Rio Grande do Norte'],
        'PB': ['25', 'Paraíba'],
        'PE': ['26', 'Pernambuco'],
        'AL': ['27', 'Alagoas'],
        'SE': ['28', 'Sergipe'],
        'BA': ['29', 'Bahia'],
        'MG': ['31', 'Minas Gerais'],
        'ES': ['32', 'Espírito Santo'],
        'RJ': ['33', 'Rio de Janeiro'],
        'SP': ['35', 'São Paulo'],
        'PR': ['41', 'Paraná'],
        'SC': ['42', 'Santa Catarina'],
        'RS': ['43', 'Rio Grande do Sul'],
        'MS': ['50', 'Mato Grosso do Sul'],
        'MT': ['51', 'Mato Grosso'],
        'GO': ['52', 'Goiás'],
        'DF': ['53', 'Distrito Federal']
    }
    cd_uf = list_uf[uf][0]
    res = requests.get(
        f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{cd_uf}/distritos')
    if res.status_code == 200:
        print('Request realizado com sucesso!')
        df = pd.json_normalize(json.loads(res.text))
        df = df.rename(columns={
            'municipio.id': 'cd_mun',
            'municipio.nome': 'nm_mun',
            'municipio.microrregiao.id': 'cd_micro',
            'municipio.microrregiao.nome': 'nm_micro',
            'municipio.microrregiao.mesorregiao.id': 'cd_meso',
            'municipio.microrregiao.mesorregiao.nome': 'nm_meso',
            'municipio.microrregiao.mesorregiao.UF.sigla': 'uf',
            'municipio.microrregiao.mesorregiao.UF.regiao.nome': 'rg'})
        df = df[['cd_mun', 'nm_mun', 'cd_micro',
                 'nm_micro', 'cd_meso', 'nm_meso', 'uf', 'rg']]
        df = df.drop_duplicates()
    else:
        print('Deu ruim no request  :/')

    return df
